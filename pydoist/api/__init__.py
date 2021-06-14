from abc import ABCMeta, abstractmethod
from secrets import token_hex
from typing import Generic, List, Optional, TypeVar

import requests
from pydantic.generics import GenericModel
from requests import Response
from todoist.api import TodoistAPI
from typing_extensions import ParamSpec

DataT = TypeVar('DataT')


class ICrud(GenericModel, Generic[DataT]):

    @abstractmethod
    def create(self, obj: DataT) -> Response:
        raise NotImplementedError

    @abstractmethod
    def update(self, obj: DataT) -> Response:
        raise NotImplementedError

    @abstractmethod
    def delete(self, obj: DataT) -> Response:
        raise NotImplementedError

    @abstractmethod
    def retrieve(self, id: int) -> Response:
        raise NotImplementedError

    @abstractmethod
    def retrieve_all(self, id: int) -> Response:
        raise NotImplementedError


def authorize():
    api = TodoistAPI('a256127132088503212ed304625e0400f54a3117')
    api.sync()
    print(api.state)
    breakpoint()
