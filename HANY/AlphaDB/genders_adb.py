from sqlalchemy import Column
from HANY.AlphaDB import BASE, SESSION
from sqlalchemy.sql.sqltypes import BigInteger

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


async def add_male(i_id):
    is_male = SESSION.query(Males).get(i_id)
    is_female = SESSION.query(Females).get(i_id)
    if is_female:
        SESSION.delete(is_female)
    if not is_male:
        adder = Males(i_id)
        SESSION.add(adder)
        SESSION.commit()

async def add_female(i_id):
    is_female = SESSION.query(Females).get(i_id)
    is_male = SESSION.query(Males).get(i_id)
    if is_male:
        SESSION.delete(is_male)
    if not is_female:
        adder = Females(i_id)
        SESSION.add(adder)
        SESSION.commit()

async def get_males():
    try:
        SESSION.query(Males).count()
    finally:
        SESSION.close()

async def get_females():
    try:
        SESSION.query(Females).count()
    finally:
        SESSION.close()
