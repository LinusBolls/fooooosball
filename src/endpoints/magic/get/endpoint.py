from flask_restful import Resource

from . import handler

def init(db, api, secret):

    handler.db = db
    handler.secret = secret

    class GetMagicLink(Resource):
        def get(self, userId, magicId):

            data, err = handler.tokenIfMagic(userId, magicId)

            if err:
                return { "ok": 0, "err": err.msg }, err.status
            return { "ok": 1 }, 200, { "set-cookie": data }

    api.add_resource(GetMagicLink, "/magic/<string:userId>/<string:magicId>")