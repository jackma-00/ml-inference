# Deploying ML Models as Docker Containers

This repository deploys an ML Models as Docker Container. 

## Requirements

* Docker engine ([Installation](https://docs.docker.com/engine/install/))
* Python3.10.12 with `pip`

## Quickstart

To get the application up and running, run the make target: 
```shell
make compose 
```

### Local Environment

Initialize Python environment running the make target

```shell
make venv
. .venv/bin/activate
```

Install now the Python project's dependencies running the make target
```shell
make install
```

To run the application in your local environment call the make target
```shell
make local_launch
```

### Docker

To run the application with Docker call the following make targets in subsequent order:
```shell
make build
make run 
```
Alternatively you can leverage docker compose technology:
```shell
make compose 
```

### Test The Application

To test the application call the following make targets in subsequent order:
```shell
make format
make lint
make test
```
Once all the tests succeed you can run the application both in your local environment or in Docker and test with:
* Swagger: visit the URL http://127.0.0.1:8080/docs
* Postman: find [postman collection](https://github.com/jackma-00/ml-inference/blob/main/container/ML%20Inference.postman_collection.json)
