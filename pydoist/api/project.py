import requests
from requests import Response
from pydoist import API_URL
from pydoist.models import ProjectModel

from . import CLIENT_ID, CLIENT_SECRET, TOKEN, ICrud


class ProjectApi(ICrud[ProjectModel]):

    __URL = API_URL.format('projects')

    def create(self, obj: ProjectModel) -> Response:
        raise NotImplementedError

    def update(self, obj: ProjectModel) -> Response:
        raise NotImplementedError

    def delete(self, obj: ProjectModel) -> Response:
        raise NotImplementedError

    def retrieve(self, id: int) -> Response:
        raise NotImplementedError

    def retrieve_all(self, id: int) -> Response:
        return requests.get(f'{self.__URL}/{id}')
