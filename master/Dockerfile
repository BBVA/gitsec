FROM python:3.6
RUN mkdir /gitsec
WORKDIR /gitsec
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY master.cfg buildbot.tac ./
CMD ["buildbot", "start", "--nodaemon"]
