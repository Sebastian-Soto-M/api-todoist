from typing import Any, Dict, List, Optional

import requests
from pydantic.main import BaseModel
from pydoist.models import (ItemModel, NoteModel,
                            SectionModel)
from todoist.api import TodoistAPI


class SectionApi:

    def __init__(self, api: TodoistAPI):
        self.__api = api

    @property
    def api(self):
        return self.__api

    def create(self, name: str, project_id: int,
               order: Optional[int] = None) -> Any:
        self.api.sections.add(name, project_id, section_order=order)
        self.api.commit()

    def update(self, obj: Any) -> Any:
        raise NotImplementedError

    def delete(self, id: str) -> Any:
        self.api.sections.delete(id)
        self.api.commit()
