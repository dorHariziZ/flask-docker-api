PROJECT_NAME = flask-docker-api
PYTHON = python3
VENV_DIR = venv
PORT = 5003
DOCKER_TAG = latest


setup:
	@source pip install --upgrade pip
	@source pip install -r requirements.txt
	@echo "Dependencies installed!"

run_server_v1:
	@echo "Starting Flask server on port $(PORT)..."
	@source $(VENV_DIR)/bin/activate && $(PYTHON) server_v1.py

run_server_v2:
	@echo "Starting Flask server on port $(PORT)..."
	@source $(VENV_DIR)/bin/activate && $(PYTHON) server_v2.py


docker-build:
	@echo "Building Docker image..."
	docker build -t $(PROJECT_NAME) .
	@echo "Tagging Docker image with '$(DOCKER_TAG)'..."
	docker tag $(PROJECT_NAME) $(PROJECT_NAME):$(DOCKER_TAG)
	@echo "Docker image tagged as '$(PROJECT_NAME):$(DOCKER_TAG)'"
	@echo "Running Docker container..."
	docker run -p $(PORT):$(PORT) $(PROJECT_NAME)

docker-stop:
	@echo "Stopping all running containers..."
	@docker stop $$(docker ps -q) || true

docker-clean:
	@echo "Removing all stopped containers..."
	@docker rm $$(docker ps -a -q) || true

clean:
	@echo "Cleaning up the virtual environment..."
	@rm -rf $(VENV_DIR)

clean-all: clean docker-stop docker-clean
	@echo "Full cleanup completed!"
