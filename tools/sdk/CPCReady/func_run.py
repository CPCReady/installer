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

import os
import sys
import datetime
import shutil
from jinja2 import Template
import subprocess
from CPCReady import common as cm
from CPCReady import func_info as info
import io
import platform


def ping_ok(sHost) -> bool:
    try:
        subprocess.check_output(
            "ping -{} 1 {}".format("n" if platform.system().lower() == "windows" else "c", sHost), shell=True
        )
    except Exception:
        return False

    return True

def executeFileM4BOARD(ip,file):
    FNULL = open(os.devnull, 'w')
    cmd = [cm.M4BOARD, "-x",ip,file]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        cm.msgInfo("Execute " + cm.getFileExt(file) + " ==> M4 Board")
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(file) + f' executing command: {e.output.decode()}')
        return False

def uploadFileM4BOARD(ip,file,folder):
    FNULL = open(os.devnull, 'w')
    cmd = [cm.M4BOARD, "-u",str(ip),str(file), str(folder), "0"]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        cm.msgInfo("Upload " + cm.getFileExt(file) + " ==> M4 Board")
        return True
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Error ' + cm.getFileExt(file) + f' executing command: {e.output.decode()}')
        return False

# def execute(project,emulator):

#     cm.validate_cfg(cm.CFG_PROJECT,cm.SECTIONS_PROJECT)
#     cm.validate_cfg(cm.CFG_EMULATORS,cm.SECTIONS_EMULATOR)
    
#     DATA_PROJECT   = cm.getData(cm.CFG_PROJECT)
#     DATA_EMULATORS = cm.getData(cm.CFG_EMULATORS)

#     PROJECT_NAME         = DATA_PROJECT.get('general','name',fallback="NONE")
#     PROJECT_AUTHOR       = DATA_PROJECT.get('general','author',fallback="NONE")
#     PROJECT_CDT          = DATA_PROJECT.get('CDT','name',fallback="NONE")
#     PROJECT_DSK          = DATA_PROJECT.get('DSK','name',fallback="NONE")
    
#     if PROJECT_NAME == "NONE":
#         cm.msgError(f"project name in {cm.CFG_PROJECT} does not exist or is empty")
#         sys.exit(1)
            
#     if PROJECT_CDT == "NONE":
#         cm.msgError(f"CDT name in {cm.CFG_PROJECT} does not exist or is empty")
#         sys.exit(1)  
  
#     if PROJECT_DSK == "NONE":
#         cm.msgError(f"DSK name in {cm.CFG_PROJECT} does not exist or is empty")
#         sys.exit(1)
    
#     PROJECT_CDT_NAME     = f"{cm.PATH_DSK}/{PROJECT_CDT}"
#     PROJECT_DSK_NAME     = f"{cm.PATH_DSK}/{PROJECT_DSK}"

#     cm.showHeadDataProject(cm.getFileExt(PROJECT_DSK_NAME))
    
#     if emulator == "rvm-web":   
        
#         PROJECT_RVM_MODEL    = DATA_EMULATORS.get(emulator,'model',fallback="NONE")
#         if PROJECT_RVM_MODEL == "NONE":
#             cm.msgError(f"CPC model has not been selected in rvm-web from the {cm.CFG_EMULATORS} file")
#             cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)
#         if not cm.validateCPCModel(PROJECT_RVM_MODEL):
#             cm.msgError(f"CPC model {PROJECT_RVM_MODEL} not supported")
#             cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)         
#         PROJECT_RVM_RUN      = DATA_EMULATORS.get(emulator,'run',fallback="")
#         EMULATOR             = f"Retro Virtual Machine WEB ({cm.TEMPLATE_RVM_WEB})"
#         context = {
#             'name': PROJECT_NAME,
#             'model': PROJECT_RVM_MODEL,
#             'dsk': f"{PROJECT_DSK_NAME}",
#             'run': f'{PROJECT_RVM_RUN}'
#         }
#         cm.createTemplate("rvm-web.html", context, cm.PATH_CFG)
#         cm.msgInfo(f"CPC Model  : {PROJECT_RVM_MODEL}")
#         cm.msgInfo(f"RUN Command: {PROJECT_RVM_RUN}")
#         cm.msgInfo(f"Emulator   : RVM Web ({cm.TEMPLATE_RVM_WEB})") 
#         cm.showFoodDataProject("SUCCCESSFULLY LAUNCHED IMAGE", 0)
           
#     elif emulator == "rvm-desktop":   
        
#         PROJECT_RVM_MODEL    = DATA_EMULATORS.get(emulator,'model',fallback="NONE")
#         if PROJECT_RVM_MODEL == "NONE":
#             cm.msgError(f"CPC model has not been selected in rvm-web from the {cm.CFG_EMULATORS} file")
#             cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)
#         if not cm.validateCPCModel(PROJECT_RVM_MODEL):
#             cm.msgError(f"CPC model {PROJECT_RVM_MODEL} not supported")
#             cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)                
#         PROJECT_RVM_RUN      = DATA_EMULATORS.get(emulator,'run',fallback="")
#         PROJECT_RVM_PATH     = DATA_EMULATORS.get(emulator,'path',fallback="")
        
