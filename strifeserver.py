from flask import Flask, render_template, flash, url_for, redirect, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, PrimeWeapon, SecWeapon, Org, Operator
import os

engine = create_engine('sqlite:///r6db.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

strife = Flask(__name__)

@strife.route("/")
def main():
    orgs = session.query(Org).all()
    return render_template("home.html")

@strife.route("/orgs/", methods=['POST', 'GET'])
def org_stats():
    if request.method == 'GET':
        orgs = session.query(Org).all()
        return render_template("orgpick.html", orgs=orgs)
    if request.method == 'POST':
        org = session.query(Org).filter_by(name = request.form['name']).first()
        operators = session.query(Operator).filter_by(org_name = org.name).all()
        p_weapons = session.query(PrimeWeapon).filter_by(org_name = org.name).all()
        s_weapons = session.query(SecWeapon).filter_by(org_name = org.name).all()
        return render_template("orgstats.html", org=org, operators=operators,
        p_weapons=p_weapons, s_weapons=s_weapons)

@strife.route("/weapons/primary/<string:weapon_name>/")
def primary_weapon_stats(weapon_name):
    weapon = session.query(PrimeWeapon).filter_by(name = weapon_name).first()
    return render_template('weapon.html', weapon = weapon)

@strife.route("/weapons/secondary/<string:weapon_name>/")
def secondary_weapon_stats(weapon_name):
    weapon = session.query(SecWeapon).filter_by(name = weapon_name).one()
    return render_template('weapon.html', weapon = weapon)

# @strif.route("/<str:weapon_name>/")
# def weapon_stats(weapon_name):


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    strife.run(host='0.0.0.0', port=port)
