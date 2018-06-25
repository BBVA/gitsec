Create a New Plugin
===================

A plugin is a *docker image* containing three things:

#. The buildbot worker.

#. The tool to run for detecting secrets.

#. The washer task. A python function to be executed by the worker in order to
   run the tool and translate the results.

The typical procedure to create a new plugin is the following.

#. Create a **Dockerfile** to build an image with the tool installed. Maybe the
   tool creator already provides one, if this is the case we only need to start
   from it.

   .. code-block:: dockerfile

      FROM myawesometool

#. Copy the buildbot-washer worker.

   .. code-block:: dockerfile

      FROM myawesometool
      COPY --from=bbvalabsci/buildbot-washer-worker:latest /washer /washer
      ENTRYPOINT ["/washer/entrypoint.sh"]

#. Create the tasks.py file and add it to the *docker image*.

   .. code-block:: python

      from subprocess import check_output
      from washer.worker.actions import CreateNamedLog, AppendToLog
      from washer.worker.commands import washertask
      
      @washertask
      def main(repopath, **kwargs):
          output = check_output(f"myawesometool {repopath}")
          if output:
              # Something found!
              yield CreateNamedLog("secrets")
              yield AppendToLog("secrets", output)
              return False  # Make the build FAIL
          else:
              # Nothing found, return SUCCESS
              return True


   Finally add the tasks file to the *Dockerfile* and set it as the
   default command.

   .. code-block:: dockerfile

      FROM myawesometool
      COPY --from=bbvalabsci/buildbot-washer-worker:latest /washer /washer
      COPY tasks.py /washer/
      ENTRYPOINT ["/washer/entrypoint.sh"]
      CMD ["/washer/tasks.py"]


At this point your plugin is ready to be build:

.. code-block:: bash

   docker build . -t myawesomeplugin


You can publish the image in your docker registry of preference.

After the plugin is published you can include it in the configuration file as
any other plugin.

You can check some examples in this directory.

If you build a plugin for a public tool don't hesitate to send a **pull request**.
