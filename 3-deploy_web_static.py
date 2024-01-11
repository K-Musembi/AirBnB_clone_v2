#!/usr/bin/python3
"""Create archive and deploy to servers"""

from fabric.api import task, execute, env

do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy

env.hosts = ["34.224.83.243", "35.153.67.53"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


@task
def deploy():
    """Archive and deploy"""

    dictionary = execute(do_pack)

    if not dictionary:
        return False

    path = next(iter(dictionary.values()))

    print(path)

    result = do_deploy(path)

    return result
