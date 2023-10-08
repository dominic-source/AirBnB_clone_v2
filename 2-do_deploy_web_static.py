#!/usr/bin/python3
"""This module houses the function for distributing the versions"""

from fabric.api import env
from fabric.operations import sudo, put, local
import os

env.hosts = ['3.94.185.85', '100.24.255.207']


def do_deploy(archive_path):
    """The deployment of the web static files"""

    if not os.path.exists(archive_path):
        return False

    try:
        filename = os.path.basename(archive_path)
        dfile = filename.split(".")[0]
        sudo("mkdir -p /data/web_static/releases/{}/".format(dfile))
        sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
             .format(filename, dfile))
        sudo("rm /tmp/{}".format(filename))
        sudo(
            "mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/"
            .format(dfile, dfile))
        sudo("rm -rf /data/web_static/releases/{}/web_static"
             .format(dfile))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s /data/web_static/releases/{} /data/web_static/current"
             .format(dfile))
        return True
    except Exception:
        return False
