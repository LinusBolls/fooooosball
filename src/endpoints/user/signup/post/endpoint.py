import json

from flask import request
from flask_restful import Resource

from . import handler

def init(db, api):

    handler.db = db

    class PutSignUp(Resource):
        def put(self):

            user = json.loads(request.form["user"])
            data, err = handler.insertUser(user)

            if err:
                return { "ok": 0, "err": err.msg }, err.status
            return { "ok": 1 }, 201

    api.add_resource(PutSignUp, "/user/signup/")