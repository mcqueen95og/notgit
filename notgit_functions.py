# notgit Functions

import os
import shutil
import json
import datetime
import sys

def init():
    os.makedirs(".notgit/saves/", exist_ok=True)
    
    with open(".notgit/history.json", "w") as f:
        json.dump([], f, indent=4)
        f.close()

def save(data):
    if os.path.exists(".notgit/"):
        save_id = str(int(datetime.datetime.now().timestamp()))

        os.makedirs(f".notgit/saves/{save_id}", exist_ok=False)
        shutil.copytree(src=os.getcwd(), dst=f"{os.getcwd()}/.notgit/saves/{save_id}", dirs_exist_ok=True, ignore=shutil.ignore_patterns(".notgit", '__pycache__'))

        files = [name for name in os.listdir(os.getcwd()) if name != '.notgit' and name !='.git']
        data.append({
            "save_id":save_id,
            "timestamp": f"{datetime.datetime.now()}",
            "message": sys.argv[2] if len(sys.argv) > 2 else "",
            "files": files
        })
        with open(".notgit/history.json", "w") as history:
            json.dump(data, history, indent=4)
            history.close()
        return "init=ok"
    else:
        return

def history() -> str:
    with open(".notgit/history.json", "r") as h:
        data = json.load(h)
        for every in data:
            print(f"ID: {every["save_id"]}\nMsg: {every["message"]}\nFiles: {every["files"]}\n")

def undo():
    usr = input("Revert Changes? (THIS WOULD DELETE ALL FILES INSIDE C.D) (y/n): ")
    if os.path.exists(".notgit/"):
        if usr.lower() == "y":
            folder_path = os.getcwd()

            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if filename == ".notgit":
                        continue
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")

        else:
            return
    else:
        return