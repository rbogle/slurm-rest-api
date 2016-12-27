from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import json
from datetime import datetime

class Assoc(Base):
    __tablename__ = 'nebula_assoc_table'
    id_assoc = Column(Integer, primary_key=True)
    user = Column(String)
    acct = Column(String)
    partition = Column(String)

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        me = dict()
        me['id_assoc']=int(self.id_assoc)
        me['user']= self.user
        me['acct']= self.acct
        me['partition']= self.partition
        return me

class Job(Base):
    __tablename__ = 'nebula_job_table'
    id_job =  Column(Integer, primary_key=True)
    id_user = Column(Integer)
    id_assoc = Column(Integer)
    job_name = Column(String)
    cpus_req = Column(Integer)
    mem_req = Column(Integer)
    account = Column(String)
    nodelist = Column(String)
    partition = Column(String)
    nodes_alloc = Column(Integer)
    timelimit = Column(Integer)
    time_submit = Column(Integer)
    time_start  = Column(Integer)
    time_end  = Column(Integer)
    priority  = Column(Integer)

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        me = dict()
        me['id_job']=int(self.id_job)
        me['id_user']= int(self.id_user)
        me['id_assoc']= int(self.id_assoc)
        me['job_name']= self.job_name
        me['cpus_req']= int(self.cpus_req)
        me['mem_req']= int(self.mem_req)
        me['account']= self.account
        me['nodelist']= self.nodelist
        me['partition']= self.partition
        me['nodes_alloc']= int(self.nodes_alloc)
        me['timelimit']=int(self.timelimit)
        me['time_submit']=datetime.fromtimestamp(self.time_submit).ctime()
        me['time_start']=datetime.fromtimestamp(self.time_start).ctime()
        me['time_end']=datetime.fromtimestamp(self.time_end).ctime()
        me['priority']=int(self.priority)
        return me
