import os
import sys
import datetime
import shutil
from rich import print
from rich.console import Console
from CPCReady import common as cm
from CPCReady import func_info as info
from pprint import pprint
import inquirer

console = Console()

##
# Create project
#
# @param project: Project name
# @param model: CPC model
##

def project_name_validation(answers, current):
    current = current.strip()
    


    if not current:
        raise inquirer.errors.ValidationError("", reason="The project name cannot be blank.")
    
    if os.path.exists(current):
        raise inquirer.errors.ValidationError("", reason="The project name already exists in this path.")
    
    return True

##
# name63 return name format 6:3
#
# @param project: Project name
# @param model: CPC model
##
def name63 (name):
    if len(name) > 6:
        validate_name = name[:6]
    else:
        validate_name = name
    return validate_name


def create():

    info.show()

    questions = [
        inquirer.List("nomenclatura", message="You want to activate the nomenclature 6:3?", choices=["Yes", "No"]),
        inquirer.Text("project_name", message="Project name", validate=project_name_validation),
    ]

    print()
    answers = inquirer.prompt(questions)

    project_name = answers["project_name"].strip()
    if not os.path.isabs(project_name):
        project_path = os.path.join(os.getcwd(), project_name)
    else:
        project_path = project_name

    os.makedirs(project_path, exist_ok=True)

    folder_project = project_name

    nomenclature63 = answers["nomenclatura"].strip()
    project = folder_project
        
    cm.showInfoTask(f"Create project...")
    
    cm.msgCustom("CREATE", f"{folder_project}", "green")

    ########################################
    # CREATE PROJECT FOLDERS
    ########################################
    
    for folders in cm.subfolders:
        os.makedirs(f"{folder_project}/{folders}")
        cm.msgCustom("CREATE", f"{folder_project}/{folders}", "green")

    ########################################
    # CREATE TEMPLATES PROJECT
    ########################################
    
    ## PROJECT
    DATA = {'name': project,'nomenclature63': nomenclature63}
    cm.createTemplate("project.cfg",   DATA, f"{folder_project}/{cm.PATH_CFG}/project.cfg")
    cm.createTemplate("emulators.cfg", DATA, f"{folder_project}/{cm.PATH_CFG}/emulators.cfg")
    cm.createTemplate("images.cfg",    DATA, f"{folder_project}/{cm.PATH_CFG}/images.cfg")
    cm.createTemplate("sprites.cfg",   DATA, f"{folder_project}/{cm.PATH_CFG}/sprites.cfg")
    cm.createTemplate("MAIN.BAS",      DATA, f"{folder_project}/{cm.PATH_SRC}/MAIN.BAS")
    cm.createTemplate("MAIN.UGB",      DATA, f"{folder_project}/{cm.PATH_SRC}/MAIN.UGB")
    cm.createTemplate("Makefile",      DATA, f"{folder_project}/Makefile")

    print()
    console.print(f"🚀  Successfully creeated project [green]{project}[/]")
    print()
    console.print(f"👉  [yellow]Thank you for using CPCReady[/]")
    
