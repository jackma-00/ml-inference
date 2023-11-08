AWS_ACCOUNT ?= 403097528197
AWS_REGION ?= eu-north-1

IMAGE ?= $(AWS_ACCOUNT).dkr.ecr.$(AWS_REGION).amazonaws.com/ml-inference-images-repo
IMAGE_TAG ?= latest

.PHONY: venv install format lint test local_launch build run

venv:
	python3 -m venv .venv

install: setup.py
	. ./.venv/bin/activate && \
	pip install --upgrade pip &&\
	pip install .[dev]

format:
	. ./.venv/bin/activate && \
	black .

lint: venv install
	. ./.venv/bin/activate && \
	black --check . && \
	pylint -j 0 --disable=C,W ./inference/

test: venv install
	. ./.venv/bin/activate && \
	pytest .

# Unzipped size must be smaller than 262144000 bytes
zip: venv install
	cd .venv/lib/python3.10/site-packages && \
	zip -r ../../../../my_deployment_package.zip . && \
	cd ../../../../inference && \
	zip -r my_deployment_package.zip .

# Unzipped size must be smaller than 262144000 bytes
layer: venv install 
	cd .venv && \
	zip -r ../layer.zip ./bin && \
	zip -r ../layer.zip ./lib 

build:
	docker build --tag $(IMAGE):$(IMAGE_TAG) .

push:
	docker push $(IMAGE):$(IMAGE_TAG)

# This command is only for development purposes
run:
	docker run --rm $(IMAGE):$(IMAGE_TAG)



