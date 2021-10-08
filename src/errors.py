class UserNotFoundError(Exception):
    status = 404
    msg = "User could not be found"

class InvalidMagicLinkError(Exception):
    status = 401
    msg = "Magic data could not be validated"

def handleErr(err):
    e = type(err).__name__

    if hasattr(err, "status") and hasattr(err, "msg"):
        return err

    elif e == "DuplicateKeyError":
        # tried to sign up with email that is already registered
        err.status = 400
        err.msg = "That ressource already exists"
    elif e == "WriteError":
        # tried to insert invalid document into schema
        err.status = 400
        err.msg = "Malformed query"
    else:
        print(f"Encountered unexpected {e}:")
        print(err)
        err.status = 500
        err.msg = "An unexpected error occured"

    return err