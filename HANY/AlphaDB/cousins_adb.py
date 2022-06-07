from sqlalchemy import Column, Integer
from HANY.AlphaDB import BASE, SESSION

class Cousins(BASE):
    __tablename__ = "cousins"
    
    i_id = Column(BigInteger, primary_key=True)
    f_id = Column(BigInteger, primary_key=True)

Cousins.__table__.create(checkfirst=True)



async def add_cousin(i_id, f_id):
    if_c = SESSION.query(Cousins).get(i_id, f_id)
    if not if_c:
        one_c = Cousins(i_id, f_id)
        two_c = Cousins(f_id, i_id)
        SESSION.add(one_c)
        SESSION.add(two_c)
        SESSION.commit()

async def are_cousins(i_id, f_id):
    try:
        SESSION.query(Cousins).get(i_id, f_id)
    finally:
        SESSION.close()

async def rmv_cousin(i_id, f_id):
    r_c = SESSION.query(Cousins).get(i_id, f_id)
    omfoo = SESSION.query(Cousins).get(f_id, i_id)
    if r_c and omfoo:
        SESSION.delete(r_c)
        SESSION.delete(omfoo)
        SESSION.commit()
    
