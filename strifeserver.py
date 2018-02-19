from flask import Flask, render_template, flash, url_for, redirect
from flask import jsonify, make_response, session as login_session
from flask import request
import flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, PrimeWeapon, SecWeapon, Org, Operator
from database_setup import Administrator, User
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


# serve homepage
@strife.route("/")
def index():
    # if user is logged in, pas user name to template
    if login_session.get('user_id'):
        return render_template('index.html', CLIENT_ID=CLIENT_ID, name=login_session['name'])
    else:
        return render_template('index.html', CLIENT_ID=CLIENT_ID)


@strife.route('/tokensignin', methods=['POST'])
def tokensignin():
    token = request.form.get('idtoken')
    try:
        idInfo = id_token.verify_oauth2_token(token, grequests.Request(), CLIENT_ID)
        userId = idInfo['sub']
    except ValueError:
        response = make_response('Invalid token', 401)
        response.headers['Content-type'] = 'text/html'
        return response
    user_request = requests.get('''
        https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=%s''' % token)
    if user_request.status_code == 200:
        data = user_request.json()
    else:
        response = make_response('Invalid token', 401)
        response.headers['Content-type'] = 'text/html'
        return response
    # check if user is admin
    if checkAuth(data['email']) == True:
        print(data['email'])
        createSession(data)
    else:
        response = make_response('Unauthorized user', 401)
        response.headers['Content-typ'] = 'text/html'
        return response
    return redirect(url_for('index'))

@strife.route('/tokensignout', methods=['POST'])
def tokensignout():
    if login_session.get('user_id') is not None:
        clear_credentials()
        return redirect(url_for('index'))
    else:
        response = make_response('User not admin or not logged in', 401)
        response.headers['Content-type'] = 'text/html'
        return response


def clear_credentials():
    print('clearing credentials')
    del login_session['user_id']
    del login_session['name']
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

# Check administrator table for
def checkAuth(email):
    try:
        email = str(email)
        authEmail = session.query(Administrator).filter_by(email = email).first()
        # query returns None if email is not in admin table
        if authEmail is not None:
            return True
        else:
            return False
    except:
        return False

def createSession(data):
    try:
        user = session.query(User).filter_by(id = data['sub']).first()
        login_session['user_id'] = user.id
        login_session['name'] = user.name
        return
    except:
        admin_email = session.query(Administrator).filter_by(email = data['email']).first()
        newUser = User(name = data['name'], email = data['email'],
                      image_url = data['picture'], id = data['sub'], admin = admin_email)
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
