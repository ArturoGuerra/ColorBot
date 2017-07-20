FROM ubuntu:16.04
RUN apt update
RUN apt install -y software-properties-common python-software-properties
RUN add-apt-repository -y ppa:jonathonf/python-3.6
RUN apt update
RUN apt -y install python3.6 python3-pip python3.6-dev python3.6-venv git libffi-dev libopus-dev libsodium-dev ffmpeg
ADD . ./bot
WORKDIR /bot
RUN python3.6 -m venv /venv
RUN /venv/bin/pip install pip --upgrade
RUN /venv/bin/pip install -r requirements.txt
ENV TOKEN=0
ENV SERVER=0
ENV ROLE=0
ENTRYPOINT ["/venv/bin/python colorbot.py", "$TOKEN", "$SERVER", "$ROLE"]
