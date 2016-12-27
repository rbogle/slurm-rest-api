from flask_restful import Resource, Api, reqparse
from models import Job, Assoc


class UserAssocApi(Resource):
    def get(self):
        parser =reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()
        if args['name']:
            userlist = Assoc.query.filter(Assoc.user == args['name']).all()
        else:
            userlist = Assoc.query.filter(Assoc.user != "").all()
        ul = list()
        for user in userlist:
            ul.append(user.to_dict())
        return ul

class JobHistoryApi(Resource):
    def get(self):
        parser =reqparse.RequestParser()
        parser.add_argument('limit', type=int, default=10)
        parser.add_argument('offset', type=int, default=0)
        parser.add_argument('user')
        parser.add_argument('assoc', type=int, default=None)
        parser.add_argument('startbefore')
        parser.add_argument('startafter')
        parser.add_argument('endafter')
        parser.add_argument('endbefore')
        parser.add_argument('jobname')
        parser.add_argument('partition')
        parser.add_argument('jobid', type=int)
        args = parser.parse_args()
        criterion = list()

        if args['user']:
            userlist = Assoc.query.filter(Assoc.user==args['user']).all()
            id_list = list()
            for assoc in userlist:
                id_list.append(assoc.id_assoc)
            criterion.append(Job.id_assoc.in_(id_list))
            #joblist = Job.query.filter(Job.id_assoc.in_(id_list)).limit(args['limit']).offset(args['offset']).all()
        if args['assoc']:
            criterion.append(Job.id_assoc==args['assoc'])
            #joblist = Job.query.filter(Job.id_assoc== args['assoc']).imit(args['limit']).offset(args['offset']).all()
        if args['jobname']:
            criterion.append(Job.job_name==args['jobname'])
        if args['jobid']:
            criterion.append(Job.id_job==args['jobid'])
        if args['partition']:
            criterion.append(Job.partition==args['partition'])

        userlist = Assoc.query.all()
        joblist = Job.query.filter(*criterion).limit(args['limit']).offset(args['offset']).all()

        users = dict()
        for user in userlist:
            users[user.id_assoc]=user.user
        rlist = list()
        for job in joblist:
            jd = job.to_dict()
            jd['user_name'] = users.get(jd['id_assoc'], "")
            rlist.append(jd)
        return rlist
