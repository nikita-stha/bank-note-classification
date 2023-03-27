# Bank Note Classification
This is a simple data science project for Bank note classification

## Demo


## System Requirements
- Python3
- [Link to Colab Notebook for the model used.](https://colab.research.google.com/drive/1MhKcqBe4PVMA-Dxi8J2r6W1XNJeScu4X?usp=sharing)
- Docker for local ( development & deployent)
- Docker-compose

## Quickstart Guide for Local Development

1. First clone this repository through 

`https://github.com/nikita-stha/bank-note-classification.git`

2. Run`cd bank-note-classification`

3. Run `cp .env.example .env.dev`

4. Run `chmod 755 services/web/entrypoint.sh` to resolve permission issues.

5. Run `docker-compose up -d --build` to build and run the container

6. Run `docker-compose down --remove-orphans` to shut down the container.

You can access web application on: http://localhost:5000/

## Quickstart Guide for Local Deployment

1. Run `cp .env.example .env.prod`

2. Run `chmod 755 services/web/entrypoint.prod.sh` to resolve permission issues.

3. Run `docker-compose -f docker-compose.prod.yml up -d --build` to build and run the container

4. To shut down running container, run `docker-compose down --remove-orphans`
You can access web application on: http://localhost:1337/
