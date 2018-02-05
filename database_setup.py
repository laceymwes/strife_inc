import sys
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship # to define related tables

Base = declarative_base()

class Org(Base): # extend and inherit from declarative_base
    __tablename__ = 'org'
    name = Column( # org_name
    String(20), nullable = False, primary_key = True # primary key for org
    )
    desc = Column( # org_desc, description of the organization
    String(50), nullable = False
    )
    # link tables

class Operator(Base): # extend and inherit from declarative_base
    __tablename__ = 'operator'
    id = Column( # operator_id
    Integer, primary_key = True # primary key for operator
    )
    name = Column( # operator_name
    String(20), nullable = False
    )
    org_name = Column( # operator_org
    String(30), ForeignKey("org.name"))
    # link database tables
    affiliation = relationship(Org)

class PrimeWeapon(Base): # extend and inherit from declarative_base
    __tablename__ = 'prime_weapon'
    name = Column( # prime_weapon_name
    String(20), nullable = False, primary_key = True # primary key for weapon
    )
    caliber = Column( # prime_weapon_caliber
    String(20), nullable = False
    )
    sht_damage = Column( # prime_weapon_damage
    Integer, nullable = False
    )
    lng_damage = Column( # prime_weapon_damage
    Integer, nullable = False
    )
    org_name = Column( # prime_weapon.org
    String(30),  ForeignKey('org.name') # maps to org primary
    )
    # link database tables
    affiliation = relationship(Org)

class SecWeapon(Base): # extend and inherit from declarative_base
    __tablename__ = 'sec_weapon'
    name = Column( # sec_weapon_name
    String(20), nullable = False, primary_key = True # primary key for weapon
    )
    caliber = Column( # sec_weapon_caliber
    String(20), nullable = False
    )
    sht_damage = Column( # sec_weapon_damage
    Integer, nullable = False
    )
    lng_damage = Column(
    Integer, nullable = False
    )
    org_name = Column( # sec_weapon.org
    String(30), ForeignKey('org.name') # maps to org primary
    )
    # link database tables
    affiliation = relationship(Org)








engine = create_engine('sqlite:///r6db.db')

# create database and associate with Base
Base.metadata.create_all(engine)
