import logging
import time
from unittest import TestCase, main, skip

from pydoist.utils import FORMAT
from pydoist.models import SectionModel
from pydoist.api.section import SectionApi
from pydoist.api.project import ProjectApi
from todoist.api import TodoistAPI

from tests.utils import debug_json, mocks_path


class TestSection(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = logging.getLogger(cls.__name__)
        cls.todoist_token = TodoistAPI(
            'a256127132088503212ed304625e0400f54a3117')
        cls.api = SectionApi(cls.todoist_token)
        cls.section_name = 'Shanti Loca'

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        info = FORMAT % (TestSection.__name__,
                         self.id().split('.')[-1], t)
        self.logger.info(info)

    def test_add_section(self):
        project_id = 2266883000
        self.api.create(self.section_name, project_id, 1)

    def test_delete_section(self):
        project_api = ProjectApi(self.todoist_token)
        obj = project_api.retrieve_data(
            2266883000)  # personal project
        sct_del_lst = [(sct.id, sct.name) for sct in obj.sections if
                       sct.name == self.section_name]
        for sct in sct_del_lst:
            self.api.delete(sct[0])
            self.logger.debug(f'Delete the section:\t{sct[1]}')


if __name__ == "__main__":
    main()
