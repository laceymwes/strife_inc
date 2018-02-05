from database_setup import Base, PrimeWeapon, SecWeapon, Operator, Org
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///r6db.db')
# bind declarative_base to engine
Base.metadata.bind = engine
# create sessionmake object and bind to engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# S.A.T. organization
sat = Org(name = 'S.A.T', desc = '''Special Assault Team. Japanese
Polic Tactical Units.''')

session.add(sat)
session.commit()

print("\nSAT CREATED\n")

hibana = Operator(name = 'Hibana', affiliation = sat)

session.add(hibana)
session.commit()

echo = Operator(name = 'Echo', affiliation = sat)

session.add(echo)
session.commit()

# SAS organization
sas = Org(name = 'SAS', desc = '''Special Air Service. Special forces regiment of
the British Army.''')

sledge = Operator(name = 'Sledge', affiliation = sas)

session.add(sledge)
session.commit()

thatcher = Operator(name = 'Thatcher', affiliation = sas)

session.add(thatcher)
session.commit()

mute = Operator(name = 'Mute', affiliation = sas)

session.add(mute)
session.commit()

smoke = Operator(name = 'Smoke', affiliation = sas)

session.add(smoke)
session.commit()

# FBI SWAT organization
fbi = Org(name = 'FBI SWAT', desc = '''Federal Bureau of Investigation.
Special Weapons and Tactics Unit''')

session.add(fbi)
session.commit()

ash = Operator(name = 'Ash', affiliation = fbi)

session.add(ash)
session.commit()

thermite = Operator(name = 'Thermite', affiliation = fbi)

session.add(thermite)
session.commit()

pulse = Operator(name = 'Pulse', affiliation = fbi)

session.add(pulse)
session.commit()

castle = Operator(name = 'Castle', affiliation = fbi)

session.add(castle)
session.commit()

# GIGN organization
gign = Org(name = 'GIGN', desc = '''National Gendarmerie Intervention Group.
French Armed Forces special operations unit.''')

session.add(gign)
session.commit()

rook = Operator(name = 'Rook', affiliation = gign)

session.add(rook)
session.commit()

twitch = Operator(name = 'Twitch', affiliation = gign)

session.add(twitch)
session.commit()

montagne = Operator(name = 'Montagne', affiliation = gign)

session.add(montagne)
session.commit()

doc = Operator(name = 'Doc', affiliation = gign)

session.add(doc)
session.commit()

# spetznaz organization
spetznaz = Org(name = 'Spetznaz', desc = '''Russian Special Forces''')

session.add(spetznaz)
session.commit()

fuze = Operator(name = 'Fuze', affiliation = spetznaz)

session.add(spetznaz)
session.commit()

glaz = Operator(name = 'Glaz', affiliation = spetznaz)

session.add(glaz)
session.commit()

kapkan = Operator(name = 'Kapkan', affiliation = spetznaz)

session.add(kapkan)
session.commit()

tachanka = Operator(name = 'Tachanka', affiliation = spetznaz)

session.add(tachanka)
session.commit()

# GSG 9 organization
gsg9 = Org(name = 'GSG 9', desc = '''Border Protection Group 9. German Federal
Police. ''')

session.add(gsg9)
session.commit()

blitz = Operator(name = 'Blitz', affiliation = gsg9)

session.add(gsg9)
session.commit()

iq = Operator(name = 'IQ', affiliation = gsg9)

session.add(iq)
session.commit()

jager = Operator(name = 'Jager', affiliation = gsg9)

session.add(jager)
session.commit()

bandit = Operator(name = 'Bandit', affiliation = gsg9)

session.add(bandit)
session.commit()

# JTF 2 organization
jtf2 = Org(name = 'JTF 2', desc = '''Joint Task Force 2. Canadian Special
Operations Forces.''')

session.add(jtf2)
session.commit()

buck = Operator(name = 'Buck', affiliation = jtf2)

session.add(buck)
session.commit()

frost = Operator(name = 'Frost', affiliation = jtf2)

session.add(frost)
session.commit()

# Navy SEALs organization
navyseals = Org(name = 'Navy SEALs', desc = '''U.S. Navy. Sear, Air,
and Land ''')

session.add(navyseals)
session.commit()

