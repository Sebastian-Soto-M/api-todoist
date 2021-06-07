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


CLIENT_ID = 'b641283c4ff34d6ca9c7398f39ded641'
CLIENT_SECRET = 'e1f3e45c010142e1b5b3cd80edac19e5'
TOKEN = ''
__SCOPE = ['tark:add', 'data:read', 'data:read_write',
           'data:delete', 'project:delete']


def auth_url():
    base_url = 'https://pydoist.com/oauth/authorize'
    params = {
        'client_id': CLIENT_ID,
        'scope': __SCOPE[2],
        'state': token_hex(16)
    }
    return requests.get(base_url, params=params)


def authorize():
    api = TodoistAPI('a256127132088503212ed304625e0400f54a3117')
    api.sync()
    print(api.state)
    breakpoint()
