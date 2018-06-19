FROM python:2.7
RUN git clone https://github.com/daylen/api-key-detect.git

COPY --from=bbvalabsci/buildbot-washer-worker:latest /washer /washer
COPY tasks.py /washer/

ENTRYPOINT ["/washer/entrypoint.sh"]
CMD ["/washer/tasks.py"]
