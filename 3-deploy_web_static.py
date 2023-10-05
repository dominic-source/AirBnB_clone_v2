#!/usr/bin/python3
""" This module bundles the full deploy"""
from fabric.operations import 
do_deploy = __import__("2-do_deploy_web_static.py").do_deploy
do_pack = __import__("1-pack_web_static.py").do_pack

def deploy():
    """The deployment of the web static file"""
    archive_path = do_pack()
    if not archive_path:
        return False
    deploy = do_deploy(archive_path)
    return deploy
