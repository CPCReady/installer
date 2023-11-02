import os
import re
from pprint import pprint
import inquirer

def name_validation(answers, current):
    if not current.strip():
        raise inquirer.errors.ValidationError("", reason="El nombre no puede estar en blanco.")
    if answers["nomenclatura"] == "Sí" and len(current) > 6:
        raise inquirer.errors.ValidationError("", reason="El nombre no puede tener más de 6 caracteres.")
    return True

def project_name_validation(answers, current):
    current = current.strip()
    if not current:
        raise inquirer.errors.ValidationError("", reason="El nombre del proyecto no puede estar en blanco.")
    
    if os.path.exists(current):
        raise inquirer.errors.ValidationError("", reason="La carpeta ya existe, elija un nombre de proyecto diferente.")
    
    return True

questions = [
    inquirer.List("nomenclatura", message="¿Desea activar la nomenclatura 6:3?", choices=["Sí", "No"]),
    inquirer.Text("project_name", message="Nombre del proyecto o ruta para la carpeta", validate=project_name_validation),
    inquirer.Text("name", message="What's your name?", validate=name_validation),
]

answers = inquirer.prompt(questions)

project_name = answers["project_name"].strip()
if not os.path.isabs(project_name):
    project_path = os.path.join(os.getcwd(), project_name)
else:
    project_path = project_name

os.makedirs(project_path, exist_ok=True)
print(f"Se ha creado la carpeta del proyecto en: {project_path}")

pprint(answers)
