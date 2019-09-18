from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
import sqlalchemy 

db_connect = create_engine('sqlite:///test.db', echo=True)

app = Flask(__name__)
api = Api(app)

class AllPhilosophers(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from Philosopher;")
        return {'philosophers': [i[0] for i in query.cursor.fetchall()]}

class AllQuotes(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select Quote, Philosopher, Source from Quote;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Philosopher(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from Philosopher order by random() limit 1;")
        return {'data': [dict(zip(tuple  (query.keys()), i)) for i in query.cursor]}

class Quote(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select Quote, Philosopher, Source from Quote order by random() limit 1;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

api.add_resource(AllPhilosophers, '/allPhilosophers')
api.add_resource(AllQuotes, '/allQuotes')
api.add_resource(Philosopher, '/philosopher')
api.add_resource(Quote, '/quote')

if __name__ == '__main__':
     app.run(port='5002')
     
