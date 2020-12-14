# Test
Test for Red Points

### Prerequisites

Make sure that you have met the following prerequisites before continuing with this tutorial.

* Logged in as a user with sudo privileges or Admin user for MAC.
* Have [python 3](https://www.python.org/downloads/) installed
* have [virtualenv](https://virtualenv.pypa.io/en/latest/) installed

### Execute

Instructions for running the program
* Install
```ssh
  virtualenv test-crawler
```
* Install requirementes
```ssh
cd red-points/crawler
```
```ssh
  pip install -r requirements.txt
```

* Run
```ssh
  python3 pipline.py --p '{"keywords": ["python","django-rest-framework","jwt"],"type": "Repositories" }'
```
* Response
```ssh
  [{'url': 'https://github.com/always-awake/SideProject_4'},
 {'url': 'https://github.com/joaovictor1205/medicarAPI-Backend'},
 {'url': 'https://github.com/joaovictor1205/navedexAPI'},
 {'url': 'https://github.com/Firok/RestApp'},
 {'url': 'https://github.com/antonioxtasis/Django2_API'},
 {'url': 'https://github.com/danagar0312/heroku-hyle-proj'},
 {'url': 'https://github.com/Rabia23/DjangoRestJWTAuthentication'},
 {'url': 'https://github.com/vaibhavkollipara/ChatroomApi'},
 {'url': 'https://github.com/sdabhi23/django-hasura-jwt-auth'},
 {'url': 'https://github.com/zhaorch/shanks-vue'}]
```

## Running the tests

To run the testsL
* APP
```ssh
  pytest -v
```

## Project scaffolding

- crawler
    - pipline.py
        - pipline execution crawler
    - config
        - config files
    - pages_crawler
        - Code to execution el scraping
    - pytest.init
        - Test configuration
    - tests.py
        - file of tests
