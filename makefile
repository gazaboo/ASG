.PHONY: deploy install update-dependencies

# Define variables
REMOTE_HOST = jilu3758@italica.o2switch.net
REMOTE_DIR = ~/test_python
VENV_DIR = /home/jilu3758/virtualenv/test_python/3.12/

deploy:
	cd vue_app && rm -rf ./dist && npm run build && \
	rm -rf ../static/* && cp -r dist/* ../static/ && \
	ssh $(REMOTE_HOST) "cd $(REMOTE_DIR) && git pull origin main && make install && make update-dependencies && make restart-app"

local-run:
	cd vue_app && rm -rf ./dist && \
	npm run build && \
	rm -rf ../static/* && \
	cp -r dist/* ../static/ && \
	sudo docker compose up --build

install:
	test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)
	. $(VENV_DIR)/bin/activate && pip install -r requirements.txt

update-dependencies:
	. $(VENV_DIR)/bin/activate && pip install --upgrade -r requirements.txt

restart-app:
	touch tmp/restart.txt

setup-env:
	test -f .env || cp .env.example .env
	. $(VENV_DIR)/bin/activate && python -c "import secrets; print(f'SECRET_KEY={secrets.token_hex(16)}')" >> .env

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

test:
	. $(VENV_DIR)/bin/activate && python -m pytest

lint:
	. $(VENV_DIR)/bin/activate && flake8 .


