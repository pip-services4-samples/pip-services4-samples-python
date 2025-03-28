import os

from pip_services4_components.config import ConfigParams

from service_beacons_python.persistence.BeaconsMongoDbPersistence import BeaconsMongoDbPersistence
from .BeaconsPersistenceFixture import BeaconsPersistenceFixture

class TestBeaconMongoDbPersistence:
    persistence: BeaconsMongoDbPersistence
    fixture: BeaconsPersistenceFixture

    mongoUri = os.getenv('MONGO_SERVICE_URI')
    mongoHost = os.getenv('MONGO_SERVICE_HOST', default='localhost')
    mongoPort = os.getenv('MONGO_SERVICE_PORT', default=27017)
    mongoDatabase = os.getenv('MONGO_SERVICE_DB', default='test')

    @classmethod
    def setup_class(cls):
        if cls.mongoUri is None and cls.mongoHost is None:
            return

        db_config = ConfigParams.from_tuples('connection.uri', cls.mongoUri,
                                             'connection.host', cls.mongoHost,
                                             'connection.port', cls.mongoPort,
                                             'connection.database', cls.mongoDatabase)
        cls.persistence = BeaconsMongoDbPersistence()
        cls.fixture = BeaconsPersistenceFixture(cls.persistence)

        cls.persistence.configure(db_config)
        cls.persistence.open(None)

    @classmethod
    def teardown_class(cls):
        cls.persistence.close(None)

    def setup_method(self, method):
        self.persistence.clear(None)

    def test_crud_operations(self):
        self.fixture.test_crud_operations()

    def test_get_with_filter(self):
        self.fixture.test_get_with_filter()