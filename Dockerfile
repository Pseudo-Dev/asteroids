FROM python:slim-buster
# FROM python:buster

RUN apt-get update -y
RUN apt-get --no-install-recommends install tk -y
RUN apt-get --no-install-recommends install syslog-ng -y

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "./start.sh" ]