blackbeard = Operator(name = 'Blackbeard', affiliation = navyseals)

session.add(blackbeard)
session.commit()

valkyrie = Operator(name = 'Valkyrie', affiliation = navyseals)

session.add(valkyrie)
session.commit()

# BOPE organization
bope = Org(name = 'BOPE', desc = '''Special Police. Rio de Janeiro, Brazil
Military Police Unit. ''')

session.add(bope)
session.commit()

capitao = Operator(name = 'Capitao', affiliation = bope)

session.add(capitao)
session.commit()

caveira = Operator(name = 'caveira', affiliation = bope)

session.add(caveira)
session.commit()

# GEO organization
geo = Org(name = 'GEO', desc = '''Special Operations Group. Spanish National
Police Corps. ''')

session.add(geo)
session.commit()

jackal = Operator(name = 'Jackal', affiliation = geo)

session.add(jackal)
session.commit()

mira = Operator(name = 'Mira', affiliation = geo)

session.add(mira)
session.commit()

# SDU organization
sdu = Org(name = 'SDU', desc = '''Special Duties Unit. Hong Kong elite
paramilitary special operations unit. ''')

session.add(sdu)
session.commit()

ying = Operator(name = 'Ying', affiliation = sdu)

session.add(ying)
session.commit()

lesion = Operator(name = 'Lesion', affiliation = sdu)

session.add(lesion)
session.commit()

# GROM organization
grom = Org(name = 'GROM', desc = '''Group for Operational Maneuvering
Response. Poland elite counter-terrorism unit. ''')

session.add(grom)
session.commit()

zofia = Operator(name = 'Zofia', affiliation = grom)

session.add(zofia)
session.commit()

ela = Operator(name = 'Ela', affiliation = grom)

session.add(ela)
session.commit()

# 707th SMB
_707thsmb = Org(name = '707th SMB', desc = '''Special Mission Batallion.
Republic of Korea Army Special Forces. ''')

session.add(_707thsmb)
session.commit()

dokkaebi = Operator(name = 'Dokkaebi', affiliation = _707thsmb)

session.add(dokkaebi)
session.commit()

vigil = Operator(name = 'Vigil', affiliation = _707thsmb)

session.add(vigil)
session.commit()

# Weapons
type89 = PrimeWeapon(name = 'Type-89', caliber = '5.56x45mm', sht_damage = 40,
lng_damage = 25, affiliation = sat)

session.add(type89)
session.commit()

supernova = PrimeWeapon(name = 'Benelli SuperNova', caliber = '12 gauge',
sht_damage = 32, lng_damage = 32, affiliation = sat)

session.add(supernova)
session.commit()

mp5sd = PrimeWeapon(name = 'MP5SD', caliber = '9x19mm', sht_damage = 30,
lng_damage = 18, affiliation = sat)

session.add(mp5sd)
session.commit()

m59a01= PrimeWeapon(name = 'M59A01', caliber = '12 gauge', sht_damage = 45,
lng_damage = 45, affiliation = sas)

session.add(m59a01)
session.commit()

l85a2 = PrimeWeapon(name = 'L85A2', caliber = '5.56X49mm', sht_damage = 47,
lng_damage = 29, affiliation = sas)

session.add(l85a2)
session.commit()

ar33 = PrimeWeapon(name = 'AR33', caliber = '5.56x45mm', sht_damage = 41,
lng_damage = 24, affiliation = sas)

session.add(ar33)
session.commit()

g36c = PrimeWeapon(name = 'G36C', caliber = '5.56x45mm', sht_damage = 38,
lng_damage = 26, affiliation = fbi)

session.add(g36c)
session.commit()

r4c = PrimeWeapon(name = 'R4-C', caliber = '5.56x45mm', sht_damage = 39,
lng_damage = 25, affiliation = fbi)

session.add(r4c)
session.commit()

_556xi = PrimeWeapon(name = '556xi', caliber = '5.56x45mm', sht_damage = 46,
lng_damage = 25, affiliation = fbi)

session.add(_556xi)
session.commit()

m1014 = PrimeWeapon(name = 'M1014', caliber = '12 gauge', sht_damage = 32,
lng_damage = 32, affiliation = fbi)

session.add(m1014)
session.commit()

