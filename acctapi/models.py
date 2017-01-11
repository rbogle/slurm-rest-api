from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
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
    state = Column(Integer)

    def __repr__(self):
        return str(self.to_dict())

    def conv_timestamp(self,time):
        rval =""
        if time>0:
            rval = datetime.fromtimestamp(time).ctime()
        return rval

    def conv_timelimit(self, minutes):
        hours, mins = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        return "%d:%d:%d" %(days,hours,mins)

    def to_dict(self):
        states = [
          'JOB_PENDING',
          'JOB_RUNNING',
          'JOB_SUSPENDED',
          'JOB_COMPLETE',
          'JOB_CANCELLED',
          'JOB_FAILED',
          'JOB_TIMEOUT',
          'JOB_NODE_FAIL',
          'JOB_PREEMPTED',
          'JOB_BOOT_FAIL',
          'JOB_DEADLINE'
        ]
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
        me['timelimit']=self.conv_timelimit(int(self.timelimit))
        me['time_submit']=self.conv_timestamp(int(self.time_submit))
        me['time_start']=self.conv_timestamp(int(self.time_start))
        me['time_end']=self.conv_timestamp(int(self.time_end))
        me['priority']=int(self.priority)
        self.state= max(min(10, int(self.state)),0)
        me['state'] = states[self.state]
        return me
