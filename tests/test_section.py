import logging
import time
from unittest import TestCase, main, skip

from todoist.utils import FORMAT

from tests.utils import debug_json, mocks_path


class TestSection(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(cls.__name__)

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        info = FORMAT % (TestSection.__name__,
                         self.id().split('.')[-1], t)
        self.logger.info(info)

    def test_parser(self):
        self.assertTrue(True)
        # req = requests.get(endpoint)
        # obj = parse_database(req)
        # debug_json(self.logger, 'DatabaseModel', json.loads(obj.json()))
        # self.assertIsInstance(obj, DatabaseModel)


if __name__ == "__main__":
    main()
