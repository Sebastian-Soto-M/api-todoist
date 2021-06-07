import logging
import time
from unittest import TestCase, main, skip

import requests
import responses
from todoist import API_URL
from todoist.models import ProjectModel
from todoist.utils import FORMAT

from .utils import debug_json, mocks_path

URL = API_URL.format('projects')


class TestProject(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(cls.__name__)
        cls.response_bodies = mocks_path('project')

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        info = FORMAT % (TestProject.__name__,
                         self.id().split('.')[-1], t)
        self.logger.info(info)

    @responses.activate
    def test_parse(self):
        body = self.response_bodies['retrieve']
        uid = body['id']
        endpoint = f'{URL}/{uid}'
        responses.add(responses.GET, endpoint, json=body, status=200)

        req = requests.get(endpoint)
        obj = ProjectModel.parse(req)
        debug_json(self.logger, 'ProjectModel', obj.dict())
        self.assertIsInstance(obj, ProjectModel)

    @responses.activate
    def test_parse_list(self):
        body = self.response_bodies['retrieve_all']
        endpoint = URL
        responses.add(responses.GET, endpoint, json=body, status=200)

        req = requests.get(endpoint)
        obj = ProjectModel.parse_list(req)
        for proj in obj:
            debug_json(self.logger, 'ProjectModel', proj.dict())
        self.assertIsInstance(obj[1], ProjectModel)


if __name__ == "__main__":
    main()
