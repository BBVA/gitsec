FROM python:2.7
RUN git clone https://github.com/daylen/api-key-detect.git

COPY --from=bbvalabsci/buildbot-washer-worker:latest /washer /washer
CMD ["/washer/entrypoint.sh"]