ump45 = PrimeWeapon(name = 'UMP45', caliber = '.45', sht_damage = 38,
lng_damage = 32, affiliation = fbi)

session.add(ump45)
session.commit()

f2 = PrimeWeapon(name = 'F2', caliber = '5.56x45mm', sht_damage = 39,
lng_damage = 21, affiliation = gign)

session.add(f2)
session.commit()

_417 = PrimeWeapon(name = '417', caliber = '7.62x51mm', sht_damage = 69,
lng_damage = 45, affiliation = gign)

session.add(_417)
session.commit()

sgcqb = PrimeWeapon(name = 'SG-CQB', caliber = '12 gauge', sht_damage = 50,
lng_damage = 50, affiliation = gign)

session.add(sgcqb)
session.commit()

mp5 = PrimeWeapon(name = 'MP5', caliber = '9x19mm', sht_damage = 30,
lng_damage = 20, affiliation = gign)

session.add(mp5)
session.commit()

p90 = PrimeWeapon(name = 'P90', caliber = '9x19mm', sht_damage = 22,
lng_damage = 18, affiliation = gign)

session.add(p90)
session.commit()

_6p41 = PrimeWeapon(name = '6P41', caliber = '7.62x54mm', sht_damage = 47,
lng_damage = 25, affiliation = spetznaz)

session.add(_6p41)
session.commit()

ak12 = PrimeWeapon(name = 'AK12', caliber = '5.45x39mm', sht_damage = 44,
lng_damage = 22, affiliation = spetznaz)

session.add(ak12)
session.commit()

ots03 = PrimeWeapon(name = 'OTs-03', caliber = '7.62x54mm', sht_damage = 85,
lng_damage = 65, affiliation = spetznaz)

session.add(ots03)
session.commit()

_9x19vsn = PrimeWeapon(name = '9x19VSN', caliber = '9x19mm', sht_damage = 34,
lng_damage = 20, affiliation = spetznaz)

session.add(_9x19vsn)
session.commit()

sasg12 = PrimeWeapon(name = 'SASG-12', caliber = '12 gauage', sht_damage = 50,
lng_damage = 42, affiliation = spetznaz)

session.add(sasg12)
session.commit()

auga2 = PrimeWeapon(name = 'AUG A2', caliber = '5.56x45mm', sht_damage = 41,
lng_damage = 26, affiliation = gsg9)

session.add(auga2)
session.commit()

_552commando = PrimeWeapon(name = '552 Commando', caliber = '5.56x45mm',
sht_damage = 48, lng_damage = 28, affiliation = gsg9)

session.add(_552commando)
session.commit()

g8a1 = PrimeWeapon(name = 'G8A1', caliber = '7.62x51mm', sht_damage = 37,
lng_damage = 28, affiliation = gsg9)

session.add(g8a1)
session.commit()

m870 = PrimeWeapon(name = 'M870', caliber = '12 gauge', sht_damage = 60,
lng_damage = 60, affiliation = gsg9)

session.add(m870)
session.commit()

_416ccarbine = PrimeWeapon(name = '416-C Carbine', caliber = '5.56x45mm',
sht_damage = 43, lng_damage = 21, affiliation = gsg9)

session.add(_416ccarbine)
session.commit()

mp7 = PrimeWeapon(name = 'MP7', caliber = '4.6x30mm', sht_damage = 32,
lng_damage = 20, affiliation = gsg9)

session.add(mp7)
session.commit()

c8sfw = PrimeWeapon(name = 'C8-SFW', caliber = '5.56x45mm', sht_damage = 40,
lng_damage = 20, affiliation = jtf2)

session.add(c8sfw)
session.commit()

camrs = PrimeWeapon(name = 'CAMRS', caliber = '7.62x51mm', sht_damage = 69,
lng_damage = 38, affiliation = jtf2)

session.add(camrs)
session.commit()

super90 = PrimeWeapon(name = 'Super 90', caliber = '12 gauge', sht_damage = 30,
lng_damage = 30, affiliation = jtf2)

session.add(super90)
session.commit()

_9mmc1 = PrimeWeapon(name = '9mm C1', caliber = '9x19mm', sht_damage = 43,
lng_damage = 27, affiliation = jtf2)

session.add(_9mmc1)
session.commit()

