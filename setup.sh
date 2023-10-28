#!/bin/bash
##-----------------------------LICENSE NOTICE------------------------------------
##  CPCReady: Software Developer Kit for programming in Amstrad Basic and Ugbasic 
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

RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)
BLUE=$(tput setaf 4)
GRAY=$(tput setaf 8) 
NC=$(tput sgr0)  # No Color

VERSION=$(cat VERSION)
VERSION_RETROVIRTUALMACHINE="2.0.beta-1.r7"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PATH_INSTALL="$SCRIPT_DIR"

echo
echo "${YELLOW} ██████╗██████╗  ██████╗██████╗ ███████╗ █████╗ ██████╗ ██╗   ██╗${NC}"
echo "${YELLOW}██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝${NC}"
echo "${YELLOW}██║     ██████╔╝██║     ██████╔╝█████╗  ███████║██║  ██║ ╚████╔╝ ${NC}" 
echo "${YELLOW}██║     ██╔═══╝ ██║     ██╔══██╗██╔══╝  ██╔══██║██║  ██║  ╚██╔╝  ${NC}" 
echo "${YELLOW}╚██████╗██║     ╚██████╗██║  ██║███████╗██║  ██║██████╔╝   ██║   ${NC}" 
echo "${YELLOW} ╚═════╝╚═╝      ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝   ${NC}" 
echo "${YELLOW}                                                    Version $VERSION"
echo "${YELLOW}--------------------------------------------------------------------"
echo "${GREEN} Software Developer Kit for programming in Amstrad Basic and Ugbasic"
echo "${YELLOW}--------------------------------------------------------------------${NC}"
echo ""
echo "${BLUE}GITHUB: https://github.com/CPCReady/installer"
echo "${BLUE}DOC   : https://cpcready.readthedocs.io/es/latest/"
echo ""
echo "${YELLOW}--------------------------------------------------------------------"

echo

##################################
# CHEQUEO DE REQUISITOS
##################################
echo "${BLUE}INFO     ${NC}Checking requirements...🍺"
if command -v pip &> /dev/null; then
    echo "${BLUE}INFO     ${NC}pip installed [${GREEN}OK${NC}]"
else
    echo "${RED}ERROR    pip not installed on the system!!!"
    echo "         ${YELLOW}To continue please execute: ${GRAY}sudo apt-get install python3-pip"
    exit 1
fi

if command -v dos2unix &> /dev/null; then
    echo "${BLUE}INFO     ${NC}dos2unix installed [${GREEN}OK${NC}]"
else
    echo "${RED}ERROR    dos2unix not installed on the system!!!"
    echo "         ${YELLOW}To continue please execute: ${GRAY}sudo apt-get install dos2unix"
    exit 1
fi
##################################
# DOWNLOAD RETRO VIRTUAL MACHINE
##################################
echo "${BLUE}INFO     ${NC}Installs tools...🍺"
download_link="https://static.retrovm.org/release/beta1/linux/x64/RetroVirtualMachine.$VERSION_RETROVIRTUALMACHINE.linux.x64.zip"
zip_file="RetroVirtualMachine.zip"

download_dir="./downloads"
extracted_dir="./extracted"
target_dir="tools/bin"

mkdir -p "$download_dir" "$extracted_dir" "$target_dir"
echo "${GREEN}DOWNLOAD ${NC}RetroVitualMachine ($VERSION_RETROVIRTUALMACHINE)"
if wget -O "$download_dir/$zip_file" "$download_link" > /dev/null 2>&1; then
    echo "${BLUE}INFO     ${NC}RetroVitualMachine [${GREEN}OK${NC}]"
else
    echo "${RED}ERROR    ${NC}Download RetroVirtual Machine [${RED}ERROR${NC}]"
    exit 1
fi

if unzip -q "$download_dir/$zip_file" -d "$extracted_dir"; then
    echo "${GREEN}UNZIP    ${NC}RetroVitualMachine > tools/bin [${GREEN}OK${NC}]"
else
    echo "${RED}ERROR    ${NC}Unzip RetroVirtual Machine [${RED}ERROR${NC}]"
    exit 1
fi

mv "$extracted_dir/RetroVirtualMachine" "$target_dir/"
rm -rf "$download_dir" "$extracted_dir"

##################################
# INSTALL CPCREADY
##################################
comando="pip install cpcready==${VERSION}"
echo "${GREEN}INSTALL  ${NC}CPCReady ($VERSION)...🍺"
$comando > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "${BLUE}INFO     ${NC}Install CPCReady ($VERSION) [${GREEN}OK${NC}]"
else
    echo "${RED}ERROR    CPCReady not installed!!!"
    exit 1
fi

##############################
# ADD ENVIRONMENT VARIABLES
##############################
# echo "${BLUE}INFO     ${NC}Installation path: $PATH_INSTALL"
# if [ -f "$HOME/.bashrc" ]; then
#     if ! grep -qxF "export CPCREADY=$PATH_INSTALL" "$HOME/.bashrc"; then
#         echo "export CPCREADY=$PATH_INSTALL" >> "$HOME/.bashrc"
#         echo "export CPCREADY_CFG=$PATH_INSTALL/CPCReady/cfg" >> "$HOME/.bashrc"
#         echo "export PATH=\$PATH:$PATH_INSTALL/CPCReady/tools/bin" >> "$HOME/.bashrc"
#         echo "export PATH=\$PATH:$PATH_INSTALL/CPCReady/tools/z88dk/bin" >> "$HOME/.bashrc"
#         echo "export ZCCCFG=$PATH_INSTALL/CPCReady/tools/z88dk/lib/config" >> "$HOME/.bashrc"
#         echo "${GREEN}ADD      ${NC}Environment variables to .bashrc [${GREEN}OK${NC}]"
#     else
#         echo "${YELLOW}WARNING  ${NC}Environment variables already exist in .bashrc"
#     fi
# else
#     echo "${YELLOW}WARNING  ${NC}Not exist .zshrc"
# fi

# if [ -f "$HOME/.zshrc" ]; then
#     if ! grep -qxF "export CPCREADY=$PATH_INSTALL" "$HOME/.zshrc"; then
#         echo "export CPCREADY=$PATH_INSTALL" >> "$HOME/.zshrc"
#         echo "export CPCREADY_CFG=$PATH_INSTALL/CPCReady/cfg" >> "$HOME/.zshrc"
#         echo "export PATH=\$PATH:$PATH_INSTALL/CPCReady/tools/bin" >> "$HOME/.zshrc"
#         echo "export PATH=\$PATH:$PATH_INSTALL/CPCReady/tools/z88dk/bin" >> "$HOME/.zshrc"
#         echo "export ZCCCFG=$PATH_INSTALL/CPCReady/tools/z88dk/lib/config" >> "$HOME/.zshrc"
#         echo "${GREEN}ADD      ${NC}Environment variables to .zshrc [${GREEN}OK${NC}]"
#     else
#         echo "${YELLOW}WARNING  ${NC}Environment variables already exist in .zshrc"
#     fi
# else
#     echo "${YELLOW}WARNING  ${NC}Not exist .zshrc"
# fi

echo

echo "${YELLOW}--------------------------------------------------------------------"
echo -e "🚀  ${GREEN}Successfully installed CPCReady v$VERSION"
echo
echo -e "👉  ${YELLOW}Thank you for using CPCReady"
echo "${YELLOW}--------------------------------------------------------------------"