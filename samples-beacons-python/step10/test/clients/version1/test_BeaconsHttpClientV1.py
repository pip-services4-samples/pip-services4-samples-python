from pip_services4_components.config import ConfigParams
from pip_services4_components.refer import References, Descriptor

from service_beacons.clients.version1.BeaconsHttpClientV1 import BeaconsHttpClientV1
from service_beacons.services.BeaconsService import BeaconsService
from service_beacons.persistence.BeaconsMemoryPersistence import BeaconsMemoryPersistence
from service_beacons.controllers.version1.BeaconsHttpControllerV1 import BeaconsHttpControllerV1
from .BeaconsClientV1Fixture import BeaconsClientV1Fixture

http_config = ConfigParams.from_tuples(
    'connection.protocol', 'http',
    'connection.port', 3000,
    'connection.host', 'localhost')

class TestBeaconsHttpClientV1:
    persistence: BeaconsMemoryPersistence
    service: BeaconsService
    controller: BeaconsHttpControllerV1
    client: BeaconsHttpClientV1
    fixture: BeaconsClientV1Fixture

    @classmethod
    def setup_class(cls):
        cls.service = BeaconsService()
        cls.persistence = BeaconsMemoryPersistence()

        cls.controller = BeaconsHttpControllerV1()
        cls.controller.configure(http_config)

        cls.client = BeaconsHttpClientV1()
        cls.client.configure(http_config)

        cls.references = References.from_tuples(
            Descriptor('beacons', 'persistence', 'memory', 'default', '1.0'), cls.persistence,
            Descriptor('beacons', 'service', 'default', 'default', '1.0'), cls.service,
            Descriptor('beacons', 'controller', 'http', 'default', '1.0'), cls.controller,
            Descriptor('beacons', 'client', 'http', 'default', '1.0'), cls.client
        )
        cls.controller.set_references(cls.references)
        cls.client.set_references(cls.references)
        cls.service.set_references(cls.references)

        cls.fixture = BeaconsClientV1Fixture(cls.client)

        cls.persistence.open(None)
        cls.controller.open(None)
        cls.client.open(None)

    @classmethod
    def teardown_class(cls):
        cls.client.close(None)
        cls.controller.close(None)
        cls.persistence.close(None)

    def test_crud_operations(self):
        self.fixture.test_crud_operations()

    def test_calculate_position(self):
        self.fixture.test_calculate_position()

