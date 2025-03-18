PROJECT_NAME = flask-docker-api
PYTHON = python3
VENV_DIR = venv
PORT = 5003
DOCKER_TAG = latest

.PHONY: docker-build docker-stop docker-clean

docker-build:
	@echo "Building Docker image..."
	docker build -t $(PROJECT_NAME) .
	@echo "Tagging Docker image with '$(DOCKER_TAG)'..."
	docker tag $(PROJECT_NAME) $(PROJECT_NAME):$(DOCKER_TAG)
	@echo "Docker image tagged as '$(PROJECT_NAME):$(DOCKER_TAG)'"
	@echo "Running Docker container..."
	docker run -d -p $(PORT):$(PORT) $(PROJECT_NAME)

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
