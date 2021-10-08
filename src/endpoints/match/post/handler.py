import datetime

from src.errors import handleErr, UserNotFoundError

global db

def insertMatch(match):
    try:
        match["created"] = datetime.datetime.now().isoformat()

        for team in match["teams"]:
            for member in team["members"]:
                result = db.users.find_one({ "email": member["id"] })
                if result is None:
                    raise UserNotFoundError()

        result = db.matches.insert_one(match)
        return [ result, None ]

    except Exception as err:
        return [ None, handleErr(err) ]