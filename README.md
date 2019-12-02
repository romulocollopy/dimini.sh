# Dimini.sh


## requirements
python 3.7+


## Install locally
```sh
git clone git@github.com:romulocollopy/dimini.sh
cd dimini.sh
python -m venv venv
source venv/bin/activate
pip install -r requirements/dev.txt
```


## Run locally
```sh
uvicorn main:app --reload --port 9099
```
or

```sh
docker-compose up
```
and access `http://0.0.0.0:9099/`


## Run the test suite
```sh
python test_runner.py
```
or
```sh
docker-compose run tests
```

## API docs
and access `http://0.0.0.0:9099/docs`


## Steps to deploy this app in the cloud
- mount database volume for persistence
- create k8s yaml files
- configure vault for database password
- expose uvicorn though reverse proxy
- configue secure conection


## Necessary improvements
- Run observers in different worker (use message queue maybe)
- improve `get_stats` testing; possibly creating different `UseCase`
- restric `ALLOWED_HOSTS`
- return endpoints description in `/`
- redirect `302` when get `/{short_code}` through browser
- recognize url posted twice and return same code
- add more character options to `short_code` string
