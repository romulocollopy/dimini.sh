from python:3.8.0-alpine

RUN mkdir /app
COPY . /app
COPY settings.example.ini settings.ini
WORKDIR /app

RUN pip install -r requirements/dev.txt

CMD ["uvicorn", "main:app", "--port", "9099"]
