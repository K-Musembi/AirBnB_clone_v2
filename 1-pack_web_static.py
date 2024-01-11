#!/usr/bin/python3
"""Generate compressed archive
"""

from fabric.api import task, local
from datetime import datetime


@task
def do_pack():
    """Compress a local folder"""

    local("mkdir -p versions")

    current = datetime.now()

    time = current.strftime("%Y%m%d%H%M%S")

    local(f"tar -czvf web_static_{time}.tgz -C web_static .")

    local(f"mv web_static_{time}.tgz versions")

    return f"versions/web_static_{time}.tgz"
