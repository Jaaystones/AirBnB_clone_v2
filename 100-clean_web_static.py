#!/usr/bin/python3
"""
Fabric script based on 3-deploy_web_static.py to clean up outdated archives.
"""

from fabric.api import *
from os import path

env.hosts = ['52.87.216.6', '54.175.46.5']


def do_clean(num=0):
     """Delete out-of-date archives.
    Args:
        numb (int): The number of archives to keep.
    If num is 0 or 1, keeps only the most recent archive. If
    num is 2, keeps the most and second-most recent archives,
    etc.
    """
    num = 1 if int(num) == 0 else int(num)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(num)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(numb)]
        [run("rm -rf ./{}".format(a)) for a in archives]
