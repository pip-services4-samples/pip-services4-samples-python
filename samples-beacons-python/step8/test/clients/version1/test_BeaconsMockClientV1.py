from service_beacons.clients.version1.BeaconsMockClientV1 import BeaconsMockClientV1

from .BeaconsClientV1Fixture import BeaconsClientV1Fixture

class TestBeaconsMockClientV1:
    client: BeaconsMockClientV1
    fixture: BeaconsClientV1Fixture

    @classmethod
    def setup_class(cls):
        cls.client = BeaconsMockClientV1()
        cls.fixture = BeaconsClientV1Fixture(cls.client)

    def test_crud_operations(self):
        self.fixture.test_crud_operations()

    def test_calculate_position(self):
        self.fixture.test_calculate_position()


