#!/usr/bin/python3
from fabric.api import run, local, env, put
from datetime import datetime
import os
from fabric.context_managers import cd

env.hosts = ['52.87.216.6', '54.175.46.5']
env.user = 'ubuntu'
env.key_filename = '/root/.ssh/school'

def do_deploy(archive_path):
       "def do_deploy(archive_path):
        """Deploy web files to server
        """
        try:
                if not (path.exists(archive_path)):
                        return False

                # upload archive
                put(archive_path, '/tmp/')

                # create target dir
                web_static = archive_path.split("/")[-1]
                web_static_path = web_static.split(".")[0]
                run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(web_static_path))

                # uncompress archive and delete .tgz
                run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                    .format(web_static, web_static_path))

                # remove archive
                run('sudo rm /tmp/web_static_{}.tgz'.format(web_static))

                # move contents into host web_static
                run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(web_static_path, web_static_path))

                # remove extraneous web_static dir
                run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
                    .format(web_static_path))

                # delete pre-existing sym link
                run('sudo rm -rf /data/web_static/current')

                # re-establish symbolic link
                run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(web_static_path))
        except:
                return False

        # return True on success
        return True
