import jwt

from src.errors import handleErr, InvalidMagicLinkError

global db
global secret

def doMagic(email, token, doInvalidate = True):
    try:
        searchQuery =  {
            "$and": [
                {
                    "email": email,
                    "token": hash(token)
                },
                {
                    "$nor": [ { "token": "" } ]
                }
            ]
        }
        invalidateQuery = { "$set": { "token": "" }}

        if doInvalidate:
            result = db.users.update_one(searchQuery, invalidateQuery)
            if (result.modified_count == 0):
                raise InvalidMagicLinkError()
        else:
            result = db.users.find_one(searchQuery)
            if result is None:
                raise InvalidMagicLinkError()

        return [ True, None ]

    except Exception as err:
        return [ None, handleErr(err) ]

def tokenIfMagic(email, token):
    data0, err0 = doMagic(email, token)
    if data0:
        token = jwt.encode(payload = { "email": email }, key = secret, algorithm = "HS256")
        return [ token, None ] 
    else: 
        return [ None, handleErr(err0) ]