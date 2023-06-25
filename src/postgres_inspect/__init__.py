import logging.config
import pathlib

import yaml

with open(pathlib.Path() / 'logging.conf.yml', 'r') as f:
    logging.config.dictConfig(yaml.safe_load(f))
