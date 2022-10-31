test:
	cd model_registry && cargo test
	pytest ./tests

check:
	flake8 ./gnn_lib

types:
	mypy ./gnn_lib
