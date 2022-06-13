from YashviDB import db

cousinsdb = db.cousinsdb


async def are_cousins(i_id: int, f_id: int) -> bool:
    cousins = await cousinsdb.find_one({"i_id": i_id}, {"f_id": f_id})
    if cousins:
        return True
    else:
        return False

async def add_cousin(i_id: int, f_id: int):
    cousins = await cousinsdb.find_one({"i_id": i_id}, {"f_id": f_id})
    if not cousins:
        await cousinsdb.insert_one({"i_id": i_id}, {"f_id": f_id})

async def rmv_cousin(i_id: int, f_id: int):
    cousins = await cousinsdb.find_one({"i_id": i_id}, {"f_id": f_id})
    if cousins:
        await cousinsdb.delete_one({"i_id": i_id}, {"f_id": f_id})

async def get_cousins(i_id: int):
    found = await cousinsdb.find_one({"i_id": i_id})
