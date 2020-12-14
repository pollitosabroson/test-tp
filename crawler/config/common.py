import os

import yaml

__config = None


def config():
    """Get config."""
    global __config
    cwd = os.getcwd()
    if not __config:
        with open(f"{cwd}/config/config.yaml", mode='r') as f:
            __config = yaml.safe_load(f)

    return __config
