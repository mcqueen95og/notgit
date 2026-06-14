# notgit Functions

import os
import shutil
import json
import datetime
import sys

def init():
    if os.path.exists(".notgit/"):
        print("notgit: Directory already intialized!")
    else:
        os.makedirs(".notgit/saves/", exist_ok=True)
        
        with open(".notgit/history.json", "w") as f:
            json.dump([], f, indent=4)
            f.close()
        print(f"notgit: Directory [{os.getcwd()}] intilized")

def save(data):
    if os.path.exists(".notgit/"):
        save_id = str(int(datetime.datetime.now().timestamp()))

        os.makedirs(f".notgit/saves/{save_id}", exist_ok=False)
        shutil.copytree(src=os.getcwd(), dst=f"{os.getcwd()}/.notgit/saves/{save_id}", dirs_exist_ok=True, ignore=shutil.ignore_patterns(".notgit", '__pycache__', '.git'))

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
        return "ok"
    else:
        return

def history() -> str:
    with open(".notgit/history.json", "r") as h:
        data = json.load(h)
        for every in data:
            print(f"ID: {every["save_id"]}\nMsg: {every["message"]}\nFiles: {every["files"]}\n")

def undo(save_id=None):
    usr = input("Revert Changes? (THIS WOULD DELETE ALL FILES INSIDE C.D) (y/n): ")

    if not os.path.exists(".notgit/"):
        print("notgit: initialize directory first! (notgit init)")
        return

    if usr.lower() != "y":
        return

    target_dir = ".notgit/saves/"

    # check save_id
    if save_id is None:
        folders = [f for f in os.scandir(target_dir) if f.is_dir()]
        if not folders:
            print("notgit: No saves found.")
            return
        target = max(folders, key=lambda f: f.stat().st_ctime).name
    else:
        if not os.path.exists(f"{target_dir}{save_id}"):
            print(f"notgit: save_id '{save_id}' doesn't exist!")
            return
        target = save_id

    print(f"notgit: reverting to save '{target}'")

    # delete logic
    folder_path = os.getcwd()
    for filename in os.listdir(folder_path):
        if filename == ".notgit" or filename == ".git":
            continue
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"notgit: Failed to delete {file_path}. Reason: {e}")

    # copy paste logic
    shutil.copytree(f"{os.getcwd()}/.notgit/saves/{target}", os.getcwd(), dirs_exist_ok=True)
    print("notgit: revert complete!")