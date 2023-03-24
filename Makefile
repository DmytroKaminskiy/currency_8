SHELL := /bin/bash

manage_py := docker exec -it backend python app/manage.py

manage:
	$(manage_py) $(COMMAND)

show_urls:
	$(manage_py) show_urls

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

shell:
	$(manage_py) shell_plus --print-sql

build:
	cp -n .env.example .env && docker-compose up -d --build

build_and_run: build \
	makemigrations \
	migrate \
	run

pytest:
	docker exec -it backend pytest app/tests/

coverage:
	docker exec -it backend pytest --cov=app app/tests/ --cov-report html && docker exec -it backend coverage report --fail-under=79.0000

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"
