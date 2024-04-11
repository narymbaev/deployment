postgres:
	docker run --name deployment --network deployment-network -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=root -d postgres

createdb:
	docker exec -it deployment createdb deployment -U root -O root

server:
	pipenv run python3 server/server.py

.PHONY: postgres createdb server