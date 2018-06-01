FROM alpine
RUN wget -O git-hound https://github.com/ezekg/git-hound/releases/download/0.6.2/git-hound_linux_amd64 && chmod +x git-hound

COPY --from=bbvalabsci/buildbot-washer-worker:latest /washer /washer
CMD ["/washer/entrypoint.sh"]
