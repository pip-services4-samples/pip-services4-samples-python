from abc import ABC, abstractmethod
from typing import Optional

from pip_services4_data.query import PagingParams, FilterParams, DataPage
from pip_services4_components.context import IContext

from ..data.version1 import BeaconV1

class IBeaconsPersistence(ABC):

    @abstractmethod
    def get_page_by_filter(self, context: Optional[IContext], filter: FilterParams, paging: PagingParams) -> DataPage:
        pass

    @abstractmethod
    def get_one_by_id(self, context: Optional[IContext], id: str) -> BeaconV1:
        pass

    @abstractmethod
    def get_one_by_udi(self, context: Optional[IContext], udi: str) -> BeaconV1:
        pass

    @abstractmethod
    def create(self, context: Optional[IContext], entity: BeaconV1) -> BeaconV1:
        pass

    @abstractmethod
    def update(self, context: Optional[IContext], entity: BeaconV1) -> BeaconV1:
        pass

    @abstractmethod
    def delete_by_id(self, context: Optional[IContext], id: str) -> BeaconV1:
        pass
