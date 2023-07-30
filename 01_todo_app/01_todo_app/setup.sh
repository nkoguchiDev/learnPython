#!/bin/bash
echo DB_USER=root >.env
echo DB_PASSWORD=password >>.env
echo DB_HOST=localhost >>.env
echo DB_PORT=27017 >>.env


cp .env ./app

docker-compose up -d