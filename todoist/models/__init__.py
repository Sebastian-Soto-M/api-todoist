from __future__ import annotations

from typing import List, Optional, Set, Union

from pydantic import BaseModel

from requests.models import Response


class ProjectModel(BaseModel):
    id: int
    name: str
    color: int
    parent_id: Optional[int]
    order: int
    comment_count: int
    shared: bool
    favorite: bool
    inbox_project: Optional[bool]
    team_inbox: Optional[bool]
    sync_id: int
    url: str

    @staticmethod
    def parse(req: Response) -> ProjectModel:
        return ProjectModel.parse_raw(req.text)

    @staticmethod
    def parse_list(req: Response) -> List[ProjectModel]:
        return [ProjectModel.parse_obj(obj) for obj in req.json()]


class SectionModel(BaseModel):
    id: int
    project_id: int
    order: int
    name: str


class Due(BaseModel):
    string: str
    date: str
    recurring: bool
    datetime: Optional[str]
    timezone: Optional[str]


class TaskModel(BaseModel):
    assignee: int
    assigner: int
    comment_count: int
    completed: bool
    content: str
    description: str
    due: Due
    id: int
    label_ids: Set[int]
    order: int
    priority: int
    project_id: int
    section_id: int
    parent_id: int
    url: str
