#!/usr/bin/env bash
set -eu

envsubst < .github/ecspresso/"${ECS_ENV}"/template.yml > .github/ecspresso/"${ECS_ENV}"/config.yml
envsubst < .github/ecspresso/"${ECS_ENV}"/ecs-service-def.tpl > .github/ecspresso/"${ECS_ENV}"/ecs-service-def.json
envsubst < .github/ecspresso/"${ECS_ENV}"/ecs-task-def.tpl > .github/ecspresso/"${ECS_ENV}"/ecs-task-def.json

curl -OL https://github.com/kayac/ecspresso/releases/download/v1.1.2/ecspresso-v1.1.2-linux-amd64.zip
unzip ecspresso-v1.1.2-linux-amd64.zip
ln -s ./ecspresso-v1.1.2-linux-amd64 ./ecspresso

aws ecr get-login-password --region "${AWS_DEFAULT_REGION}" | docker login --username AWS --password-stdin "${ECR_REPOSITORY_URI}"

docker pull "${ECR_REPOSITORY_URI}":latest || true

DOCKER_BUILDKIT=1 docker build \
               --cache-from "${ECR_REPOSITORY_URI}":latest \
               --build-arg VERSION="${GITHUB_SHA}" \
               --build-arg BUILD="${ECS_ENV}_${GITHUB_SHA}" \
               -t "${ECR_REPOSITORY_URI}":"${GITHUB_SHA}" \
               -t "${ECR_REPOSITORY_URI}":latest \
               -f ./Dockerfile .

docker push "${ECR_REPOSITORY_URI}":"${GITHUB_SHA}"
docker push "${ECR_REPOSITORY_URI}":latest
