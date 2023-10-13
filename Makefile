include .env


run-dev:
	@python -m uvicorn main:app --host ${SERVER_HOST} --port ${SERVER_PORT} --reload

run:
	@python -m uvicorn main:app --host ${SERVER_HOST} --port ${SERVER_PORT}

