"""
Sample beacons microservice in Python
----------------------

This is a sample beacons microservice that stores information about RFID beacons and calculates positions.

Links
`````

* `development version <https://github.com/pip-services4-samples/pip-services4-samples-python/tree/main/service-beacons-python>`

"""

from setuptools import find_packages
from setuptools import setup

try:
    readme = open('README.md').read()
except:
    readme = __doc__

setup(
    name='service_beacons_python',
    version='1.0.0',
    url='https://github.com/pip-services4-samples/pip-services4-samples-python/tree/main/service-beacons-python',
    license='MIT',
    author='Conceptual Vision Consulting LLC',
    author_email='seroukhov@gmail.com',
    description='Sample Beacons microservice in Python',
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['config', 'data', 'test']),
    include_package_data=True,
    zip_safe=True,
    platforms='any',
        install_requires=[
        'pip-services4-commons>=0.0.0',
        'pip-services4-components>=0.0.0',
        'pip-services4-config>=0.0.0',
        'pip-services4-container>=0.0.0',
        'pip-services4-data>=0.0.0',
        'pip-services4-rpc>=0.0.0',
        'pip-services4-http>=0.0.0',
        'pip-services4-persistence>=0.0.0',
        'pip-services4-mongodb>=0.0.0',
        'pip-services4-swagger>=0.0.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
