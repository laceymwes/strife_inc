from flask import Flask, render_template, flash, url_for, redirect
from flask import jsonify, make_response, session as login_session
from flask import request
import flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, PrimeWeapon, SecWeapon, Org, Operator, User
import os
import requests
from google.oauth2 import id_token
from google.auth.transport import requests as grequests
import googleapiclient.discovery
import json
import uuid

engine = create_engine('sqlite:///r6db.db')
# bind declarative_base to database
Base.metadata.bind = engine

# instantiate sessionmaker object to transact upon database
DBSession = sessionmaker(bind=engine)
session = DBSession()

strife = Flask(__name__)

# Load CLIENT_ID from Google credentials JSON file
CLIENT_ID = json.loads(open('signin_client.json', 'r').read())['web']['client_id']


@strife.route('/tokensignin/', methods=['POST', 'GET'])
def tokensignin():
    token = request.form.get('idtoken')
    print(token)
    try:
        idinfo = id_token.verify_oauth2_token(token, grequests.Request(), CLIENT_ID)
        userId = idInfo['sub']
    except ValueError:
        response = make_response('Invalid token', 401)
        response.headers['Content-type'] = 'text/html'
        return response
    user_request = requests.get('''
        https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=%s''' % token)
    print('printing user_request.status_code\n')
    print(user_request.status_code)
    if user_request.status_code == '200':
        print('\nrequest response 200 \n')
        data = request.json()
    else:
        response = make_response('Invalid token', 401)
        response.headers['Content-type'] = 'text/html'
        return response
    # if user is an authorized admin, store cookie information
    if checkAuth(data['email']):
        createSession(data)
    return redirect(url_for('index'))



# serve homepage
@strife.route("/")
def index():
    if login_session.get('user_id') is not None:
        return render_template('index.html', CLIENT_ID=CLIENT_ID, name=login_session['name'])
    else:
        return render_template('index.html', CLIENT_ID=CLIENT_ID)

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

def checkAuth(email):
    try:
        authEmail = session.query(Administrator).filter_by(email = email).first()
        return True
    except:
        return False

def createSession(data):
    try:
        user = session.query(User).filter_by(id = data['sub'])
        login_session['user_id'] = user.id
        login_session['name'] = user.name
        return
    except:
        newUser = User(name = data['name'], email = data['email'],
                      image_url = data['picture'], id = data['sub'])
        session.add(newUser)
        session.commit()
        login_session['user_id'] = data['sub']
        login_session['name'] = data['name']
        return

# __name__ attribute is assign '__main__' when .py ran first
if __name__ == '__main__':
    strife.secret_key = str(uuid.uuid4())
    port = int(os.environ.get('PORT', 5000))
    strife.run(host='0.0.0.0', port=port)
