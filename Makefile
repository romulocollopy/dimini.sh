PROJECT_NAME=diminish
TAG=latest
DOCKERFILE=./ops/Dockerfile
DOCKER_COMPOSE=docker-compose -f ./ops/docker-compose.yaml -p ${PROJECT_NAME}
DOCKER_COMPOSE_RUN=${DOCKER_COMPOSE} run --rm
DOCKER_COMPOSE_DEV=${DOCKER_COMPOSE} -f ./ops/docker-compose.dev.yaml
DOCKER_COMPOSE_DEV_RUN=${DOCKER_COMPOSE_DEV} run --rm
UI_DIR=public/
UI_PORT=8000

test:
	${DOCKER_COMPOSE_DEV_RUN} --entrypoint="" app python test_runner.py

bash:
	${DOCKER_COMPOSE_DEV_RUN} --entrypoint="" app bash

run:
	${DOCKER_COMPOSE_DEV_RUN} --service-ports app

run-uwsgi:
	${DOCKER_COMPOSE_RUN} --service-ports app

compose-up:
	${DOCKER_COMPOSE} up -d

compose-down:
	${DOCKER_COMPOSE} down

compose-build:
	${DOCKER_COMPOSE} build

build:
	docker build -f ${DOCKERFILE} . -t ${PROJECT_NAME}:${TAG}


provision: provision-docker provision-user provision-repo

provision-docker:
	ansible-playbook \
		-i ./ops/ansible/inventories/hosts.yaml \
		./ops/ansible/playbooks/docker-install.yaml -vv
provision-user:
	ansible-playbook \
		-i ./ops/ansible/inventories/hosts.yaml \
		./ops/ansible/playbooks/create-user.yaml -vv
provision-repo:
	ansible-playbook \
		-i ./ops/ansible/inventories/hosts.yaml \
		./ops/ansible/playbooks/clone-repo.yaml -vv

deploy: provision-repo
	ansible-playbook \
		-i ./ops/ansible/inventories/hosts.yaml \
		./ops/ansible/playbooks/run-app.yaml -vv
