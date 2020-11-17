FROM python:alpine

ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=server.py

ENV GREETING "Hello, world"


COPY requirements.txt .
RUN pip install -r requirements.txt
COPY server.py .
CMD [ "flask", "run", "--host=0.0.0.0", "--port=80" ]
