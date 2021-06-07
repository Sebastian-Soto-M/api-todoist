import logging
from unittest import TestSuite, TextTestRunner, makeSuite

from . import CLI_OPTS, TESTS

logger = logging.getLogger('TestMain')


def get_suite() -> TestSuite:
    suite = TestSuite()
    selected_suite = CLI_OPTS.suite
    if selected_suite != False:
        suite.addTest(makeSuite(TESTS[selected_suite]))
    else:
        tests = set()
        for k, v in TESTS.items():
            tests.add(f'Test{k.capitalize()}')
            suite.addTest(makeSuite(v))
        logger.info(f'The following tests will run: {tests}')
    return suite


if __name__ == "__main__":
    runner = TextTestRunner()
    runner.run(get_suite())
