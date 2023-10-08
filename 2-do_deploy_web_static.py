#!/usr/bin/python3
"""This module houses the function for distributing the versions"""

from fabric.api import env
from fabric.operations import run, put, local
import os

env.hosts = ['3.94.185.85', '100.24.255.207']


def do_deploy(archive_path):
    """The deployment of the web static files"""

    if not os.path.exists(archive_path):
        return False

    try:
        filename = os.path.basename(archive_path)
        dfile = filename.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(dfile))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename, dfile))
        run("rm /tmp/{}".format(filename))
        run(
            "mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/"
            .format(dfile, dfile))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(dfile))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(dfile))
        return True
    except Exception:
        return False
