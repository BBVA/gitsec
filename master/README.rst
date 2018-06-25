Master Configuration
====================

Master is configured with environment variables only. This is a list of
variables you can customize to fit your needs.

========================= ============================= =====================================
Variable                  Default                       Description
========================= ============================= =====================================
DOCKER_HOST               "unix://var/run/docker.sock"  URI of the docker
                                                        daemon gitsec shall use to spawn new
                                                        workers.
WORKER_IMAGE_AUTOPULL     "on"                          Pull the docker images
                                                        of defined plugins at runtime when
                                                        if needed.
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
GITHUB_HOOK_SECRET                                      Github webhook secret token.
ENABLE_BITBUCKET_HOOK     "on"                          Enable Bitbucket webhook integration.
GITSEC_SERVER_CONFIG                                    When this file is
                                                        provided the server will run the set
                                                        of defined plugins independently of the 
                                                        user config.
GITSEC_WORKER_IMAGE       bbvalabsci/gitsec-worker      Worker image used to basic bootstrapping.
========================= ============================= =====================================


