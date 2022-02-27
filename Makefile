install:
	pip install -r requirements.txt
test:
	pytest -s
run:
	uvicorn app.main:app --reload
