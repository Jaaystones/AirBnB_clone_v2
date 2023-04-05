from fabric.api import run, local, env, put
from datetime import datetime
import os 
from fabric.context_managers import cd

env.hosts = ['52.87.216.6', '54.175.46.5']
env.user = 'ubuntu'
env.password = '/root/.ssh/school'

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder of the AirBnB Clone repo
    """
    try:
        if not os.path.exists("versions")):
            local("mkdir -p versions")
        now = datetime.now()
        date_time = now.strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date_time)
        local("tar -czvf {} web_static".format(file_name))
        return file_name
    except:
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or pulls up an error - False.
        Otherwise - True.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the server
        put(archive_path, "/tmp/")

        # Create the directory where the files will be extracted
        static = archive_path.split("/")[-1]
        static_path = static.split(".")[0]
        run("sudo mkdir -p /data/web_static/releases/{}/"\
            .format(static_path))

        # Extract the archive into the directory
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/"\
            .format(static, static_path))

        # Delete the archive from the server
        run("sudo rm /tmp/{}".format(static))

        # Move the contents of the web_static directory up one level
        run("sudo mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/"\
            .format(static, static_path))

        # Remove the now empty web_static directory
        run("sudo rm -rf /data/web_static/releases/{}/web_static"\
            .format(static_path))

        # Delete the symbolic link /data/web_static/current from the web server
        run("rm -rf /data/web_static/current")

        # Create a symbolic link from /data/web_static/current to the new version of the code
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"\
            .format(static_path))

        return True
    except:
        return False

def deploy():
    """
    Full deployment of AirBnB Clone
    """
    # Create the archive of the web_static folder
    archive_path = do_pack()

    if archive_path is None:
        return False

    # Distribute the archive to the web servers
    return do_deploy(archive_path)