#         if PROJECT_RVM_PATH != "":
#             if cm.fileExist(PROJECT_RVM_PATH):
#                 cm.msgInfo(f"CPC Model  : {PROJECT_RVM_MODEL}")
#                 cm.msgInfo(f"RUN Command: {PROJECT_RVM_RUN}")
#                 cm.msgInfo(f"Emulator   : RVM Desktop ({PROJECT_RVM_PATH})")
#                 FNULL = open(os.devnull, 'w')
#                 try:
#                     retcode = subprocess.Popen([PROJECT_RVM_PATH,"-i", PROJECT_DSK_NAME,"-b=cpc"+str(PROJECT_RVM_MODEL),"-c="+PROJECT_RVM_RUN + "\n"], stdout=FNULL, stderr=subprocess.STDOUT)
#                 except subprocess.CalledProcessError as e:
#                     cm.msgError(f'{cm.getFileExt(PROJECT_DSK_NAME)} RELEASED WITH ERROR: {e.output.decode()}')
#                     return False
#             else:
#                 cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)
#         else:
#             cm.msgError(f"RVM Desktop path does not exist in {cm.CFG_PROJECT}")
#             cm.showFoodDataProject("DISC IMAGE RELEASED WITH ERROR", 1)

#         cm.showFoodDataProject("SUCCCESSFULLY LAUNCHED IMAGE", 0)
        
#     elif emulator == "m4board":   
        
#         PROJECT_M4_EXECUTE = DATA_EMULATORS.get(emulator,'execute',fallback="")
#         PROJECT_M4_FOLDER  = DATA_EMULATORS.get(emulator,'folder',fallback="CPCReady")
#         PROJECT_M4BOARD_IP = DATA_EMULATORS.get(emulator,'ip',fallback="NONE")
#         EMULATOR             = "M4 Board"
#         cm.msgInfo(f"Emulator    : {EMULATOR}")
#         if PROJECT_M4BOARD_IP == "NONE":
#             cm.msgError(f"No ip found in {cm.CFG_EMULATORS} for M4 Board")
#             cm.showFoodDataProject("NO FILES UPLOAD M4 BOARD", 1)
#         if not cm.validateIP(PROJECT_M4BOARD_IP):
#             cm.showFoodDataProject("NO FILES UPLOAD M4 BOARD", 1)
#         if not ping_ok(PROJECT_M4BOARD_IP):
#             cm.msgError(f"No connect ==> {PROJECT_M4BOARD_IP}")
#             cm.showFoodDataProject("NO FILES UPLOAD M4 BOARD", 1)
#         else:
#             cm.msgInfo(f"Connect OK ==> {PROJECT_M4BOARD_IP}")          
        
        
#         count = 0

#         archivos = os.listdir(cm.PATH_DISC)
#         for archivo in archivos:
#             if os.path.isfile(os.path.join(cm.PATH_DISC, archivo)):
#                 if not uploadFileM4BOARD(PROJECT_M4BOARD_IP,cm.PATH_DISC + "/" + archivo,PROJECT_M4_FOLDER):
#                     cm.showFoodDataProject("NO FILES UPLOAD M4 BOARD", 1)
#             count = count + 1     
        
#         if count > 0:
#             if cm.fileExist(cm.PATH_DISC + "/" + PROJECT_M4_EXECUTE):
#                 if not executeFileM4BOARD(PROJECT_M4BOARD_IP,PROJECT_M4_FOLDER + "/" + PROJECT_M4_EXECUTE):
#                     cm.showFoodDataProject("NO FILES UPLOAD M4 BOARD", 1)
                
