from src.errors import handleErr, UserNotFoundError

global db

def getUser(userId):
    try:
        result = db.users.find_one({ "email": userId })
        if result is None:
            raise UserNotFoundError()

    except Exception as err:
         return [ None, handleErr(err) ]