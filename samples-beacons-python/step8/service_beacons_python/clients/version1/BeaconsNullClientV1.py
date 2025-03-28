from typing import Optional, List, Any

from pip_services4_components.context import IContext
from pip_services4_data.query import DataPage, FilterParams, PagingParams

from .IBeaconsClientV1 import IBeaconsClientV1
from ...data.version1 import BeaconV1

class BeaconsNullClientV1(IBeaconsClientV1):
    def __init__(self):
        pass

    def get_beacons_by_filter(self, context: Optional[IContext], filter: FilterParams,
                              paging: PagingParams) -> DataPage:
        return DataPage([], 0)

    def get_beacon_by_id(self, context: Optional[IContext], id: str) -> BeaconV1:
        return None

    def get_beacon_by_udi(self, context: Optional[IContext], udi: str) -> BeaconV1:
        return None

    def calculate_position(self, context: Optional[IContext], site_id: str, udis: List[str]) -> Any:
        return None

    def create_beacon(self, context: Optional[IContext], entity: BeaconV1) -> BeaconV1:
        return None

    def update_beacon(self, context: Optional[IContext], entity: BeaconV1) -> BeaconV1:
        return None

    def delete_beacon_by_id(self, context: Optional[IContext], id: str) -> BeaconV1:
        return None

