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
uvicorn main:app --reload
```

## Run the test suite
```sh
python test_runner.py
```

## API docs
access `/docs` to api docs.

## Steps to deploy this app in the cloud
-


## Necessary improvements
- Run observers in different worker
- improve `get_stats` testing; possibly creating different `UseCase`
- restric `ALLOWED_HOSTS`
- return endpoints description in `/`
- redirect `302` when get `/{short_code}` through browser
- regognize url posted twice and return same code
- add more character options to `short_code` string
