Docker Management API
====================

This application is for Managing the Docker using Flask API's.

Installing
----------

Python3 is prerequisite

.. code-block:: text

    pip install -r requirements.txt
    export FLASK_APP=app.py

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
    