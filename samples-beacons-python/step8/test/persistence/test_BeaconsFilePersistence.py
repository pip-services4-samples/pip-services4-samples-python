from service_beacons.persistence.BeaconsFilePersistence import BeaconsFilePersistence
from .BeaconsPersistenceFixture import BeaconsPersistenceFixture

class TestBeaconFilePersistence():
    persistence: BeaconsFilePersistence
    fixture: BeaconsPersistenceFixture

    @classmethod
    def setup_class(cls):
        cls.persistence = BeaconsFilePersistence("./data/beacons.test.json")
        cls.fixture = BeaconsPersistenceFixture(cls.persistence)

    def setup_method(self, method):
        self.persistence.clear(None)

    def test_crud_operations(self):
        self.fixture.test_crud_operations()

    def test_get_with_filter(self):
        self.fixture.test_get_with_filter()