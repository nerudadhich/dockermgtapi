Docker Management API
====================

This application is for Managing the Docker using Flask API's.

Installing
----------

Configuration of Docker used by this app

    client = docker.from_env()   => (active)

    client = docker.DockerClient(base_url='unix://var/run/docker.sock') => (can active by uncommenting the line in app.py)
    
    client = docker.DockerClient(base_url='tcp://127.0.0.1:1234') => (can active by uncommenting the line in app.py)

Python3 is prerequisite

.. code-block:: text

    pip install -r requirements.txt
    export FLASK_APP=app.py
    flask run

To start in debug mode

.. code-block:: text

    export FLASK_DEBUG=1

API Details
----------------

.. code-block:: text

    GET /container/list
    GET /image/list
    GET /network/list
    GET /volume/list

Code Coverage Details
---------------------

.. code-block:: text

    coverage run -m pytest
    coverage report resources/*.py
    