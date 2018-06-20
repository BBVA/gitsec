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

=============== =================================
Project         Image
=============== =================================
api-key-detect  bbvalabsci/gitsec-api-key-detect
git-hound       bbvalabsci/gitsec-git-hound
git-secrets     bbvalabsci/gitsec-git-secrets
gittyleaks      bbvalabsci/gitsec-gittyleaks
trufflehog      bbvalabsci/gitsec-trufflehog
=============== =================================


Usage
-----

Server Deployment
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   docker run -ti -v/var/run/docker.sock:/var/run/docker.sock  -p8010:8010 -p9989:9989 gitsec


Server Configuration
~~~~~~~~~~~~~~~~~~~~

Server is configured with environment variables only. This is a list of
variables you can customize to fit your needs.


========================= ============================= =====================================
Variable                  Default                       Description
========================= ============================= =====================================
DOCKER_HOST               "unix://var/run/docker.sock"  URI of the docker daemon gitsec will use to spawn new workers.
WORKER_IMAGE_AUTOPULL     True
WORKER_INSTANCES          16
WORKER_IMAGE_WHITELIST    "*"
BUILDBOT_MQ_URL           None
BUILDBOT_MQ_REALM         "buildbot"
BUILDBOT_MQ_DEBUG         False
BUILDBOT_WORKER_PORT      9989
BUILDBOT_WEB_URL          "http://localhost:8010/"
BUILDBOT_WEB_PORT         8010
BUILDBOT_WEB_HOST         "localhost"
BUILDBOT_DB_URL           "sqlite://"
ENABLE_GITHUB_HOOK        True
GITHUB_HOOK_SECRET        None
ENABLE_BITBUCKET_HOOK     True
GITSEC_SERVER_CONFIG      None
========================= ============================= =====================================


I've just committed a secret! How I fix it??
--------------------------------------------

https://help.github.com/articles/removing-sensitive-data-from-a-repository/
