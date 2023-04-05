#!/usr/bin/python3
from fabric.api import local
from time import strftime
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        # Create the versions directory if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Create the name of the archive file
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(now)

        # Create the archive using the tar command
        local("tar -cvzf {} web_static".format(archive_path))

        # Return the path to the archive file
        return archive_path
    return None
