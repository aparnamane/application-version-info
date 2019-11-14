# Application Version Information Services
  The `application_version_info` is developed with Python, Docker and Travis CI

## Table of Contents
  - [Introduction](#introduction)
    - [Python3](#python3)
    - [Docker Image Build](docker-image-build)

## Introduction

This repository builds containerised application as a single deployable artifact along with all the dependencies.
This simple application provides detailed versioning information with single endpoint `/version`.

### Python3

This application is written in Python utilising python version 3.8.0.

### Docker Image Build

This image uses python:alpine as base image for thin size and install requird packages along with copying application code. 
Dockerfile is [here](Dockerfile).

Stages:

- 