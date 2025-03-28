from typing import Optional, List, Any

from pip_services4_components.context import IContext
from pip_services4_data.query import DataPage, FilterParams, PagingParams
from pip_services4_http.clients import CommandableHttpClient

from .IBeaconsClientV1 import IBeaconsClientV1
from ...data.version1 import BeaconV1

class BeaconsHttpClientV1(CommandableHttpClient, IBeaconsClientV1):
    def __init__(self):
        super(BeaconsHttpClientV1, self).__init__("v1/beacons")

    def _dict_to_beacon(self, value) -> BeaconV1:
        if value == None:
            return None
        
        beacon = BeaconV1()
        beacon.id = value['id']
        beacon.site_id = value['site_id']
        beacon.type = value['type']
        beacon.udi = value['udi']
        beacon.label = value['label']
        beacon.center = value['center']
        beacon.radius = value['radius']

        return beacon
    
    def _array_to_beacons(self, values):
        if values == None:
            return None
        
        beacons = []
        for value in values:
            beacons.append(self._dict_to_beacon(value))

        return beacons

    def get_beacons_by_filter(self, context: Optional[IContext], filter: FilterParams,
                              paging: PagingParams) -> DataPage:
        result = self.call_command(
            'get_beacons',
            context,
            {
                'filter': filter,
                'paging': paging
            }
        )

        return DataPage(self._array_to_beacons(result['data']), result['total'])

    def get_beacon_by_id(self, context: Optional[IContext], id: str) -> BeaconV1:
        result = self.call_command(
            'get_beacon_by_id',
            context,
            {
                'id': id
            }
        )
        return self._dict_to_beacon(result)

    def get_beacon_by_udi(self, context: Optional[IContext], udi: str) -> BeaconV1:
        result = self.call_command(
            'get_beacon_by_udi',
            context,
            {
                'udi': udi
            }
        )
        return self._dict_to_beacon(result)

    def calculate_position(self, context: Optional[IContext], site_id: str, udis: List[str]) -> Any:
        return self.call_command(
            'calculate_position',
            context,
            {
                'site_id': site_id,
                'udis': udis
            }
        )

    def create_beacon(self, context: Optional[IContext], entity: BeaconV1) -> BeaconV1:
        result = self.call_command(
            'create_beacon',
            context,
            {
                'beacon': entity
            }
        )
        return self._dict_to_beacon(result)

    def update_beacon(self, context: Optional[IContext], entity: BeaconV1) -> BeaconV1:
        result = self.call_command(
            'update_beacon',
            context,
            {
                'beacon': entity
            }
        )
        return self._dict_to_beacon(result)

    def delete_beacon_by_id(self, context: Optional[IContext], id: str) -> BeaconV1:
        result = self.call_command(
            'delete_beacon_by_id',
            context,
            {
                'id': id
            }
        )
        return self._dict_to_beacon(result)

