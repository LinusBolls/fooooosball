from flask import Flask
from flask_restful import Api

from src.init import config, db, send_mail, secret

app = Flask(__name__)
api = Api(app)

# ===== Registering Endpoints ===== #

import endpoints.user.get.endpoint as getUser
getUser.init(db, api)

import endpoints.user.signup.post.endpoint as signupUser
signupUser.init(db, api)

import endpoints.magic.get.endpoint as getMagic
getMagic.init(db, api, secret)

import endpoints.magic.post.endpoint as postMagic
postMagic.init(db, api, send_mail)

# import endpoints.match.get.endpoint as getMatch
# getMatch.init(db, api)

# import endpoints.match.post.endpoint as postMatch
# postMatch.init(db, api)

if __name__ == "__main__":
    app.run(host = config["server"]["hostname"], port = config["server"]["port"], debug = config["isTesting"])