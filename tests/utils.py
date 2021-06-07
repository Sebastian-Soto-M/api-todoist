import json
import logging
from os.path import join
from pathlib import Path

from todoist.utils import CLI, Argument


def debug_json(logger: logging.Logger, title: str, data: dict, indent=2):
    logger.debug(f'[{title}] {json.dumps(data, indent=indent)}')


def cli_options(suites: list) -> dict:
    options = {
        "name": "Todoits Tests",
        "flags": {Argument('v', 'verbose', 'Use the DEBUG logging mode')},
        "arguments": {
            Argument('s', 'suite', 'Select a suite of tests to run',
                     str, suites)
        }
    }
    return CLI(**options).read()


def mocks_path(obj: str) -> dict:
    return json.loads(
        Path(join(Path(__file__).parent, 'mocks.json')).open().read()
    )[obj]
