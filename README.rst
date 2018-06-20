gitsec
======

gitsec is an *automated secret discovery service* for **git** that helps you
detect sensitive data leaks.

.. image:: https://raw.githubusercontent.com/BBVA/gitsec/develop/docs/_static/logo-small.png
    :target: http://gitsec.readthedocs.org/


Architecture
------------

gitsec is build upon *buildbot* and *buildbot-washer* therefore inheriting
their architecture.


Workflow
--------


The **master** runs on a *docker* container and spawns **workers** in new
containers as needed.

**Workers** are *buildbot-washer* tasks. You can check the ready-to-use plugins
in the section below.


Plugins
-------

=============== ================================= ================
Project         Image                             Summary
=============== ================================= ================
api-key-detect  bbvalabsci/gitsec-api-key-detect
git-hound       bbvalabsci/gitsec-git-hound
git-secrets     bbvalabsci/gitsec-git-secrets
gittyleaks      bbvalabsci/gitsec-gittyleaks
trufflehog      bbvalabsci/gitsec-trufflehog
=============== ================================= ================


Usage
-----


Server Deployment
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run -ti -v/var/run/docker.sock:/var/run/docker.sock  -p8010:8010 -p9989:9989 bbvalabsci/gitsec


Server Configuration
~~~~~~~~~~~~~~~~~~~~

Server is configured with environment variables only. This is a list of
variables you can customize to fit your needs.

========================= ============================= =====================================
Variable                  Default                       Description
========================= ============================= =====================================
DOCKER_HOST               "unix://var/run/docker.sock"  URI of the docker
                                                        daemon gitsec will use to spawn new
                                                        workers.
WORKER_IMAGE_AUTOPULL     True                          Pull the docker images
                                                        of needed plugins at runtime when
                                                        the are needed.
WORKER_INSTANCES          16                            Maximum number of parallel tasks.
WORKER_IMAGE_WHITELIST    "*"                           Comma separated list of shell-like
                                                        expressions defining the allowed
                                                        docker images.
BUILDBOT_WORKER_PORT      9989                          Port used for master<->worker
                                                        communication.
BUILDBOT_WEB_URL          "http://localhost:8010/"      Web UI absolute URL.
BUILDBOT_WEB_PORT         8010                          Port the webserver to bind to.
BUILDBOT_WEB_HOST         "localhost"                   Address the webserver to bind to.
BUILDBOT_DB_URL           "sqlite://"                   Database URI in SQLAlchemy format.
ENABLE_GITHUB_HOOK        "on"                          Enable Github webhook integration.
GITHUB_HOOK_SECRET        -                             Github webhook secret token.
ENABLE_BITBUCKET_HOOK     "on"                          Enable Bitbucket webhook integration.
GITSEC_SERVER_CONFIG      None                          When this file is
                                                        provided the server will run the set
                                                        of defined plugins independently of the 
                                                        user config.
========================= ============================= =====================================


I've just committed a secret! How I fix it??
--------------------------------------------

https://help.github.com/articles/removing-sensitive-data-from-a-repository/
