from pip_services4_components.config import ConfigParams
from pip_services4_components.refer import References, Descriptor

from service_beacons.clients.version1.BeaconsDirectClientV1 import BeaconsDirectClientV1
from service_beacons.services.BeaconsService import BeaconsService
from service_beacons.persistence.BeaconsMemoryPersistence import BeaconsMemoryPersistence
from .BeaconsClientV1Fixture import BeaconsClientV1Fixture

class TestBeaconsDirectClientV1():
    @classmethod
    def setup_class(cls):
        cls.service = BeaconsService()
        cls.persistence = BeaconsMemoryPersistence()

        cls.client = BeaconsDirectClientV1()

        cls.references = References.from_tuples(
            Descriptor('beacons', 'persistence', 'memory', 'default', '1.0'), cls.persistence,
            Descriptor('beacons', 'service', 'default', 'default', '1.0'), cls.service,
            Descriptor('beacons', 'client', 'direct', 'default', '1.0'), cls.client
        )
        cls.service.set_references(cls.references)
        cls.client.set_references(cls.references)

        cls.fixture = BeaconsClientV1Fixture(cls.client)

        cls.persistence.open(None)

    def teardown_method(self, method):
        self.persistence.close(None)

    def test_crud_operations(self):
        self.fixture.test_crud_operations()

    def test_calculate_position(self):
        self.fixture.test_calculate_position()