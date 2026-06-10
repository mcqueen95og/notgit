import sys
import os
import shutil
import json
import datetime

ver = "0.1"
helpmsg = """
notgit v0.1
Commands:
    notgit init: Create a .notgit folder in the current directory
    notgit save "msg": Saves current directory as a snapshot into -> .notgit
    notgit history: Shows all saved snapshots
    """
print("notgit: Recommended to use current directory\n")

try:
    command = sys.argv[1]

    if command == "init":
        os.makedirs(".notgit/saves/", exist_ok=True)
    
        with open(".notgit/history.json", "w") as f:
            json.dump({"saves": []}, f, indent=4)

        print("notgit: Directory intilized")
    
    elif command == "save":
        if os.path.exists(".notgit/"):
            print("notgit: .notgit exists")
            save_id = str(int(datetime.datetime.now().timestamp()))

            shutil.copytree(os.getcwd(), ".notgit/saves/", dirs_exist_ok=True, ignore=shutil.ignore_patterns(".notgit"))
            print("notgit: took a snapshot of files")
        else:
            print("notgit: intilize directory first!")

    else:
        print(f"notgit: command '{command}' not valid")
except IndexError:
    print(helpmsg)
