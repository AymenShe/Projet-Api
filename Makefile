.PHONY: start test

start:
	rm -f projet.db
	python3 init_db.py
	python3 seed_products.py
	python3 seed_stores.py
	uvicorn app.main:app --reload

start-frontend:
	cd frontend && npm install && npm run dev

test:
	python3 -m pytest
