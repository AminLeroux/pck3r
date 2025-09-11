.PHONY: all build clean install run

BINARY_NAME := pck3r

all: build

build:
	cp main.py $(BINARY_NAME)
	chmod +x $(BINARY_NAME)

clean:
	rm -f $(BINARY_NAME)

install: build
	sudo cp README.md /bin/pck3r-help
	sudo install -m 755 $(BINARY_NAME) /usr/local/bin/$(BINARY_NAME)

run:
	python3 main.py --help
