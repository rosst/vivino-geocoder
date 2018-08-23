FROM python:3.6.6-slim-jessie

ENV PYTHONPATH .

COPY requirements.txt /

RUN pip install -U pip

RUN pip install --trusted-host pypi.python.org -r /requirements.txt

ENV FLASK_APP vivino.web_app.map.py 

EXPOSE 5000

COPY . . 

WORKDIR . 

#https://github.com/moby/moby/issues/21650
ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]
