##-----------------------------LICENSE NOTICE------------------------------------
##  CPCReady: SDK for programming in Locomotive Amstrad Basic and Basic Compiled
##            with Ugbasic (https://ugbasic.iwashere.eu/)
##
##  Copyright (C) 2023 destroyer
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU Lesser General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU Lesser General Public License for more details.
##
##  You should have received a copy of the GNU Lesser General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##------------------------------------------------------------------------------

PROJECT_CFG = cfg/project.cfg
EMULATORS_CFG = cfg/emulators.cfg
EMULATOR = WEB6128

all: build

.PHONY: read-project-config
read-project-config:
	@if [ -f $(PROJECT_CFG) ]; then \
		MODEL=$$(awk -F'=' '/model/{print $$2}' $(PROJECT_CFG)); \
		NAME=$$(awk -F'=' '/name/{print $$2}' $(PROJECT_CFG)); \
    else \
		echo "El archivo $(PROJECT_CFG) no existe."; \
		exit 1; \
    fi

.PHONY: build
build: read-project-config
	@cpcr build

.PHONY: check-emulators-config
check-emulators-config:
	@if [ ! -f $(EMULATORS_CFG) ]; then \
		echo "El archivo $(EMULATORS_CFG) no existe."; \
        exit 1; \
 	fi

.PHONY: run
run: check-emulators-config
	@cpcr run --setting $(EMULATOR)