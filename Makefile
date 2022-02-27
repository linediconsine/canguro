install:
	pip install -r requirements.txt
test:
	pytest
run:
	uvicorn app.main:app --reload
