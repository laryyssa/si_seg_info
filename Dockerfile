FROM python:3.9.16

RUN apt-get update && \
    apt-get install -y postgresql-client-13

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app app
COPY run.py .

EXPOSE 5000

CMD [ "python", "run.py"]