from typing import Any, Dict, List, Optional

import requests
from pydantic.main import BaseModel
from pydoist.models import (ItemModel, NoteModel, ProjectObjectModel,
                            SectionModel)
from todoist.api import TodoistAPI


class ProjectInfoModel(BaseModel):
    project: ProjectObjectModel
    notes: List[NoteModel]


class ProjectDataModel(BaseModel):
    project: ProjectObjectModel
    items: List[ItemModel]
    sections: List[SectionModel]
    project_notes: List[NoteModel]


class ProjectApi:

    def __init__(self, api: TodoistAPI):
        self.__api = api

    @property
    def api(self):
        return self.__api

    def create(self, obj: ProjectObjectModel) -> Any:
        raise NotImplementedError

    def update(self, obj: ProjectObjectModel) -> Any:
        raise NotImplementedError

    def delete(self, obj: ProjectObjectModel) -> Any:
        raise NotImplementedError

    def retrieve_data(self, id: int) -> ProjectDataModel:
        info = self.api.projects.get_data(id)
        return ProjectDataModel(**info)

    def retrieve_info(self, id: int) -> ProjectInfoModel:
        info = self.api.projects.get(id)
        return ProjectInfoModel(**info)

    def retrieve_all(self) -> List[ProjectObjectModel]:
        return [ProjectObjectModel(**proj.data) for proj in self.api.projects.all()]
