FROM python:3.6
RUN git clone https://github.com/awslabs/git-secrets
RUN cd git-secrets && make install

COPY --from=bbvalabsci/buildbot-washer-worker:latest /washer /washer
CMD ["/washer/entrypoint.sh"]
