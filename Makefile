.PHONY: all build clean install run

EXEC_NAME := pck3r

all: build

build:
	cp main.py $(EXEC_NAME)
	chmod +x $(EXEC_NAME)

clean:
	rm -f $(EXEC_NAME)

install: build
	sudo cp README.md /bin/pck3r-help
	sudo install -m 755 $(EXEC_NAME) /usr/local/bin/$(BINARY_NAME)

run:
	python3 main.py --help
