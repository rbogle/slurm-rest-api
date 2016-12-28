from flask_restful import Resource, reqparse
import pyslurm

class Slurm_Queue(Resource):
    def get(self):
        j = pyslurm.job()
        data = j.get()
        return data

class Slurm_Statistics(Resource):
    def get(self):
        s = pyslurm.statistics()
        data = s.get()
        return data

class Slurm_Nodes(Resource):
    def get(self):
        n = pyslurm.node()
        data = n.get()
        return data

class Slurm_Partitions(Resource):
    def get(self):
        p = pyslurm.partition()
        data = p.get()
        return data
