FROM bbvalabsci/buildbot-washer-worker:latest
RUN apk update && apk upgrade && apk add --no-cache git
RUN touch notasks.py
CMD ["/washer/entrypoint.sh", "notasks.py"]
