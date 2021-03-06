from YashviDB import db

cousinsdb = db.cousinsdb

waitdb = db.waitdb

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

async def get_cousin_ids(i_id: int) -> list:
    cousins = cousinsdb.find({"i_id": i_id}, {"f_id": {"$gt": 0}})
    if not cousins:
        return []
    COUSINS = []
    for cousin in await cousins.to_list(length=1000000000):
        COUSINS.append(cousin)
    return COUSINS

async def add_to_waiting(i_id: int, f_id: int):
    waiting = await waitdb.find_one({"i_id": i_id}, {"f_id": f_id})
    if not waiting:
        await waitdb.insert_one({"i_id": i_id}, {"f_id": f_id})

async def rmv_from_waiting(i_id: int, f_id: int):
    waiting = await waitdb.find_one({"i_id": i_id}, {"f_id": f_id})
    if waiting:
        await waitdb.delete_one({"i_id": i_id}, {"f_id": f_id})

async def is_waiting(i_id: int, f_id: int) -> bool:
    waiting = await waitdb.find_one({"i_id": i_id}, {"f_id": f_id})
    if waiting:
        return True
    else:
        return False
    
