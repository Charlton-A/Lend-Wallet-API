# Lend Wallet API

## Structure

```bash
.
├── apps
│   ├── api
│   │   ├── api_v1.py
│   │   ├── __init__.py
│   │   └── views
│   │       ├── auth.py
│   │       ├── filter.py
│   │       ├── ping.py
│   │       └── profile.py
│   ├── __init__.py
│   └── ui
├── conf
│   ├── config.py
│   └── __init__.py
├── docker-compose.yml
├── Dockerfile
├── init.sh
├── Makefile
├── manage.py
├── middleware
│   └── token.py
├── models
│   ├── __init__.py
│   ├── mixin.py
│   ├── transaction.py
│   ├── user.py
│   └── wallet.py
├── pytest.ini
├── README.md
├── requirements.txt
└── tests
```

## Description

This repo is an implementaion of wallet API to fetch user profile and recent transactions on one end point.
The other end point filters transactions based on start date and end date

# API Endpoints

| METHOD |       ENDPOINT       |                     DESCRIPTION |
| ------ | :------------------: | ------------------------------: |
| GET    |     /api/v1/ping     |      Ping to check if API is up |
| GET    |   /api/v1/profile    | Get data to display on Screen 2 |
| GET    | / api/v1/filter/date | Get data to display on screen 3 |

[There is postman collection file](/postman-collection/lend-wallet-postman-collection.json)

## Getting Started

[The docker-compose file](docker-compose.yml) contains the components needed to the services.
In the root project directory, boot up the services in the docker compose file using .This will also seed the database.
Ensure ports 8003,5432(postgres) and 8077 are not in use

```shell
docker-compose up
```

# Running Tests

Python 3.9+ is required\
While still in the root directory of the project. You can create a virtual environment in the folder using

```shell
 python{PYTHON_VERSION} -m venv lend
```

You can activate the environment using

```shell
source lend/bin/activate
```

To install depenndencies.

```shell
(venv) make init
```

To run unit tests

```shell
(venv)  make unit_tests
```

To run integration tests ensure all the services are running then run.

```shell
(venv)  make integration_tests
```

To run all tests with coverage report .

```shell
(venv)  make all_tests
```

### Assumtions

A user can only have one wallet
