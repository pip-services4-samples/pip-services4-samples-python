import sys

from pip_services4_container.container import ProcessContainer
from pip_services4_http.build.DefaultHttpFactory import DefaultHttpFactory
from pip_services4_swagger.build.DefaultSwaggerFactory import DefaultSwaggerFactory

from ..build.BeaconsServiceFactory import BeaconsServiceFactory

class BeaconsProcess(ProcessContainer):
    def __init__(self):
        super(BeaconsProcess, self).__init__('beacons', 'Beacons microservice')

        self._factories.add(BeaconsServiceFactory())
        self._factories.add(DefaultHttpFactory())
        self._factories.add(DefaultSwaggerFactory())

