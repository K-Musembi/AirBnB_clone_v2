#!/usr/bin/python3
"""Distribute archive to web servers
"""

from fabric.api import task, local, run, env, put
from datetime import datetime
import os

env.hosts = ["34.224.83.243", "35.153.67.53"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


@task
def do_pack():
    """Compress a local folder"""

    local("mkdir -p versions")

    current = datetime.now()

    time = current.strftime("%Y%m%d%H%M%S")

    local(f"tar -czvf web_static_{time}.tgz -C web_static .")

    local(f"mv web_static_{time}.tgz versions")

    return f"versions/web_static_{time}.tgz"


@task
def do_deploy(archive_path):
    """Deploy archive to servers"""

    if not os.path.exists(archive_path):
        return False

    archive = os.path.basename(archive_path)

    put(f"{archive_path}", f"/tmp/{archive}")

    folder = os.path.splitext(archive)[0]

    run(f"mkdir -p /data/web_static/releases/{folder}")

    run(f"tar -xzvf /tmp/{archive} -C /data/web_static/releases/{folder}")

    run(f"rm /tmp/{archive}")

    run("rm -rf /data/web_static/current")

    run(f"ln -s /data/web_static/releases/{folder} /data/web_static/current")

    return True
