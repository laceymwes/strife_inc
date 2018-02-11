from flask import Flask, render_template, flash, url_for, redirect
from flask import jsonify, make_response, session as login_session
from flask import request
import flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, PrimeWeapon, SecWeapon, Org, Operator, User
import os
import requests
import google.oauth2.credentials
import google_auth_oauthlib.flow
import json
import uuid

engine = create_engine('sqlite:///r6db.db')
# bind declarative_base to database
Base.metadata.bind = engine

# instantiate sessionmaker object to transact upon database
DBSession = sessionmaker(bind=engine)
session = DBSession()

strife = Flask(__name__)

# Load CLIENT_ID from Google client secrets JSON file
CLIENT_SECRETS = 'client_secrets.json'
SCOPES = ['profile']


# serve homepage
@strife.route("/")
def index():
    # test for state
    if login_session.get('state') is None:
        return render_template("index.html")
    else:
        # pass user info from cookies dictionary
        userName = login_session.get('displayName')
        imageUrl = login_session.get('image_url')
        return render_template('index.html', userName=userName, imageUrl=imageUrl)

@strife.route('/login')
def login():
    # replaces deprecated oauth2client lib flow object
    flow_object = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS,
        scopes=SCOPES
    )
    # must match callback designated in developer console
    # oauth2callback method will handle google auth server response
    # google auth server response will be determined by resource owner
    flow_object.redirect_uri = url_for('oauth2callback', _external=True,
        _scheme='https')


    authorization_url, state = flow_object.authorization_url(
        # use refresh token with out redundant user permission request
        access_type='offline',
        # incremental authorization
        include_granted_scopes='true'
    )

    # store state variable that was just defined ^^^ in cookies dictionary
    login_session['state'] = state

    # authorization_url sends request to google auth server
    # redirect_uri defined above 'oauth2callback'
    return redirect(authorization_url)

@strife.route('/oauth2callback')
def oauth2callback():
    # pull cookie state value down to local state variable
    state = login_session['state']

    # instantiate local flow_object again with same state as original request
    flow_object = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS, scopes=SCOPES, state=state)

    flow_object.redirect_uir = url_for('oauth2callback', _external=True,
        _scheme='https')

    # get auth server response with request.url
    # store response
    authorization_response = flask.request.url
    # parse response and extract refresh and access tokens
    flow_object.fetch_token(authorization_response=authorization_response)

    # store credentials parse from response in local variable
    credentials = flow_object.credentials
    # store credentials in cookies dictionary
    login_session['credentials'] = credentials_to_dict(credentials)

    # request profile information of resource owner
    request = requests.get('https://www.googleapis.com/auth/plus.me')
    data = request.jsonify()
    # response format reference:
    # https://developers.google.com/+/web/api/rest/latest/people/get#response
    login_session['displayName'] = data['displayName']
    login_session['image_url'] = data['image']['url']
    return redirect(url_for('index'))

def credentials_to_dict(credentials):
    return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}

@strife.route('/logout')
def logout():
    # test if session is establish already
    if 'credentials' not in login_session:
        return redirect(url_for('index'))

    credentials = google.oauth2.credentials.Credentials(
    **flask.session['credentials'])

    revoke = requests.post('https://accounts.google.com/o/oauth2/revoke',
      params={'token': credentials.token},
      headers = {'content-type': 'application/x-www-form-urlencoded'})

    status_code = getattr(revoke, 'status_code')
    if status_code == 200:
        clear_credentials()
        return redirect(url_for('index'))
    else:
        return('An error occurred.' + print_index_table())


def clear_credentials():
    if 'credentials' in login_session:
        del login_session['credentials']
        del login_session['displayName']
        del login_session['image_url']
    return


# serve org selection form or org info page
@strife.route("/orgs/", methods=['POST', 'GET'])
def org_stats():
    if request.method == 'GET':
        orgs = session.query(Org).all()
        return render_template("orgpick.html", orgs=orgs)
    if request.method == 'POST':
        # SELECT * FROM org WHERE name = name LIMIT 1;
        org = session.query(Org).filter_by(name=request.form['name']).first()
        # SELECT * FROM operator WHERE org_name = org.name;
        operators = session.query(Operator).filter_by(org_name=org.name).all()
        # SELECT * FROM prime_weapon WHERE org_name = org.name;
        p_weapons = session.query(PrimeWeapon).filter_by(org_name=org.name).all()
        # SELECT * FROM sec_weapon WHERE org_name = org.name;
        s_weapons = session.query(SecWeapon).filter_by(org_name=org.name).all()
        return render_template("orgstats.html", org=org, operators=operators,
                               p_weapons=p_weapons, s_weapons=s_weapons)


# serve primary weapon stats page
@strife.route("/weapons/primary/<string:weapon_name>/")
def primary_weapon_stats(weapon_name):
    # # SELECT * FROM prime_weapon WHERE name = weapon_name LIMIT 1;
    weapon = session.query(PrimeWeapon).filter_by(name=weapon_name).first()
    return render_template('weapon.html', weapon=weapon)


# serve secondary weapon stats page
@strife.route("/weapons/secondary/<string:weapon_name>/")
def secondary_weapon_stats(weapon_name):
    # SELECT * FROM sec_weapon WHERE name = weapon_name lIMIT 1;
    weapon = session.query(SecWeapon).filter_by(name=weapon_name).one()
    return render_template('weapon.html', weapon=weapon)

# @strif.route("/<str:weapon_name>/")
# def weapon_stats(weapon_name):

# create new user entry, accessible only by admin
# def createUser(login_session):
#     user_id = str(uuid.uuid4())
#     new_user = User(name = login_session['username'],
#                     email = login_session['email'],
#                     picture = login_session['picture'],
#                     id = user_id)
#     session.add(new_user)
#     session.commit()
#     return new_user.id



# return whole user entry
def getUserInfo(user_id):
    user = session.query(User).filter_by(id = user_id)
    return user

# attempt to find user entry in user table
def getUserID(email):
    try:
        user = session.query(User).filter_by(email = email).one()
        return user.id
    except:
        return None

# __name__ attribute is assign '__main__' when .py ran first
if __name__ == '__main__':
    strife.secret_key = str(uuid.uuid4())
    port = int(os.environ.get('PORT', 5000))
    strife.run(host='0.0.0.0', port=port)
