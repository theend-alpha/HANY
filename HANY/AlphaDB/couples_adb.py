from sqlalchemy import Column
from HANY.AlphaDB import BASE, SESSION
from sqlalchemy.sql.sqltypes import BigInteger

COUPLES = []

class Couples(BASE):
    __tablename__ = "couples"
    
    i_id = Column(BigInteger, primary_key=True)
    f_id = Column(BigInteger, primary_key=True)

    def __init__(self, i_id, f_id):
        self.i_id = i_id 
        self.f_id = f_id

Couples.__table__.create(checkfirst=True)

def add_couple(i_id, f_id):
    is_selected = SESSION.query(Couples).get(i_id, f_id)
    if not is_selected:
        adder = Couples(i_id, f_id)
        SESSION.add(adder)
        SESSION.commit()

def c_is_selected(i_id, f_id):
    global COUPLES
    selected = SESSION.query(Couples).get(i_id, f_id)
    if selected:
        COUPLES.append(i_id)
        COUPLES.append(f_id)
    else: 
        return

def reset_couple(i_id, f_id):
    couple = SESSION.query(Couples).get(i_id, f_id)
    if couple:
        SESSION.delete(couple)
        SESSION.commit()
    else:
        SESSION.close()
