import logging
import time
from unittest import TestCase, main, skip

from pydoist.api.project import ProjectApi, ProjectDataModel, ProjectInfoModel
from pydoist.models import ProjectObjectModel
from pydoist.utils import FORMAT
from todoist.api import TodoistAPI

from .utils import debug_json


class TestProject(TestCase):
    api: ProjectApi

    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(cls.__name__)
        tapi = TodoistAPI('a256127132088503212ed304625e0400f54a3117')
        cls.api = ProjectApi(tapi)

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        info = FORMAT % (TestProject.__name__,
                         self.id().split('.')[-1], t)
        self.logger.info(info)

    def test_get(self):
        obj = self.api.retrieve(2266883000)  # personal project
        debug_json(self.logger, 'ProjectObjectModel', obj.dict())
        self.assertIsInstance(obj, ProjectObjectModel)

    def test_get_info(self):
        obj = self.api.retrieve_info(2266883000)  # personal project
        debug_json(self.logger, 'ProjectInfoModel', obj.dict())
        self.assertIsInstance(obj, ProjectInfoModel)

    def test_get_data(self):
        obj = self.api.retrieve_data(2266883000)  # personal project
        debug_json(self.logger, 'ProjectDataModel', obj.dict())
        self.assertIsInstance(obj, ProjectDataModel)


if __name__ == "__main__":
    main()
