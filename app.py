from flask import Flask
from flask_restful import Api
from controllers.helloResource import HelloResource, HelloWithParamsResource


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # 'mysql://username:password@ip:port/databasename'
api = Api(app)


api.add_resource(HelloResource, '/api/hello')
api.add_resource(HelloWithParamsResource, '/api/hello/<string:name>')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)