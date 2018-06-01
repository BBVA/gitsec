.. warning::

   Work In Progress


gitsec plugins
==============

gitsec plugins are Docker containers providing three things:


#. The tool to be integrated with gitsec.

#. An adapter capable of configuring (if necessary) and launch the tool.

#. The buildbot-washer worker.


How to contribute
-----------------

If you've found a cool tool that you want be integrated with gitsec follow the
next instructions.


#. Make a fork of this repository.

#. Create a new subdirectory in this directory with the name of the tool in
lowercase, replacing space and underscores with hyphens.

#. Create a Dockerfile inside the new directory.

#. If the tool you want to integrate already has a docker image distribution
   you can extend it using the FROM construct.

#. If your tool has not a docker image distribution you can create your own
   from your favorite distribution. After that, install all the tools
   dependencies and the tool itself.

#. Add your adapter to the image. See below.

#. Copy the buildbot-washer worker. See below.


Adding your adapter
~~~~~~~~~~~~~~~~~~~

XXX

Add the environment variable WASHER_ENTRYPOINT pointing to the full path of
your adapter.


Coping the `buildbot-washer` worker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add these two lines at the end of your Dockerfile and you are ready to go!

.. code-block:: docker

   COPY --from=bbvalabsci/buildbot-washer-worker:latest /washer /washer
   CMD ["/washer/entrypoint.sh"]
