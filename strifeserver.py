from flask import Flask, render_template, flash, url_for, redirect, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, PrimeWeapon, SecWeapon, Org, Operator
import os


engine = create_engine('sqlite:///r6db.db')
# bind declarative_base to database
Base.metadata.bind = engine

# instantiate sessionmaker object to transact upon database
DBSession = sessionmaker(bind = engine)
session = DBSession()

strife = Flask(__name__)

# serve homepage
@strife.route("/")
def main():
    # SELECT * FROM org;
    orgs = session.query(Org).all()
    return render_template("home.html")

# serve org selection form or org info page
@strife.route("/orgs/", methods=['POST', 'GET'])
def org_stats():
    if request.method == 'GET':
        orgs = session.query(Org).all()
        return render_template("orgpick.html", orgs=orgs)
    if request.method == 'POST':
        # SELECT * FROM org WHERE name = name LIMIT 1;
        org = session.query(Org).filter_by(name = request.form['name']).first()
        # SELECT * FROM operator WHERE org_name = org.name;
        operators = session.query(Operator).filter_by(org_name = org.name).all()
        # SELECT * FROM prime_weapon WHERE org_name = org.name;
        p_weapons = session.query(PrimeWeapon).filter_by(org_name = org.name).all()
        # SELECT * FROM sec_weapon WHERE org_name = org.name;
        s_weapons = session.query(SecWeapon).filter_by(org_name = org.name).all()
        return render_template("orgstats.html", org=org, operators=operators,
        p_weapons=p_weapons, s_weapons=s_weapons)

# serve primary weapon stats page
@strife.route("/weapons/primary/<string:weapon_name>/")
def primary_weapon_stats(weapon_name):
    # # SELECT * FROM prime_weapon WHERE name = weapon_name LIMIT 1;
    weapon = session.query(PrimeWeapon).filter_by(name = weapon_name).first()
    return render_template('weapon.html', weapon = weapon)

# serve secondary weapon stats page
@strife.route("/weapons/secondary/<string:weapon_name>/")
def secondary_weapon_stats(weapon_name):
    # SELECT * FROM sec_weapon WHERE name = weapon_name lIMIT 1;
    weapon = session.query(SecWeapon).filter_by(name = weapon_name).one()
    return render_template('weapon.html', weapon = weapon)

# @strif.route("/<str:weapon_name>/")
# def weapon_stats(weapon_name):

# __name__ attribute is assign '__main__' when .py ran first
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    strife.run(host='0.0.0.0', port=port)