mk17cqb = PrimeWeapon(name = 'Mk17 CQB', caliber = '7.62x51mm', sht_damage = 42,
lng_damage = 26, affiliation = navyseals)

session.add(mk17cqb)
session.commit()

sr25 = PrimeWeapon(name = 'SR-25', caliber = '7.6x51mm', sht_damage = 72,
lng_damage = 43, affiliation = navyseals)

session.add(sr25)
session.commit()

mpx = PrimeWeapon(name = 'MPX', caliber = '9x19mm', sht_damage = 26,
lng_damage = 10, affiliation = navyseals)

session.add(mpx)
session.commit()

spas12 = PrimeWeapon(name = 'SPAS-12', caliber = '12 gauge', sht_damage = 33,
lng_damage = 33, affiliation = navyseals)

session.add(spas12)
session.commit()

para308 = PrimeWeapon(name = 'PARA-308', caliber = '7.62x51mm', sht_damage = 48,
lng_damage = 29, affiliation = bope)

session.add(para308)
session.commit()

m249 = PrimeWeapon(name = 'M249', caliber = '5.56x45mm', sht_damage = 34,
lng_damage = 25, affiliation = bope)

session.add(m249)
session.commit()

m12 = PrimeWeapon(name = 'M12', caliber = '9x19mm', sht_damage = 36,
lng_damage = 28, affiliation = bope)

session.add(m12)
session.commit()

spas15 = PrimeWeapon(name = 'SPAS-15', caliber = '12 gauge', sht_damage = 28,
lng_damage = 28, affiliation = bope)

session.add(spas15)
session.commit()

c7e = PrimeWeapon(name = 'C7E', caliber = '5.56x45mm', sht_damage = 46,
lng_damage = 23, affiliation = geo)

session.add(c7e)
session.commit()

pdw9 = PrimeWeapon(name = 'PDW9', caliber = '9x19mm', sht_damage = 34,
lng_damage = 35, affiliation = geo)

session.add(pdw9)
session.commit()

ita12l = PrimeWeapon(name = 'ITA12L', caliber = '12 gauge', sht_damage = 47,
lng_damage = 47, affiliation = geo)

session.add(ita12l)
session.commit()

vector45acp = PrimeWeapon(name = 'Vector 45 ACP', caliber = '.45',
sht_damage = 21, lng_damage = 15, affiliation = geo)

session.add(vector45acp)
session.commit()

t5smg = PrimeWeapon(name = 'T-5 SMG', caliber = '9x19mm', sht_damage = 30,
lng_damage = 20, affiliation = sdu)

session.add(t5smg)
session.commit()

six12 = PrimeWeapon(name = 'SIX12', caliber = '12 gauge', sht_damage = 35,
lng_damage = 35, affiliation = sdu)

session.add(six12)
session.commit()

six12sd = PrimeWeapon(name = 'SIX12 SD', caliber = '12 gauge', sht_damage = 35,
lng_damage = 35, affiliation = sdu)

session.add(six12sd)
session.commit()

t95lsw = PrimeWeapon(name = 'T-95 LSW', caliber = '5.8x42mm', sht_damage = 34,
lng_damage = 30, affiliation = sdu)

session.add(t95lsw)
session.commit()

lmge = PrimeWeapon(name = 'LMG-E', caliber = '5.56x45mm', sht_damage = 32,
lng_damage = 26, affiliation = grom)

session.add(lmge)
session.commit()

m762 = PrimeWeapon(name = 'M762', caliber = '7.62x39mm', sht_damage = 45,
lng_damage = 23, affiliation = grom)

session.add(m762)
session.commit()

scorpionevo3a1 = PrimeWeapon(name = 'Scorpion Evo 3 A1', caliber = '9x19mm',
sht_damage = 28, lng_damage = 18, affiliation = grom)

session.add(scorpionevo3a1)
session.commit()

fo12 = PrimeWeapon(name = 'FO-12', caliber = '12 gauge', sht_damage = 35,
lng_damage = 24, affiliation = grom)

session.add(fo12)
session.commit()

mk14ebr = PrimeWeapon(name = 'Mk 14 EBR', caliber = '.308', sht_damage = 60,
lng_damage = 51, affiliation = _707thsmb)

session.add(mk14ebr)
session.commit()

