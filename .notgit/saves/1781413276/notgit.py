import notgit_functions as functions
import os
import json
import sys

ver = "0.2"

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
    
    elif command == "save":
        if functions.save(hisfile) == 'ok':
            print("notgit: took a snapshot!")
        else:
            print("notgit: initialize dir first")

    elif command == 'history':
        functions.history()
    
    elif command == 'undo':
        if len(sys.argv) > 2:
            save = sys.argv[2]
        else:
            save = None
        functions.undo(save_id=save)

    else:
        print(f"notgit: command '{command}' not valid")
except IndexError:
    print("notgit: ")
    print("""
notgit ver: v0.2
Commands:
    notgit init: Create a .notgit folder in the current directory
    notgit save "msg": Saves current directory as a snapshot into -> .notgit
    notgit undo: revives old snapshot
    notgit history: Shows all saved snapshots
    """)#
# YOOOOO!!!!! hi back!