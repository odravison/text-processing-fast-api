PROJECT_NAME = text-processing-app

IMAGE_NAME = $(PROJECT_NAME):dev

.PHONY: build up down restart logs

# Builda a imagem Docker
build:
	docker build -t $(IMAGE_NAME) .

# Sobe os containers do Docker Compose (app + banco de dados)
up: build
	docker-compose up -d

# Para e remove os containers
down:
	docker-compose down

# Reinicia os containers
restart: down up

# Exibe os logs
logs:
	docker-compose logs -f

.PHONY: clean
clean:
	docker-compose down -v
	docker system prune -af

.PHONY: check-lint
check-lint: ## Check lint
	@echo "Running ruff lint"
	$(MAKE) --no-print-directory run-command-in-container \
	COMMAND="poetry run ruff check src/ tests/"
	@echo "Running ruff formatter"
	$(MAKE) --no-print-directory run-command-in-container \
	COMMAND="poetry run ruff format --check src/ tests/"

run-command-in-container:
	@docker run \
	--rm \
	$(if $(INTERACTIVE), -i, $("")) \
	-t \
	-v $(PWD)/src:/opt/text-processing-fast-api/src \
	-v $(PWD)/tests:/opt/text-processing-fast-api/tests \
	-v $(PWD)/poetry.lock:/opt/text-processing-fast-api/poetry.lock \
	-v $(PWD)/pyproject.toml:/opt/text-processing-fast-api/pyproject.toml \
	-v $(PWD)/.ruff_cache:/opt/text-processing-fast-api/.ruff_cache \
	$(if $(NETWORK), --network text-processing-fast-api, $("")) \
	--env-file .env.local \
	$(IMAGE_NAME) \
	$(COMMAND)
