#!/usr/bin/python3
import os
from fabric.api import env
from fabric.api import local
from fabric.api import put
from fabric.api import run

env.hosts = ['52.87.216.6', '54.175.46.5']
env.key_filename = '/root/.ssh/school'


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        value(int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    value = 1 if int(value) == 0 else int(value)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(value)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(value)]
        [run("rm -rf ./{}".format(a)) for a in archives]
