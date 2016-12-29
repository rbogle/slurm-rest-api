from flask import Flask
from flask_restful import Api
from acctapi import db_session, init_db, JobHistoryApi, UserAssocApi
from slurmapi import Slurm_Queue, Slurm_Statistics, Slurm_Nodes, Slurm_Partitions
import config

app = Flask(__name__)
app.debug = config.DEBUG

api = Api(app)

if config.USE_ACCT_DB:
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    init_db()

    api.add_resource(JobHistoryApi, '/', '/jobhistory')
    api.add_resource(UserAssocApi, '/users')

api.add_resource(Slurm_Queue, '/queue')
api.add_resource(Slurm_Nodes, '/nodes')
api.add_resource(Slurm_Partitions, '/partitions')
api.add_resource(Slurm_Statistics, '/stats')

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)
