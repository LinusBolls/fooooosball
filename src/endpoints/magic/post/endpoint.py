from flask_restful import Resource

from . import handler

def init(db, api, send_mail):

    handler.db = db
    handler.send_mail = send_mail

    class SendMagicLink(Resource):
        def get(self, userId):

            data, err = handler.makeMagicLink(userId)

            if err:
                return { "ok": 0, "err": err.msg }, err.status
            return { "ok": 1 }, 200

    api.add_resource(SendMagicLink, "/user/<string:userId>")