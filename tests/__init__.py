import logging
import sys

from todoist.utils import CLI, Argument


def cli_options() -> dict:
    options = {
        "name": "Todoits Tests",
        "flags": {Argument('v', 'verbose', 'Use the DEBUG logging mode')},
        "arguments": {
            Argument('s', 'suite', 'Select a suite of tests to run',
                     str, {'models'})
        }
    }
    return CLI(**options).read()


CLI_OPTS = cli_options()

logging_mode = logging.INFO if not CLI_OPTS.verbose else logging.DEBUG

logging.basicConfig(level=logging_mode, stream=sys.stdout,
                    format='\t%(levelname)s| %(message)s')
