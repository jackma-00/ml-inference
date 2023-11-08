# Deploying ML Models as Serverless Functions

This repository deploys an ML Models as Serverless Functions. 

## Requirements

* Docker engine ([Installation](https://docs.docker.com/engine/install/))
* Python3.10.12 with `pip`
* AWS CLI v2 ([User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html))
* Amazon ECR credential helper ([Installation](https://github.com/awslabs/amazon-ecr-credential-helper))

## Quickstart

Set up your AWS console initializing:
* an ECR repository named `ml-inference-images-repo`
* Lambda function where to deploy the container image

Get valid AWS credential to push the Docker image to ECR. 

### Docker

To build the application and push it to ECR call the following make targets in subsequent order:
```shell
make build
make push
```

### Test The Application

Once the development Lambda function is updated with the new Docker image you can test the function form the AWS console.
