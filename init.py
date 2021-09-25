import requests
import os
from pathlib import Path
from urllib.parse import quote
import tourPaperTask

folder = "/tourpaper/"
path = str(os.path.join(Path.home())) + folder
linksFile = path + "/link.txt"
listFile = path + "/list.txt"

def addLink(query):
    query = quote(query)
    print("adding .. ", query)

    endpoint = f"https://api.unsplash.com/photos/random?query={query}&orientation=landscape&topics=wallpaper"
    api_key = "Client-ID H_2-ZGR4A33wOsyCUWmHXNxhkl68Rz8zyINTaYeWj7M"
    params = {"Authorization": api_key}

    res = requests.get(endpoint, headers=params)
    if(res.status_code == 404):
        print("not found - ", query)
    else:
        res = res.json()
        url = res["urls"]["raw"]
        with open(linksFile, "a") as file:  
            file.write(query.rstrip() + " " + url+"\n")

def readAndAdd():
    if(os.path.exists(listFile) == False or os.stat(listFile).st_size == 0):
        print("No list created ! create list.txt in ~/tourpaper/")
        exit(0)

    print("deleting old links ..")
    with open(linksFile, "w") as file:  
        file.truncate(0)

    with open(listFile, "r") as file:  
        for line in file:
            addLink(line)

    print("done")

if(os.path.exists(path) == False):
    os.mkdir(path)

readAndAdd()
tourPaperTask.main()