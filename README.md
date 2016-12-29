# Slurm RestAPI

This is a flask based rest interface to slurm.
There are two sub-packages which implement interfaces to different parts of the slurm manager
  * acctapi - interacts with the accounting database slurmdb to get job history and user associations
  * slurmapi - interacts with the pyslurm package to get queue, node, partition, and stat info

Endpoints are
```
 /users - can be filtered on user
 /history - can be filtered on offset,limit,jobid,user,partition,jobname,associd
 /queue
 /partitions
 /nodes
 /stats
 ```

### Install / Setup
Files are included to enable running the flask service under NGINX via uwsgi
 * slurmrest.ini - uwsgi ini file
 * etc/slurmrest.service - systemd service descriptor for running this service under uwsgi
 * etc/nginx_slurmrest.conf - example nginx config fragment for proxying to the uwsgi service.

To install, clone this repo somewhere like: `/opt`
```
git clone urlforgitrepo /opt
```
Then setup a virtualenv or conda env with the following:
```
conda create -p /opt/conda/envs/slurm_rest_api python=2.7
source activate /opt/conda/envs/slurm_rest_api
conda install flask
conda install -c conda-forge flask-restful flask-sqlalchemy
pip install mysql-python
pip install uwsgi
```
Make sure the uwsgi files and nginx file all point to the location of your git clone and the python environment.
Make sure the location of the uwsgi socket file is writable by nginx or the user that starts uwsgi

leave slurmrest.ini in repo dir
copy slurmrest.service to /usr/lib/systemd/systemd
include nginx_slurmrest.conf fragment in nginx config.

then:
```
sudo systemctl enable slurmrest.service
sudo systemctl start slurmrest.service

sudo systemctl restart nginx

```
