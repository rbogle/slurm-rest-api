from flask import Flask
from flask_restful import Resource, Api, reqparse
from models import Job, User
from database import db_session, init_db
import json

app = Flask(__name__)
api = Api(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

init_db()

class UserApi(Resource):
    def get(self):
        userlist = User.query.all()
        ul = list()
        for user in userlist:
            ul.append(user.to_dict())
        return ul

class JobApi(Resource):
    def get(self):
        parser =reqparse.RequestParser()
        parser.add_argument('limit', type=int, default=10)
        parser.add_argument('offset', type=int, default=0)
        parser.add_argument('user', type=int, default=None)
        args = parser.parse_args()
        if args['user']:
            filter = args['user']
            userlist = User.query.filter(User.id_assoc==filter).all()
            joblist = Job.query.filter(Job.id_assoc==filter).limit(args['limit']).offset(args['offset']).all()
        else:
            userlist = User.query.all()
            joblist = Job.query.limit(args['limit']).offset(args['offset']).all()
        users = dict()
        for user in userlist:
            users[user.id_assoc]=user.user
        rlist = list()
        for job in joblist:
            jd = job.to_dict()
            jd['user_name'] = users.get(jd['id_assoc'], "")
            rlist.append(jd)
        return rlist

api.add_resource(JobApi, '/', '/job')
api.add_resource(UserApi, '/user')

if __name__ == '__main__':
    app.run(debug=True)
