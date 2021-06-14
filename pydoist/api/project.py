from typing import Any, List

from pydoist.api import ApiCrud
from pydoist.models import (ProjectDataModel, ProjectInfoModel,
                            ProjectObjectModel)
from todoist.api import TodoistAPI


class ProjectApi(ApiCrud):

    def __init__(self, api: TodoistAPI):
        super().__init__(api)

    def create(self, obj: ProjectObjectModel) -> Any:
        pass

    def update(self, obj: ProjectObjectModel) -> Any:
        pass

    def delete(self, obj: ProjectObjectModel) -> Any:
        pass

    def retrieve_data(self, id: int) -> ProjectDataModel:
        info = self.api.projects.get_data(id)
        return ProjectDataModel(**info)

    def retrieve_info(self, id: int) -> ProjectInfoModel:
        info = self.api.projects.get(id)
        return ProjectInfoModel(**info)

    def retrieve(self, id: int) -> ProjectObjectModel:
        return ProjectObjectModel(**self.api.projects.get_by_id(id))

    def retrieve_all(self) -> List[ProjectObjectModel]:
        return [ProjectObjectModel(**proj.data) for proj in self.api.projects.all()]
