import datetime

from src.errors import handleErr

global db

def insertUser(user):
    try:
        user["created"] = datetime.datetime.now().isoformat()
        user["matches"] = []

        result = db.users.insert_one(user)
        return [ result, None ]

    except Exception as err:
         return [ None, handleErr(err) ]