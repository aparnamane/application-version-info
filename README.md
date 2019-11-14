# Application Version Information Services
  The `application_version_info` is developed with Python, Docker and Travis CI

## Table of Contents
  - [Introduction](#introduction)
    - [Python3](#python3)
    - [Docker Image Build](docker-image-build)
    - [TravisCI](#travisci)
    - [GitHub](#github)
  - [Build with TravisCI](#build-with-travisci)
  - [Build Locally](#build-locally)
    - [Prerequisite](#prerequisite)
    - [Build](#build)
    - [Test](#test)
    - [Push](#push)
  - [Enhancement Production Readiness](#enhancement production-Readiness)

## Introduction

This repository builds containerised application as a single deployable artifact along with all the dependencies.
This simple application provides detailed versioning information with single endpoint `/version`.

### Python3

This application is written in Python utilising python version 3.8.0.

### Docker Image Build

This image uses python:alpine as base image for thin size and install required packages along with copying application code. 
Dockerfile is [here](Dockerfile).

Image Build:

- Install required packages and 
- Copy the source code
- Build the image

### TravisCI

TravisCI pipeline is [here] `.travis.yml` file [here](.travis.yml) which conatins three stages as:

- Build: Build the containerised application image and will run for all the branches
- Test: This will test by hitting API endpoint to get expected results in JSON   format and also stage will run for all the branches.
- Push: Once the Test stage is completed successfully Push stage will run to push the final image to docker repository. This stage will run for only `master` branch.
`This stage need to access docker repository to push the image, so need to set docker login credentials as environment variables.`

### GitHub

All the application code along with CI pipeline sits in GitHub repo which will allow TravisCI to auto build for each and every commit.

## Build with TravisCI

- Login to `https://travis-ci.com` with GitHub login details and from settings a lclick to `Manage repositories on GitHub` and select the repository to Approve and Install TravisCI.
- Once the TravisCI is installed for the repository, it will build for every push commit by running all stages in pipeline [here] `.travis.yml`.

## Build Locally

### Build and Run application locally

## Prerequisite

- python3
- docker
- docker-compose
- git

## Build

Clone the git repo locally.

`git clone git@github.com:aparnamane/application-version-info.git`

Change directory to the application directory

`cd application-version-info`

Build the image

`docker-compose build`

This will build the application image with `aparnamane/app-version-info:abc57858585` tag.

`As in the above command commit SHA is the static value from the `.env` file while running locally, but when run by TravisCI the file will be overwrite the commit SHA with actual last git commit SHA.`

## Test

Run the container using the image

`docker run -d --name=aplication_version_info -p 5000:5000 aparnamane/app-version-info:abc57858585`

Check the container is running

`docker ps`

Test the application with API call using `curl`

`docker exec aplication_version_info curl -i http://0.0.0.0:5000/application-version-info/api/v1.0/version`

This should get response in JSON format as:

``` 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   157  100   157    0     0  78500      0 --:--:-- --:--:-- --:--:-- 78500
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 157
Server: Werkzeug/0.16.0 Python/3.8.0
Date: Thu, 14 Nov 2019 04:40:48 GMT

{
  "myapplication": [
    {
      "description": "pre-interview technical test", 
      "lastcommitsha": "abc57858585", 
      "version": "1.0"
    }
  ]
}

```

## Push

Login to docker registry before pushing the image.

Push the image to the image registry

`docker-compose push`


### Enhancement/Production Readiness

To deploy the application in production/production like environment following statergies need to be considered.

- Use certified image by security team.
- Branching statergy need to implement.
- Deployment statergy need implement.
- Use third party tools for authentication, identity management.
- CI/CD tool should be managed internally.
- User should provided limited/previlaged access for all tools.
- Aplication packages and images should be saved and extracted from private repositories.


