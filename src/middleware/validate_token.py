import jwt

from src.errors import handleErr

global token

def validateToken(token):
    try:
        return [ jwt.decode(token, secret, algorithms = ["HS256"]), None ]

    except Exception as err:
        return [ None, handleErr(err) ]