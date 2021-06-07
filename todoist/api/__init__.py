from abc import ABCMeta, abstractmethod
from typing import Generic, List, Optional, TypeVar

from pydantic.generics import GenericModel

DataT = TypeVar('DataT')


class ICrud(GenericModel, Generic[DataT], ABCMeta):

    @abstractmethod
    def create(self, obj: DataT):
        raise NotImplementedError

    @abstractmethod
    def update(self, obj: DataT):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def retrieve(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def retrieve_all(self, id: int):
        raise NotImplementedError
