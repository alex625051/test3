from flask import request
from flask_restful import Resource
from resources.get_gravatar import get_gravatar


class gravatars(Resource):
    def get(self):
        query = request.args.get('query',"no mail")
        result = get_gravatar(query)

        return {"result": result}