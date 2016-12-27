from flask import Flask
from flask_restful import Api
from database import db_session, init_db
from resources import JobHistoryApi, UserAssocApi

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
