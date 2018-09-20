from flask_restful import Resource, request
from models.hello import HelloModel


class HelloResource(Resource):

    def get(self):
        all = HelloModel.find_all() or []
        all_in_json = [hello.to_json() for hello in all]
        return {"allHellos": all_in_json}, 200

    def post(self):
        data = request.get_json()
        hello = HelloModel(data["hello"])
        hello.save_to_db()
        return {'message': 'hello aangemaakt'}, 201


class HelloWithParamsResource(Resource):

    def get(self, name):
        return "hello " + name