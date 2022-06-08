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
    if not is_male:
        adder = Males(i_id)
        SESSION.add(adder)
        SESSION.commit()
