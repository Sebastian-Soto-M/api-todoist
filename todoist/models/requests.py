from typing import Optional

from pydantic import BaseModel
from todoist.enums import ColorEnum


class CreateProjectModel(BaseModel):
    name: str
    parent_id: Optional[int]
    color: Optional[ColorEnum]
    favorite = False


class UpdateProjectModel(BaseModel):
    id: int
    name: Optional[str]
    color: Optional[ColorEnum]
    favorite: Optional[bool]


class CreateSectionModel(BaseModel):
    name: str
    project_id: int
    order: Optional[int]
