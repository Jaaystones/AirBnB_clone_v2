#!/usr/bin/python3
"""
Fabric script based on 3-deploy_web_static.py to clean up outdated archives.
"""

from fabric.api import *
from os import path

env.user = 'ubuntu'
env.hosts = ['52.87.216.6', '54.175.46.5']
env.key_filename = '/root/.ssh/school'


def do_clean(number=0):
    """
    Deletes all unnecessary archives in the versions and web_static/releases
    directories. The number of archives to keep can be specified with the
    number argument. By default, all but the most recent archive will be
    deleted.
    """
    try:
        number = int(number)
    except ValueError:
        print("Invalid number: {}".format(number))
        return False

    if number < 0:
        print("Invalid number: {}".format(number))
        return False

    # Get a list of all archives
    with cd('/data/web_static/releases'):
        archives = sorted(run('ls -1tr').split())

    # Delete old archives in versions directory
    with cd('/data/web_static/releases'):
        archives_to_delete = archives[:-number]
        if len(archives_to_delete) > 0:
            for archive in archives_to_delete:
                if path.exists(archive):
                    run('rm -f {}'.format(archive))

    # Delete old archives in web_static/releases directory on both servers
    with cd('/data/web_static/releases'):
        archives_to_delete = archives[:-number]
        if len(archives_to_delete) > 0:
            for archive in archives_to_delete:
                with settings(host_string=env.hosts[0]):
                    if path.exists(archive):
                        run('rm -f {}'.format(archive))
                with settings(host_string=env.hosts[1]):
                    if path.exists(archive):
                        run('rm -f {}'.format(archive))

    return True
