FROM python:3.9.5

LABEL version=0.0.1

ENV ENV /root/.profile
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get upgrade -y && pip install --upgrade pip
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install  --no-cache-dir -r requirements.txt
ADD . /app

ARG PORT=5000
EXPOSE $PORT
ENV FLASK_PORT $PORT

CMD ["/app/run_app.sh"]
