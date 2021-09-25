import os
import requests
from pathlib import Path

images = str(Path.home()) + "/tourpaper/images/"
folder = "/tourpaper/"
path = str(Path.home()) + folder
linksFile = path + "/link.txt"

if(os.path.exists(images) == False):
    os.mkdir(images)

if(os.stat(linksFile).st_size == 0):
    print("list is not initialised, create the list first !")
    exit(0)

with open(linksFile, "r+") as file:
    lines = file.readlines()

    # removing the first line
    file.seek(0)
    file.truncate()
    file.writelines(lines[1:])

    wallpaper = lines[0].split(" ")
    name = wallpaper[0]
    
    url = wallpaper[1]

    print("downloading ...", name)
    res = requests.get(url, allow_redirects=True)
    open(images+name, "wb").write(res.content)

    print("setting...", name)
    os.system(f"gsettings set org.gnome.desktop.background picture-uri {images+name}")
