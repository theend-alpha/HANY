from sqlalchemy import Column
from HANY.AlphaDB import BASE, SESSION
from sqlalchemy.sql.sqltypes import BigInteger
import threading

MALES = []

FEMALES = []

class Males(BASE):
    __tablename__ = "males"

    i_id = Column(BigInteger, primary_key=True)
   
    def __init__(self, i_id):
        self.i_id = i_id
       

class Females(BASE):
    __tablename__ = "females"

    i_id = Column(BigInteger, primary_key=True)

    def __init__(self, i_id):
        self.i_id = i_id

Males.__table__.create(checkfirst=True)

Females.__table__.create(checkfirst=True)

MALE_IL = threading.RLock()

FEMALE_IL = threading.RLock()

def add_male(i_id):
    with MALE_IL:
        adder = Males(i_id)
        SESSION.add(adder)
        SESSION.commit()

def add_female(i_id):
    with FEMALE_IL:
        adder = Females(i_id)
        SESSION.add(adder)
        SESSION.commit()

def id_is_male(i_id):
    global MALES
    male = SESSION.query(Males).get(i_id)
    if male:
        MALES.append(i_id)
    else:
        return

def id_is_female(i_id):
    global FEMALES
    female = SESSION.query(Females).get(i_id)
    if female:
        FEMALES.append(i_id)
    else:
        return 

def get_males():
    try:
        return SESSION.query(Males).count()
    finally:
        SESSION.close()
def get_females():
    try:
        return SESSION.query(Females).count()
    finally:
        SESSION.close()
def rmv_male(i_id):
    with MALE_IL:
        is_male = SESSION.query(Males).get(i_id)
        if is_male:
            SESSION.delete(is_male)
            SESSION.commit()
        else:
            SESSION.close()

def rmv_female(i_id):
    with FEMALE_IL:
        is_female = SESSION.query(Females).get(i_id)
        if is_female:
            SESSION.delete(is_female)
            SESSION.commit()
        else:
            SESSION.close()
