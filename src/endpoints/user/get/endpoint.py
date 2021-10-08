from flask_restful import Resource

from . import handler

def init(db, api):

    handler.db = db

    class GetUser(Resource):
        def get(self, userId):

            data, err = handler.getUser(userId)

            if err:
                return { "ok": 0, "err": err.msg }, err.status
            return { "ok": 1, "data": data }, 200

    api.add_resource(GetUser, "/user/<string:userId>")