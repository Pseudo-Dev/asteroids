FROM python:slim-buster

RUN apt-get update -y
RUN apt-get --no-install-recommends install tk -y

WORKDIR /usr/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "main.py" ]