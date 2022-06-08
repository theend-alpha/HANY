from sqlalchemy import Column
from HANY.AlphaDB import BASE, SESSION
from sqlalchemy.sql.sqltypes import BigInteger

class Males(BASE):
    __tablename__ = "males"

    i_id = Column(BigInteger, primary_key=True)

    def __init__(self, i_id):
        self.i_id = i_id
