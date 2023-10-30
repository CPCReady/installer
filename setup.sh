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
cpcready_path="tools/sdk"

VERSION=$(cat VERSION)
VERSION_RETROVIRTUALMACHINE="2.0.beta-1.r7"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PATH_INSTALL="$SCRIPT_DIR"
PATH_CPCREADY="$SCRIPT_DIR/tools/sdk"
PATH_CPCREADY_DIST="$SCRIPT_DIR/tools/sdk/dist"
WHL_FILE="$PATH_CPCREADY_DIST/CPCReady-${VERSION}-py3-none-any.whl"

# Valor predeterminado
INSTALL="full"

if [ "$#" -gt 0 ]; then
    # Si se pasaron argumentos, verificar si el primer argumento está en la lista permitida
    caso_valido=false
    for caso in "upgrade" "full"; do
        if [ "$1" == "$caso" ]; then
            caso_valido=true
            break
        fi
    done

    if [ "$caso_valido" == true ]; then
        INSTALL="$1"
    else
        echo
        echo "${RED}ERROR    The argument passed to the script is not valid. Options [upgrade, full]"
        exit 1
    fi
fi


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

check_install() {
    if ! grep -qxF "export CPCREADY=$PATH_INSTALL" "$HOME/$1"; then
        echo "${GREEN}CHECK    ${NC}Previous installation in $1 [${GREEN}NONE${NC}]"
    else
        echo "${RED}ERROR    CPCReady is installed on this computer. "
        echo "         To continue deleting data from $1 or exetute ./setup.sh upgrade to update software"
        exit 1
    fi
}

check_requirements() {
    if command -v $1 &> /dev/null; then
        echo "${BLUE}INFO     ${NC} - $1 installed [${GREEN}OK${NC}]"
    else
        echo "${RED}ERROR    $1 not installed on the system!!!"
        echo "         ${YELLOW}To continue please install $1"
        exit 1
    fi
}

generateChanges() {
    carpeta="docs/versions"
    archivo_concatenado="docs/CHANGES.md"
    if [ -e $archivo_concatenado ]; then
        rm $archivo_concatenado
    fi
    unamestr=$(uname)
    case "$unamestr" in
        "Linux")
            archivos=$(find "$carpeta" -type f -exec ls -t -p "{}" + | awk '{print $NF}')
            ;;
        "Darwin")
            archivos=$(find "$carpeta" -type f -exec ls -t -p "{}" + | awk '{print $NF}')
            ;;
        *)
            echo "Sistema operativo no compatible"
            exit 1
            ;;
    esac

    echo "## Historial de Cambios" > "$archivo_concatenado"
    for archivo in $archivos; do
        cat "$archivo" >> "$archivo_concatenado"
    done
}

del_temporal_files() {
    find . -type f -name ".DS_Store" -exec rm -f {} \;
    directorio_a_eliminar="$1"
    if [ -d "$directorio_a_eliminar" ]; then
        rm -r "$directorio_a_eliminar"
        echo "${GREEN}DELETE   ${NC} - $directorio_a_eliminar [${GREEN}OK${NC}]"
    fi
}


get_repo_version() {
    url_version="https://raw.githubusercontent.com/CPCReady/installer/main/VERSION"
    publishversion=$(curl -s "$url_version")
    if [ -z "$publishversion" ]; then
        echo "${RED}ERROR    ${NC}Could not obtain the latest published version"
        exit 1
    fi
}

compare_versions() {
    
    get_repo_version

    local v1=$1
    local v2=$2

    IFS='.' read -ra arr1 <<< "$v1"
    IFS='.' read -ra arr2 <<< "$v2"

    for i in "${!arr1[@]}"; do
        if [ "${arr1[i]}" -lt "${arr2[i]}" ]; then
            return 0
        elif [ "${arr1[i]}" -gt "${arr2[i]}" ]; then
            return 1
        fi
    done

}

##################################
# CHECK NEW VERSION
##################################

if [ "$INSTALL" == "upgrade" ]; then
    echo "${BLUE}INFO     ${NC}Checking new version...🍺"

    # Obtenemos version del repositorio.
    get_repo_version

    # comparamos con version instalada.
    if ! compare_versions "$publishversion" "$VERSION"; then
        echo "${BLUE}INFO     ${NC} - New version $publishversion found"
        echo "${BLUE}UPDATE   ${NC} - Get started update software."
        check_requirements "git"
        upgrade=$(git pull)
        echo "${BLUE}UPDATE   ${NC} - $upgrade"
    else
        echo "${BLUE}INFO     ${NC}The application is updated"
        exit
    fi
fi

##################################
# CHEQUEO DE REQUISITOS
##################################

echo "${BLUE}INFO     ${NC}Checking requirements...🍺"
check_requirements "pip"
check_requirements "python3"
check_requirements "dos2unix"
check_requirements "git"

##################################
# CHEQUEO DE INSTALACION
##################################

check_install ".bashrc"
check_install ".zshrc"


