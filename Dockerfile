FROM python:3.8.0-alpine
RUN apk add gcc libc-dev make

RUN mkdir /app
WORKDIR /app

COPY . /app
COPY settings.example.ini settings.ini

RUN pip install -r requirements/dev.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9099"]
