FROM python:slim-buster

RUN apt-get update -y
RUN apt-get install tk -y

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]