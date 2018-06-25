gitsec
======

gitsec is an *automated secret discovery service* for **git** that helps you
detect sensitive data leaks.

gitsec doesn't directly detect sensitive data but uses already available open
source tools with this pourpose and provides a unified framework to run them
easily.

.. image:: https://raw.githubusercontent.com/BBVA/gitsec/develop/docs/_static/logo-small.png
    :target: http://gitsec.readthedocs.org/


Architecture
------------

gitsec is build upon buildbot_ and buildbot-washer_ therefore inheriting their
architecture.

Master processes receive code changes from git repositories.
When a change is detected, workers are spawned to run the defined plugins on
the configuration file(s).

The **master** process runs on a *docker* container and spawns **workers** in
new containers as needed. The master process is a regular *buildbot* master
with gitsec's specific configuration. Worker processes are *buildbot* worker
processes with an specific *buildbot-washer* task registered.


Plugins
-------

=============== =================================== ===========================================
Project         Image                               Summary
=============== =================================== ===========================================
api-key-detect_ `bbvalabsci/gitsec-api-key-detect`_ Scan a codebase for API keys and passwords
git-hound_      `bbvalabsci/gitsec-git-hound`_      Git plugin that prevents sensitive data
                                                    from being committed
git-secrets_    `bbvalabsci/gitsec-git-secrets`_    Prevents you from committing secrets and
                                                    credentials into git repositories
gittyleaks_     `bbvalabsci/gitsec-gittyleaks`_     Find sensitive information for a git repo
trufflehog_     `bbvalabsci/gitsec-trufflehog`_     Searches through git repositories for
                                                    high entropy strings and secrets, digging
                                                    deep into commit history
=============== =================================== ===========================================


Usage
-----

In order to use **gitsec** you must follow these steps:

#. Configure and deploy a master.
#. Configure your a GitHub's repository or organization webhooks.
#. Add a *.gitsec.yml* configuration file to your project.


Master Deployment
~~~~~~~~~~~~~~~~~

You can run the gitsec master process with docker this way:

.. code-block:: bash

   docker run -ti -v/var/run/docker.sock:/var/run/docker.sock -p8010:8010 -p9989:9989 bbvalabsci/gitsec


Master Configuration
~~~~~~~~~~~~~~~~~~~~

Master configuration documentation `is available here`_.


Github Webhook Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can set a Github webhook to trigger a *gitsec* analysis for a particular
repository or for all the repositories in an organization.

Follow `this guide`_ to add the webhook.

You should set a strong *secret* to the webhook, remember to pass the secret to
your master using the **GITHUB_HOOK_SECRET** variable.

The endpoint to point to shall be "http://YOUR-HOST-AND-POR-HERE/change_hook/github".



Configuration File Format
-------------------------

gitsec configuration file define the list of plugins to run for each source
code change.

Two configuration files may be defined: one in the server, another in the users
repository. The former, if present, is managed by the owner of the gitsec
service and contains the list of plugins that must always run for a code
change. The latest is managed by the source code repository owners and contains
an extra list of plugins and configuration.

This way a list of plugins may be enforced by the gitsec service owner and, at
the same time, maintains flexibility for the developers to add their own checks.

The configuration file format is YAML.

This is an example of configuration file:


.. code-block:: yaml

    plugins:
        bbvalabsci/gitsec-git-secrets:
            options:
                prohibited:
                    password:
                        value: '^password:'
                        type: regex
        bbvalabsci/gitsec-api-key-detect:
            unimportant: yes
        bbvalabsci/gitsec-trufflehog:
        bbvalabsci/gitsec-gittyleaks:


- The *plugins* key contains the list of plugins. In the example 4 plugins are defined.

  - Each plugin section is defined by the name of the **docker image to run**.

    - The plugin section may contain the following keys:

      - *unimportant* (yes|no): If **yes** the failure of this plugin will not
        make the whole check to fail.

      - *options*: The parameter passed to the plugin. Depends on the
        plugin.


Create a New Plugin
-------------------

If you want to create a gitsec plugin for a tool of yours, or for any other
already available tool, follow the instructions `given here`_.

If you want your plugin to be part of gitsec distribution, please send a **pull
request** adding the plugin files in a directory under the `plugins` directory.


I've just committed a secret! How I fix it??
--------------------------------------------

https://help.github.com/articles/removing-sensitive-data-from-a-repository/


.. _api-key-detect: https://github.com/daylen/api-key-detect
.. _git-hound: https://github.com/ezekg/git-hound
.. _git-secrets: https://github.com/awslabs/git-secrets
.. _gittyleaks: https://hub.docker.com/r/bbvalabsci/gitsec-gittyleaks/
.. _trufflehog: https://github.com/dxa4481/truffleHog
.. _buildbot: https://buildbot.net
.. _buildbot-washer: https://github.com/BBVA/buildbot-washer/
.. _`bbvalabsci/gitsec-api-key-detect`: https://hub.docker.com/r/bbvalabsci/gitsec-api-key-detect/
.. _`bbvalabsci/gitsec-git-hound`: https://hub.docker.com/r/bbvalabsci/gitsec-git-hound/
.. _`bbvalabsci/gitsec-git-secrets`: https://hub.docker.com/r/bbvalabsci/gitsec-git-secrets/
.. _`bbvalabsci/gitsec-gittyleaks`: https://hub.docker.com/r/bbvalabsci/gitsec-gittyleaks/
.. _`bbvalabsci/gitsec-trufflehog`: https://hub.docker.com/r/bbvalabsci/gitsec-trufflehog/
.. _`this guide`: https://developer.github.com/webhooks/creating/#setting-up-a-webhook
.. _`given here`: https://github.com/BBVA/gitsec/tree/develop/plugins
.. _`is available here`: https://github.com/BBVA/gitsec/tree/develop/master
