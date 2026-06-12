import notgit_functions as functions
import os
import json

ver = "0.2"
helpmsg = """
notgit ver: v0.2
Commands:
    notgit init: Create a .notgit folder in the current directory
    notgit save "msg": Saves current directory as a snapshot into -> .notgit
    notgit history: Shows all saved snapshots
    """


try:
    with open(".notgit/history.json", "r") as openn:
        hisfile = json.load(openn)
        openn.close()
except FileNotFoundError:
    hisfile = []

try:
    command = sys.argv[1]

    if command == "init":
        functions.init()
        print(f"notgit: Directory [{os.getcwd()}] intilized")
    
    elif command == "save":
        if functions.save(hisfile) == 'init=ok':
            print("notgit: took a snapshot!")
        else:
            print("notgit: initialize dir first")

    elif command == 'history':
        functions.history()

    else:
        print(f"notgit: command '{command}' not valid")
except IndexError:
    print("notgit: USE YOUR PROJECT DIRECTORY AS YOU CURRENT DIRECTORY ALWAYS!!")
    print(helpmsg)