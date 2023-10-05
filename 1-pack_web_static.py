#!/usr/bin/python3
"""This module showcases fabric usage"""

from fabric.operations import local
from datetime import datetime


def do_pack():
    """utilize fabric"""
    dt = datetime.now()
    vname = "web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                 dt.month,
                                                 dt.day, dt.hour,
                                                 dt.minute, dt.second)
    local("mkdir -p ./versions")
    result = local("tar -czvf ./versions/{} web_static".format(vname))
    if result.succeeded:
        return result
    else:
        return None
