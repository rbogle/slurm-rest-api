from flask import Flask
from flask_restful import Api
from accounting import db_session, init_db, JobHistoryApi, UserAssocApi

app = Flask(__name__)
api = Api(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

init_db()

api.add_resource(JobHistoryApi, '/', '/jobhistory')
api.add_resource(UserAssocApi, '/users')

if __name__ == '__main__':
    app.run(debug=True)
