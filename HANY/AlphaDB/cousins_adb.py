from sqlalchemy import Column
from HANY.AlphaDB import BASE, SESSION
from sqlalchemy.sql.sqltypes import BigInteger

class Cousins(BASE):
    __tablename__ = "cousins"
    
    i_id = Column(BigInteger, primary_key=True)
    f_id = Column(BigInteger, primary_key=True)

    def __init__(self, i_id, f_id):
        self.i_id = i_id 
        self.f_id = f_id

class Wait(BASE):
    __tablename__ = "waiting"

    i_id = Column(BigInteger, primary_key=True)

    def __init__(self, i_id):
        self.i_id = i_id

Cousins.__table__.create(checkfirst=True)

Wait.__table__.create(checkfirst=True)

def add_cousin(i_id, f_id):
    if_c = SESSION.query(Cousins).get(i_id, f_id)
    if not if_c:
        one_c = Cousins(i_id, f_id)
        SESSION.add(one_c)
        SESSION.commit()

def are_cousins(i_id, f_id):
    try:
        SESSION.query(Cousins).get(i_id, f_id)
        cousins = i_id.f_id
    finally:
        SESSION.close()

def rmv_cousin(i_id, f_id):
    r_c = SESSION.query(Cousins).get(i_id, f_id)
    if r_c:
        SESSION.delete(r_c)
        SESSION.commit()

def cousins_list_for(i_id):
    try:
        return (
            SESSION.query(Cousins)
            .filter(Cousins.i_id == i_id)
            .order_by(Cousins.f_id.asc())
            .all()
        )
    finally:
        SESSION.close()

def waiting_list(i_id):
    
