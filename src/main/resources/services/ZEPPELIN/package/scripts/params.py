#!/usr/bin/env python
from resource_management import *
from resource_management.libraries.script.script import Script
import sys, os
from resource_management.libraries.functions.default import default

# server configurations
config = Script.get_config()

zeppelin_dirname = 'zeppelin'

# params from zeppelin-ambari-config
install_dir = config['configurations']['zeppelin-ambari-config']['zeppelin.install.dir']
executor_mem = config['configurations']['zeppelin-ambari-config']['zeppelin.executor.mem']
zeppelin_tarball_url = str(config['configurations']['zeppelin-ambari-config']['zeppelin.tarball.url'])
zeppelin_notebooks_url = str(config['configurations']['zeppelin-ambari-config']['zeppelin.notebooks.url'])
temp_file = config['configurations']['zeppelin-ambari-config']['zeppelin.temp.file']

# params from zeppelin-env
zeppelin_user = config['configurations']['zeppelin-env']['zeppelin_user']
zeppelin_group = config['configurations']['zeppelin-env']['zeppelin_group']
zeppelin_log_dir = config['configurations']['zeppelin-env']['zeppelin_log_dir']
zeppelin_pid_dir = config['configurations']['zeppelin-env']['zeppelin_pid_dir']
zeppelin_log_file = os.path.join(zeppelin_log_dir, 'zeppelin-setup.log')
zeppelin_hdfs_user_dir = format("/user/{zeppelin_user}")
  
zeppelin_dir = os.path.join(*[install_dir, zeppelin_dirname]) 
conf_dir = os.path.join(*[install_dir, zeppelin_dirname, 'conf'])
notebook_dir = os.path.join(*[install_dir, zeppelin_dirname, 'notebook'])

# zeppelin-env.sh
zeppelin_env_content = config['configurations']['zeppelin-env']['content']

# detect HS2 details and java home
master_configs = config['clusterHostInfo']

java64_home = config['hostLevelParams']['java_home']
ambari_host = str(master_configs['ambari_server_host'][0])

