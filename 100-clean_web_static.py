#!/usr/bin/python3
from fabric.api import run, local, put, env
import datetime
import os


def do_pack():
    now = datetime.datetime.now()
    date = (str(now.year) + str(now.month) + str(now.day)
            + str(now.hour) + str(now.minute) + str(now.second))
    try:
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf versions/web_static_{}.tgz ./web_static".format(date))
        return "./versions/web_static_{}.tgz".format(date)
    return None


env.hosts = ['52.87.216.6', '54.175.46.5']


def do_deploy(archive_path):
    if os.path.exists(archive_path) is False:
        return False
    try:
        upload = put(archive_path, "/tmp/")
        static = archive_path[11:-4]
        static_path = "/data/web_static/releases/" + static
        run("sudo mkdir {}".format(static_path))
        run("sudo tar -xvzf /tmp/{}.tgz --directory {}/".format(static, static_path))
        run("sudo rm /tmp/{}.tgz".format(static))
        run("sudo rm /data/web_static/current")
        run("sudo ln -nsf /data/web_static/releases/{} /data/web_static/current"
            .format(static))
        run("sudo mv {}/web_static/* {}".format(static_path, static_path))
        run("sudo rm -d {}/web_static/".format(static_path))
        return True
    return False


def deploy():
    path = do_pack()
    print("este es el path: ", path)
    if path is None:
        return False
    return do_deploy(path)


def do_clean(number=0):
    num_files = local("ls -1t versions/ | wc -l", capture=True)
    if number == "0":
        number = "1"
    dif = int(num_files) - int(number)
    if dif > 0:
        for i in range(0, dif):
            local("rm  versions/$(ls -1t versions/ | tail -1)")
