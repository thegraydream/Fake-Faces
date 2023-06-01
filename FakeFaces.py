# ╭─────────────────────────── Import ───────────────────────────╮ #
import os
import json
import time

try:import requests
except:
     os.system('pip install requests')
     os.system('cls')
     import requests

# ╭─────────────────────────── Version ───────────────────────────╮ #
VERSIONID = '1.0.0'


# ╭─────────────────────────── Github ───────────────────────────╮ #
github = "Fake-Faces"


# ╭─────────────────────────── Colors ───────────────────────────╮ #
green = "\033[0;32m"
red = "\033[0;31m"
reset = "\033[0m"


# ╭─────────────────────────── Config Data ───────────────────────────╮ #
config_default = """{
    "log": true,
    "version": true
}"""


if not os.path.exists('config.json'):open('config.json', 'w', encoding='utf-8').write(config_default) # Create config.json

configdata = json.loads(open('config.json', 'r', encoding='utf-8').read()) # Read config.json
try:log_statut = configdata["log"]  # Read log data
except:log_statut = True
try:version = configdata["version"]  # Read log data
except:version = True

def check_version():
    if version == True:
        try:
            if not requests.get(f'https://raw.githubusercontent.com/thegraydream/{github}/master/version').text.strip() == VERSIONID:
                if log_statut == True:print(f'{reset}[{red}>{reset}] {red}You are not using the latest version of {github.replace("-", " ")}, please update it on "https://github.com/thegraydream/{github}".{reset}')

                r = input('Would you like to download the latest version? (y/n) > ').strip()
                if r == "y":
                    for dow in json.loads(requests.get(f'https://raw.githubusercontent.com/thegraydream/{github}/master/update.json').text)["update"]:
                        if log_statut == True:print(f'{reset}[{green}>{reset}] {green}Downloading {dow}{reset}')
                        try:
                            content = requests.get(f'https://raw.githubusercontent.com/thegraydream/{github}/master/{dow}').text
                            if content == "404: Not Found":print(f'{reset}[{red}>{reset}] {red} We cannot find the file {dow}')
                            else:
                                open(dow, 'w', encoding='utf-8').write(content)
                        except:
                            if log_statut == True:print(f'{reset}[{red}<{reset}] {red} An error occurred while downloading the latest version of {dow}')
                            return False, f'Error while downloading the update ({dow})'
                    return True, 'Update completed successfully, please restart program'
                else:return None, 'You have cancelled the update'
        except:return False, f'Error while downloading the update'
    else:return None, 'No update available'


# ╭─────────────────────────── Def Fake Faces ───────────────────────────╮ #
def fake_faces(number=1, path='.', name=int(time.time())):
    try:

        # ╭─── Author ───╮ #
        if log_statut == True:print(f'{reset}[{green}-{reset}] TikTok TTS by TheGrayDream, need help or report a bug? https://dsc.gg/tgdgithub') # Log Print


        # ╭─── Version ───╮ #
        if version == True:
            if log_statut == True:print(f'{reset}[{green}-{reset}] Update search') # Log Print
            ver = check_version()
            if log_statut == True:print(f'{reset}[{green}-{reset}] State: {ver[0]} - {ver[1]}') # Log Print


        # ╭─── Manage ───╮ #
        picture_path = [] # Path List
        image_data = [] # Image Data List
        if str(path[-1:]).strip() == '\\' or str(path[-1:]).strip() == '/':path = path[:-1] # Remove useless / or \

    
        # ╭─── Download all image ───╮ #
        if log_statut == True:print(f'{reset}[{green}+{reset}] {green}Starting to download {number} image(s)') # Log Print
        for nb in range(number):
            while True:
                try:
                    os.makedirs(path, exist_ok=True) # Create Path Folder
                    response = requests.get('https://thispersondoesnotexist.com/') # Request to thispersondoesnotexist.com for fake faces
                
                    if not response.content in image_data:
                        open(f'{path}/{name}{nb}.png', 'wb').write(response.content) # Write content
                        image_data.append(response.content) # Add response.content to image_data list
                        picture_path.append(f'{path}/{name}{nb}.png') # Add path to list
                        if log_statut == True:print(f'{reset}[{green}+{reset}] {green}{path}/{name}{nb}.png has been created!{reset}') # Log Print
                        break
                except:
                    if log_statut == True:print(f'{reset}[{red}+{reset}] {red}An error has occurred! Retrying...{reset}') # Log Print
        if log_statut == True:print(f'{reset}[{green}+{reset}] {green}All {number} images have been downloaded!') # Log Print
        return True, picture_path
    except:
        if log_statut == True:print(f'{reset}[{red}+{reset}] {red}An error has occurred!{reset}') # Failed 
        return False, []


# ╭─────────────────────────── USAGE ───────────────────────────╮ #
# ╭───────────── Optional ────────────╮ #
# fake_faces(NB IMG, Path, 'File Name') #

fake_faces() # You can use fake_faces function with 0 argument (default nb = 1, default path = '.', default file = timestamp)
fake_faces(500, 'Fake/Faces', 'test') # Example