##################################
# DOWNLOAD RETRO VIRTUAL MACHINE
##################################
echo "${BLUE}INFO     ${NC}Installs tools...🍺"
if [ "$ENVIRONMENT" != "DOCKER" ]; then
    download_link="https://static.retrovm.org/release/beta1/linux/x64/RetroVirtualMachine.$VERSION_RETROVIRTUALMACHINE.linux.x64.zip"
    zip_file="RetroVirtualMachine.zip"

    download_dir="./downloads"
    extracted_dir="./extracted"
    target_dir="tools/bin"

    mkdir -p "$download_dir" "$extracted_dir" "$target_dir"
    echo "${GREEN}DOWNLOAD ${NC} - RetroVitualMachine ($VERSION_RETROVIRTUALMACHINE)"
    # if wget -O "$download_dir/$zip_file" "$download_link" > /dev/null 2>&1; then
    if wget -O "$download_dir/$zip_file" "$download_link"; then
        echo "${BLUE}INFO     ${NC} - RetroVitualMachine [${GREEN}OK${NC}]"
    else
        echo "${RED}ERROR    ${NC}Download RetroVirtual Machine [${RED}ERROR${NC}]"
        exit 1
    fi

    if unzip -q "$download_dir/$zip_file" -d "$extracted_dir"; then
        echo "${GREEN}UNZIP    ${NC} - RetroVitualMachine > tools/bin [${GREEN}OK${NC}]"
    else
        echo "${RED}ERROR    ${NC}Unzip RetroVirtual Machine [${RED}ERROR${NC}]"
        exit 1
    fi

    mv "$extracted_dir/RetroVirtualMachine" "$target_dir/"
    rm -rf "$download_dir" "$extracted_dir"
else
    echo "${YELLOW}WARNING  ${NC}No install Retrovirtualmachine desktop in docker."
fi
##################################
# INSTALL CPCREADY
##################################

echo "${GREEN}INSTALL  ${NC}Dependencies Build & twine...🍺"

del_temporal_files "$PATH_CPCREADY/dist"
del_temporal_files "$PATH_CPCREADY/CPCReady.egg-info"
del_temporal_files "$PATH_CPCREADY/CPCReady/__pycache__"

pip install build
pip install --upgrade twine
echo "${GREEN}COMPILE  ${NC}CPCReady ($VERSION)"
echo "__version__ = '$VERSION'" > $PATH_CPCREADY/CPCReady/__init__.py

##################################
# COMPILE CPCREADY
##################################

cd $PATH_CPCREADY
python3 -m build

##################################
# INSTALL CPCREADY
##################################

pip install "$WHL_FILE" --force-reinstall 

if [ $? -eq 0 ]; then
    echo "${BLUE}INFO     ${NC}CPCReady install successfully [${GREEN}OK${NC}]"
else
    exit 1
fi

# #############################
# ADD ENVIRONMENT VARIABLES
# #############################
if [ "$INSTALL" == "full" ]; then
    echo "${BLUE}INFO     ${NC}Installation path: $PATH_INSTALL"
    if [ -f "$HOME/.bashrc" ]; then
        if ! grep -qxF "export CPCREADY=$PATH_INSTALL" "$HOME/.bashrc"; then
            echo "export CPCREADY=$PATH_INSTALL" >> "$HOME/.bashrc"
            echo "export CPCREADY_CFG=$PATH_INSTALL/CPCReady/cfg" >> "$HOME/.bashrc"
            echo "export PATH=\$PATH:$PATH_INSTALL/CPCReady/tools/bin" >> "$HOME/.bashrc"
            echo "export PATH=\$PATH:$PATH_INSTALL/CPCReady/tools/z88dk/bin" >> "$HOME/.bashrc"
            echo "export ZCCCFG=$PATH_INSTALL/CPCReady/tools/z88dk/lib/config" >> "$HOME/.bashrc"
            echo "${GREEN}ADD      ${NC}Environment variables to .bashrc [${GREEN}OK${NC}]"
        else
            echo "${YELLOW}WARNING  ${NC}Environment variables already exist in .bashrc"
        fi
    else
        echo "${YELLOW}WARNING  ${NC}Not exist .zshrc"
    fi

    if [ -f "$HOME/.zshrc" ]; then
        if ! grep -qxF "export CPCREADY=$PATH_INSTALL" "$HOME/.zshrc"; then
            echo "export CPCREADY=$PATH_INSTALL" >> "$HOME/.zshrc"
            echo "export CPCREADY_CFG=$PATH_INSTALL/CPCReady/cfg" >> "$HOME/.zshrc"
            echo "export PATH=\$PATH:$PATH_INSTALL/CPCReady/tools/bin" >> "$HOME/.zshrc"
            echo "export PATH=\$PATH:$PATH_INSTALL/CPCReady/tools/z88dk/bin" >> "$HOME/.zshrc"
            echo "export ZCCCFG=$PATH_INSTALL/CPCReady/tools/z88dk/lib/config" >> "$HOME/.zshrc"
            echo "${GREEN}ADD      ${NC}Environment variables to .zshrc [${GREEN}OK${NC}]"
        else
            echo "${YELLOW}WARNING  ${NC}Environment variables already exist in .zshrc"
        fi
    else
        echo "${YELLOW}WARNING  ${NC}Not exist .zshrc"
    fi
fi
echo

echo "${YELLOW}--------------------------------------------------------------------"
echo -e "🚀  ${GREEN}Successfully installed CPCReady v$VERSION"
echo
echo -e "👉  ${YELLOW}Thank you for using CPCReady"
echo "${YELLOW}--------------------------------------------------------------------"