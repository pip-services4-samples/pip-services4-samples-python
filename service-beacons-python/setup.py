"""
Sample data microservice in Python
----------------------

This is a sample data microservice that stores and retries generic entities. This microservice shall be used
as a template to create general purpose data microservices.

Links
`````

* `development version <https://bitbucket.org/entinco/eic-templates-services-python/src/master/service-data-pipservices>`

"""

from setuptools import find_packages
from setuptools import setup

try:
    readme = open('readme.md').read()
except:
    readme = __doc__

setup(
    name='service_beacons_python',
    version='1.0.1',
    url='https://bitbucket.org/entinco/eic-templates-services-python/src/master/service-cruddata-pipservices',
    license='Commercial',
    author='Conceptual Vision Consulting LLC',
    author_email='seroukhov@gmail.com',
    description='Communication components for Pip.Services in Python',
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=['config', 'data', 'test']),
    include_package_data=True,
    zip_safe=True,
    platforms='any',
        install_requires=[
        'pip-services4-aws>=0.0.0',
        'pip-services4-azure>=0.0.0',
        'pip-services4-commons>=0.0.0',
        'pip-services4-components>=0.0.0',
        'pip-services4-config>=0.0.0',
        'pip-services4-container>=0.0.0',
        'pip-services4-data>=0.0.0',
        'pip-services4-datadog>=0.0.0',
        'pip-services4-elasticsearch>=0.0.0',
        'pip-services4-gcp>=0.0.0',
        'pip-services4-grpc>=0.0.0',
        'pip-services4-http>=0.0.0',
        'pip-services4-mongodb>=0.0.0',
        'pip-services4-persistence>=0.0.0',
        'pip-services4-prometheus>=0.0.0',
        'pip-services4-rpc>=0.0.0',
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
