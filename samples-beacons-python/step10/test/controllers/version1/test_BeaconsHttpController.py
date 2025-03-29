import json
import time

from json import JSONDecodeError
from typing import Union

from pip_services4_components.config import ConfigParams
from pip_services4_components.refer import References, Descriptor
from pip_services4_commons.reflect import PropertyReflector
from pip_services4_components.exec import Parameters
from pip_services4_http.test.TestCommandableHttpClient import TestCommandableHttpClient

from service_beacons.data.version1 import BeaconV1, BeaconTypeV1
from service_beacons.services.BeaconsService import BeaconsService
from service_beacons.persistence.BeaconsMemoryPersistence import BeaconsMemoryPersistence
from service_beacons.controllers.version1.BeaconsHttpControllerV1 import BeaconsHttpControllerV1

BEACON1 = BeaconV1("1", "1", BeaconTypeV1.AltBeacon, "00001", "TestBeacon1", {"type": 'Point', "coordinates": [0, 0]}, 50.0)
BEACON2 = BeaconV1("2", "1", BeaconTypeV1.iBeacon, "00002", "TestBeacon2", {"type": 'Point', "coordinates": [2, 2]}, 70.0)
BEACON3 = BeaconV1("3", "2", BeaconTypeV1.AltBeacon, "00003", "TestBeacon3", {"type": 'Point', "coordinates": [10, 10]}, 50.0)

class TestBeaconsHttpControllerV1:
    _persistence: BeaconsMemoryPersistence
    _service: BeaconsService
    _controller: BeaconsHttpControllerV1
    _client: TestCommandableHttpClient

    @classmethod
    def setup_class(cls):
        restConfig = ConfigParams.from_tuples(
            "connection.protocol", "http",
            "connection.host", "localhost",
            "connection.port", 3010)

        cls._persistence = BeaconsMemoryPersistence()
        cls._persistence.configure(ConfigParams())

        cls._service = BeaconsService()
        cls._service.configure(ConfigParams())

        cls._controller = BeaconsHttpControllerV1()
        cls._controller.configure(restConfig)

        cls._client = TestCommandableHttpClient('v1/beacons')
        cls._client.configure(restConfig)

        references = References.from_tuples(
            Descriptor('beacons', 'persistence', 'memory', 'default', '1.0'), cls._persistence,
            Descriptor('beacons', 'service', 'default', 'default', '1.0'), cls._service,
            Descriptor('beacons', 'controller', 'http', 'default', '1.0'), cls._controller)
        cls._service.set_references(references)
        cls._controller.set_references(references)

        cls._persistence.open(None)
        cls._controller.open(None)
        cls._client.open(None)

    @classmethod
    def teardown_class(cls):
        cls._client.close(None)
        cls._controller.close(None)
        cls._persistence.close(None)
 
    def test_crud_operations(self):
        # Create the first beacon
        beacon1 = self._client.call_command(
            'create_beacon',
            None,
            { 'beacon': BEACON1 })

        assert beacon1 is not None
        assert beacon1['id'] == BEACON1.id
        assert beacon1['site_id'] == BEACON1.site_id
        assert beacon1['udi'] == BEACON1.udi
        assert beacon1['type'] == BEACON1.type
        assert beacon1['label'] == BEACON1.label
        assert beacon1['center'] is not None

        # Create the second beacon
        beacon2 = self._client.call_command(
            'create_beacon',
            None,
            { 'beacon': BEACON2 })

        assert beacon2 is not None
        assert beacon2['id'] == BEACON2.id
        assert beacon2['site_id'] == BEACON2.site_id
        assert beacon2['udi'] == BEACON2.udi
        assert beacon2['type'] == BEACON2.type
        assert beacon2['label'] == BEACON2.label
        assert beacon2['center'] is not None

        # Get all beacons
        page = self._client.call_command(
            'get_beacons',
            None,
            { })
        assert page is not None
        assert len(page['data']) == 2

        beacon1 = page['data'][0]

        # Update the beacon
        beacon1['label'] = "ABC"
        beacon = self._client.call_command(
            'update_beacon',
            None,
            { 'beacon': beacon1 })
        assert beacon is not None
        assert beacon1['id'] == beacon['id']
        assert "ABC" == beacon['label']

        # Get beacon by udi
        beacon = self._client.call_command(
            'get_beacon_by_udi',
            None,
            { 'udi': beacon1['udi'] })
        assert beacon is not None
        assert beacon['id'] == beacon1['id']

        # Calculate position for one beacon
        position = self._client.call_command(
            'calculate_position',
            None,
            { 'site_id': "1", 'udis': ['00001'] })
        assert position is not None
        assert "Point" == position["type"]
        assert 2 == len(position["coordinates"])
        assert 0 == position["coordinates"][0]
        assert 0 == position["coordinates"][1]

        # Delete beacon
        self._client.call_command(
            'delete_beacon_by_id',
            None,
            { 'id': beacon1['id'] })

        # Try to get deleted beacon
        beacon = self._client.call_command(
            'get_beacon_by_id',
            None,
            { 'id': beacon1['id'] })
        assert beacon is None