#                 cm.showFoodDataProject("FILES UPLOAD AND EXECUTE M4 BOARD", 0)
#         else:
#             cm.msgWarning("No upload files in " + cm.PATH_DISC)    
#             cm.showFoodDataProject("NO FILE EXECUTED M4 BOARD", 1)
                  

        
def launch(file,emulator):

    if not cm.fileExist(file):
        sys.exit(1)
        
    if not cm.validateSection(file,emulator):
        print()
        cm.msgError(f"Setting {emulator} not exist in {file}")
        sys.exit(1)        
    
    DATA_EMULATORS = cm.getData(file)
    RVM_EMULATOR_TYPE  = DATA_EMULATORS.get(emulator,'type',fallback="NONE")
    RVM_CPC_MODEL      = DATA_EMULATORS.get(emulator,'model',fallback="NONE")
    RVM_CPC_RUN        = DATA_EMULATORS.get(emulator,'run',fallback="NONE")
    RVM_CPC_IMAGE      = DATA_EMULATORS.get(emulator,'image',fallback="NONE")
    # RVM_CPC_PATH       = DATA_EMULATORS.get(emulator,'path',fallback="NONE")
    
    
    if RVM_EMULATOR_TYPE not in cm.EMULATORS_TYPES:
        cm.msgError(f"The {RVM_EMULATOR_TYPE} emulator type is not supported.")
        sys.exit(1)  
    if RVM_CPC_MODEL not in cm.CPC_MODELS:
        cm.msgError(f"CPC Model {RVM_CPC_MODEL} not supported.")
        sys.exit(1)          
    if not cm.fileExist(RVM_CPC_IMAGE):
        sys.exit(1)  
    
    #info.show("👉 DSK FILE: " + RVM_CPC_IMAGE)
    info.show(False) 
    
    cm.showInfoTask(f"Launch disc image "+RVM_CPC_IMAGE+" in progress...")
    
    cm.msgInfo(f"Emulator type ==> {RVM_EMULATOR_TYPE}")  
    cm.msgInfo(f"CPC Model     ==> {RVM_CPC_MODEL}")
    cm.msgInfo(f"CPC Image     ==> {RVM_CPC_IMAGE}") 
    
    if RVM_EMULATOR_TYPE.upper() == "DESKTOP" and os.getenv("ENVIRONMENT") == "DOCKER":
        cm.msgError(f"It is not possible to run RetroVirtualMachine Desktop in a container environment..")
        cm.showFoodDataProject("Failure launch disc image", 1)  
        sys.exit(1)
        
    if RVM_EMULATOR_TYPE.upper() == "DESKTOP":
    
        rvmDesktop("RetroVirtualMachine",RVM_CPC_IMAGE,RVM_CPC_MODEL,RVM_CPC_RUN)
        cm.showFoodDataProject("Successfully launch disc image", 0)
    
    elif RVM_EMULATOR_TYPE.upper() == "WEB":
        context = {
            'name': "RETRO VIRTUAL MACHINE WEB",
            'model': RVM_CPC_MODEL,
            'dsk': f"{RVM_CPC_IMAGE}",
            'run': f'{RVM_CPC_RUN}'
        }
        cm.createTemplate("rvm-web.html", context, "cfg/" + emulator + ".html" ) 
        cm.showFoodDataProject("Template RVM Web Create successfully", 0)
         
    elif RVM_EMULATOR_TYPE.upper() == "M4BOARD":
        
        PROJECT_M4_EXECUTE = DATA_EMULATORS.get(emulator,'execute',fallback="")
        PROJECT_M4_FOLDER  = DATA_EMULATORS.get(emulator,'folder',fallback="CPCReady")
        PROJECT_M4BOARD_IP = DATA_EMULATORS.get(emulator,'ip',fallback="NONE")
        cm.msgInfo(f"Emulator type ==> M4 Board")  
        cm.msgInfo(f"CPC Image     ==> {RVM_CPC_IMAGE}")
        cm.msgInfo(f"Files         ==> {PROJECT_M4_FOLDER}") 
        if PROJECT_M4BOARD_IP == "NONE":
            cm.msgError(f"No ip found in {cm.CFG_EMULATORS} for M4 Board")
        if not cm.validateIP(PROJECT_M4BOARD_IP):
            sys.exit(1)
        if not ping_ok(PROJECT_M4BOARD_IP):
            cm.msgError(f"No connect    ==> {PROJECT_M4BOARD_IP}")
            cm.msgInfo (f"Connect OK    ==> {PROJECT_M4BOARD_IP}")
            sys.exit(1)
        else:
            cm.msgInfo (f"Connect OK    ==> {PROJECT_M4BOARD_IP}")        
        
        count = 0

        archivos = os.listdir(cm.PATH_DISC)
        for archivo in archivos:
            if os.path.isfile(os.path.join(cm.PATH_DISC, archivo)):
                if not uploadFileM4BOARD(PROJECT_M4BOARD_IP,cm.PATH_DISC + "/" + archivo,PROJECT_M4_FOLDER):
                    sys.exit(1)
            count = count + 1     
        
        if count > 0:
            if cm.fileExist(cm.PATH_DISC + "/" + PROJECT_M4_EXECUTE):
                if not executeFileM4BOARD(PROJECT_M4BOARD_IP,PROJECT_M4_FOLDER + "/" + PROJECT_M4_EXECUTE):
                    sys.exit(1)
                
                cm.msgInfo (f"Files upload and execute in M4 Board.")
        else:
            cm.msgWarning("No upload files in " + cm.PATH_DISC) 

        cm.showFoodDataProject("Successfully send files to M4 Board", 0)
          
def rvmDesktop(RVM_CPC_PATH,RVM_CPC_IMAGE,RVM_CPC_MODEL,RVM_CPC_RUN):
    FNULL = open(os.devnull, 'w')
    try:
        retcode = subprocess.Popen([RVM_CPC_PATH,"-i", RVM_CPC_IMAGE,"-b=cpc"+str(RVM_CPC_MODEL),"-c="+RVM_CPC_RUN + "\n"], stdout=FNULL, stderr=subprocess.STDOUT)
        cm.msgInfo(f"Disk image launched successfully")
    except subprocess.CalledProcessError as e:
        cm.msgError(f'Failed to launch {cm.getFileExt(RVM_CPC_IMAGE)} image on RVM Desktop: {e.output.decode()}')
        sys.exit(1)