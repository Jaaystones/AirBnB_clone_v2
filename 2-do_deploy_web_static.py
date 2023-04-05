#!/usr/bin/python3
from fabric.api import run, local, env, put
from datetime import datetime
import os
from fabric.context_managers import cd

env.hosts = ['52.87.216.6', '54.175.46.5']
env.user = 'ubuntu'
env.key_filename = '/root/.ssh/school'


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    try:
        if not os.path.exists(archive_path):
            return False
        # Upload the archive to the server
        put(archive_path, "/tmp/")

        # Create the directory where the files will be extracted
        web_static = archive_path.split("/")[-1]
        web_static_path = web_static.split(".")[0]
        run("sudo mkdir -p /data/web_static/\
            releases/web_static_{}/".format(web_static_path))
        # Extract the archive into the directory
        run("sudo tar -xzf /tmp/web_static_{}.tgz -C /data/web_static\
            /releases/web_static_{}/".format(web_static, web_static_path))
        # Delete the archive from the server
        run("sudo rm /tmp/web_static_{}.tgz".format(web_static))

        # Move the contents of the web_static directory up one level
        run("sudo mv /data/web_static/releases/{}/web_static/*\
            /data/web_static\
            /releases/{}/".format(web_static_path, web_static_path))
        # Remove the now empty web_static directory
        run("sudo rm -rf /data/web_static/releases/{} \
            /web_static_{}/web_static".format(web_static_path))
        # Delete the symbolic link /data/web_static/current
        run("sudo rm -rf /data/web_static/current")
        # Create a symbolic link from /data/web_static/current to new code
        run("sudo ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(web_static_path))
        return True
    return False
