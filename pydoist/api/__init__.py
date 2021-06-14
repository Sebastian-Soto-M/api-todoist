from abc import ABCMeta, abstractmethod
from typing import Any, List, Optional

from todoist.api import TodoistAPI


class ApiCrud(metaclass=ABCMeta):

    def __init__(self, api: TodoistAPI):
        self.__api = api

    @property
    def api(self):
        return self.__api

    @abstractmethod
    def create(self, obj: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    def update(self, obj: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> Any:
        raise NotImplementedError

    @abstractmethod
    def retrieve(self, id: int) -> Optional[Any]:
        raise NotImplementedError

    @abstractmethod
    def retrieve_all(self, id: int) -> Optional[List[Any]]:
        raise NotImplementedError
