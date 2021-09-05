default: all

all: build up

# ==========
# interaction tasks
bash: up
	docker-compose exec app bash

python: up
	docker-compose exec app python

gremlin-console: up
	docker-compose run --rm gremlin-console

# ==========
# docker-compose aliases
up:
	docker-compose up -d app gremlin-server

ps images down:
	docker-compose $@

build:
	docker-compose build

build-no-cache:
	docker-compose build --no-cache

reup: down up

clean: clean-container

clean-container:
	docker-compose down --rmi all

