import subprocess
from typing import NoReturn


def celery_runner(c: str) -> NoReturn:
    subprocess.run(c.split(' '))
