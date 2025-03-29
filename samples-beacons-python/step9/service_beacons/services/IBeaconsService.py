from abc import ABC, abstractmethod
from typing import Any, List, Optional

from pip_services4_data.query import PagingParams, FilterParams, DataPage
from pip_services4_components.context import IContext

from ..data.version1 import BeaconV1

class IBeaconsService(ABC):
    @abstractmethod
    def get_beacons_by_filter(self, context: Optional[IContext], filter: FilterParams, paging: PagingParams) -> DataPage:
        pass

    @abstractmethod
    def get_beacon_by_id(self, context: Optional[IContext], id: str) -> BeaconV1:
        pass

    @abstractmethod
    def get_beacon_by_udi(self, context: Optional[IContext], udi: str) -> BeaconV1:
        pass

    @abstractmethod
    def calculate_position(self, context: Optional[IContext], site_id: str, udis: List[str]) -> Any:
        pass

    @abstractmethod
    def create_beacon(self, context: Optional[IContext], entity: BeaconV1) -> BeaconV1:
        pass

    @abstractmethod
    def update_beacon(self, context: Optional[IContext], entity: BeaconV1) -> BeaconV1:
        pass

    @abstractmethod
    def delete_beacon_by_id(self, context: Optional[IContext], id: str) -> BeaconV1:
        pass

