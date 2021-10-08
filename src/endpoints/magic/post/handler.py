from secrets import token_urlsafe

from src.errors import handleErr, UserNotFoundError

global db
global send_mail

def makeMagicLink(email, isTestMode = False):
    try:
        token = token_urlsafe(8)
        link = f"https://randomuser.me/magic/linus.bolls@code.berlin/{token}"

        setTokenQuery = { "$set": { "token": hash(token) }}

        if not isTestMode:
            send_mail([ email ], "Your Magic Login Link", link)

        result = db.users.update_one({ "email": email }, setTokenQuery)

        if (result.modified_count == 0):
            raise UserNotFoundError()

        return [ token if isTestMode else True, None ]

    except Exception as err:
        return [ None, handleErr(err) ]