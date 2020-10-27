# Dimini.sh


## requirements
- python 3.7+
- docker
- docker-compose


## Install locally
```sh
git clone git@github.com:romulocollopy/dimini.sh
cd dimini.sh
python -m venv venv
source venv/bin/activate
pip install -r requirements/dev.txt
```


## Run on docker
```sh
make compose-dev
```
and access `http://0.0.0.0:8088/`


## Run the test suite
```sh
make test
```

## API docs
and access `http://0.0.0.0:8088/docs`


## Steps to deploy this app in the cloud
- mount database volume for persistence
- create k8s yaml files
- configure vault for database password


## Necessary improvements
- Run observers in different worker (use message queue maybe)
- improve `get_stats` testing; possibly creating different `UseCase`
- restric `ALLOWED_HOSTS`
- recognize url posted twice and return same code
- add more character options to `short_code` string
