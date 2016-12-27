# taken from http://flask.pocoo.org/docs/0.11/patterns/sqlalchemy/#declarative

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import *

engine = create_engine('mysql://%s:%s@%s/%s' %(DB_USER,DB_PASS,DB_HOST,DB_NAME))
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from models import Job,Assoc
    Base.metadata.create_all(bind=engine)
