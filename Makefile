.PHONY: help up down logs ps test lint clean

help:
	@echo "up     - demarre la stack"
	@echo "down   - arrete la stack"
	@echo "logs   - affiche les logs"
	@echo "ps     - etat des services"
	@echo "test   - lance les tests"
	@echo "lint   - verifie le code"
	@echo "clean  - supprime les volumes"

up:
	docker compose -f docker/docker-compose.yml up -d

down:
	docker compose -f docker/docker-compose.yml down

logs:
	docker compose -f docker/docker-compose.yml logs -f

ps:
	docker compose -f docker/docker-compose.yml ps

test:
	pytest tests/ -v

lint:
	ruff check src/ tests/

clean:
	docker compose -f docker/docker-compose.yml down -v
