.PHONY: deploy install update-dependencies

# Define variables
REMOTE_HOST = jilu3758@italica.o2switch.net
REMOTE_DIR = ~/test_python
VENV_DIR = /home/jilu3758/virtualenv/test_python/3.12/

deploy:
	cd vue_app && npm run build && \
	cp -r dist/* ../static/ && \
	ssh $(REMOTE_HOST) "cd $(REMOTE_DIR) && git pull origin main && make install && make update-dependencies && make restart-app"

install:
	test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)
	. $(VENV_DIR)/bin/activate && pip install -r requirements.txt

update-dependencies:
	. $(VENV_DIR)/bin/activate && pip install --upgrade -r requirements.txt

restart-app:
	touch tmp/restart.txt'

# restart-app:
# 	ssh $(REMOTE_HOST) 'cd $(REMOTE_DIR) && touch tmp/restart.txt'

