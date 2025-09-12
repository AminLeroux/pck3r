.PHONY: all build clean install run

EXEC_NAME := pck3r
INSTALL_PATH :="/usr/local/bin/"

all: build

build:
	cp main.py $(EXEC_NAME)
	chmod +x $(EXEC_NAME)

clean:
	rm -f $(EXEC_NAME)

install: build
	
	sudo rm -rf /bin/pck3r*
	sudo mkdir -p $(INSTALL_PATH)
	sudo cp -rf . $(INSTALL_PATH)
	sudo cp README.md /bin/pck3r-help
	sudo install -m 755 $(EXEC_NAME) $(INSTALL_PATH)$(BINARY_NAME)
	sudo ln -s $(INSTALL_PATH)main.py /bin/pck3r
run:
	python3 main.py --help
