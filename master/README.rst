docker build . -t gitsec
#docker run -ti -v/var/run/docker.sock:/var/run/docker.sock  -p8010:8010 -p9989:9989 --rm gitsec
docker run -ti -v/var/run/docker.sock:/var/run/docker.sock  -p8010:8010 -p9989:9989 -v`pwd`/server.yml:/tmp/server.yml -eGITSEC_SERVER_CONFIG=/tmp/server.yml --rm gitsec