k1a = PrimeWeapon(name = 'K1A', caliber = '.223', sht_damage = 36,
lng_damage = 24, affiliation = _707thsmb)

session.add(k1a)
session.commit()

bosg122 = PrimeWeapon(name = 'BOSG.12.2', caliber = '12 gauge slug',
sht_damage = 125, lng_damage = 80, affiliation = _707thsmb)

session.add(bosg122)
session.commit()

p229 = SecWeapon(name = 'P229', caliber = '.357', sht_damage = 50,
lng_damage = 28, affiliation = sat)

session.add(p229)
session.commit()

bearing9 = SecWeapon(name = 'Bearing 9', caliber = '9x19mm', sht_damage = 33,
lng_damage = 22, affiliation = sat)

session.add(bearing9)
session.commit()

p226mk25 = SecWeapon(name = 'P226 Mk 25', caliber = '9x19mm', sht_damage = 50,
lng_damage = 30, affiliation = sas)

session.add(p226mk25)
session.commit()

smg11 = SecWeapon(name = 'SMG-11', caliber = '.380', sht_damage = 33,
lng_damage = 22, affiliation = sas)

session.add(smg11)
session.commit()

m45meusoc = SecWeapon(name = 'M45 MEUSOC', caliber = '.45', sht_damage = 58,
lng_damage = 33, affiliation = fbi)

session.add(m45meusoc)
session.commit()

_57usg = SecWeapon(name = '5.7 USG', caliber = '5.7x28mm', sht_damage = 42,
lng_damage = 25, affiliation = fbi)

session.add(_57usg)
session.commit()

p9 = SecWeapon(name = 'P9', caliber = '9x19mm', sht_damage = 45,
lng_damage = 27, affiliation = gign)

session.add(p9)
session.commit()

lfp586 = SecWeapon(name = 'LFP586', caliber = '.357', sht_damage = 78,
lng_damage = 34, affiliation = gign)

session.add(lfp586)
session.commit()

pmm = SecWeapon(name = 'PMM', caliber = '9x18mm', sht_damage = 63,
lng_damage = 29, affiliation = spetznaz)

session.add(pmm)
session.commit()

gsh18 = SecWeapon(name = 'GSh-18', caliber = '9x19mm', sht_damage = 33,
lng_damage = 24, affiliation = spetznaz)

session.add(gsh18)
session.commit()


p12 = SecWeapon(name = 'P12', caliber = '.45', sht_damage = 44,
lng_damage = 24, affiliation = gsg9)

session.add(p12)
session.commit()

mk19mm = SecWeapon(name = 'Mk1 9mm', caliber = '9x19mm', sht_damage = 48,
lng_damage = 27, affiliation = jtf2)

session.add(mk19mm)
session.commit()

d50 = SecWeapon(name = 'D-50', caliber = '.50', sht_damage = 71,
lng_damage = 35, affiliation = navyseals)

session.add(d50)
session.commit()

lusion = SecWeapon(name = 'Lusion', caliber = '9x19mm', sht_damage = 99,
lng_damage = 20, affiliation = bope)

session.add(lusion)
session.commit()

usp40 = SecWeapon(name = 'USP40', caliber = '.40', sht_damage = 48,
lng_damage = 25, affiliation = geo)

session.add(usp40)
session.commit()

ita12s = SecWeapon(name = 'ITA12S', caliber = '12 gauge', sht_damage = 66,
lng_damage = 66, affiliation = geo)

session.add(ita12s)
session.commit()

q929 = SecWeapon(name = 'Q-929', caliber = '9x19mm', sht_damage = 60,
lng_damage = 30, affiliation = sdu)

session.add(q929)
session.commit()

rg15 = SecWeapon(name = 'RG15', caliber = '9x19mm', sht_damage = 48,
lng_damage = 27, affiliation = grom)

session.add(rg15)
session.commit()

c75auto = SecWeapon(name = 'C75 Auto', caliber = '9x19mm', sht_damage = 35,
lng_damage = 23, affiliation = _707thsmb)

session.add(c75auto)
session.commit()

smg12 = SecWeapon(name = 'SMG-12', caliber = '9x19mm', sht_damage = 27,
lng_damage = 19, affiliation = _707thsmb)

session.add(smg12)
session.commit()
