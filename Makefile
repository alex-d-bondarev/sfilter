.DEFAULT_GOAL := default

default:
	@echo "The following commands are supported:"
	@echo "test \t # Test the project"

test: sfilter pytest

sfilter:
	@echo "Run sfilter"

pytest:
	@echo "Run tests"
