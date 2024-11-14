
from json import load
import shutil
import os
from time import time
from googledrive import Service

def backup_save(service: Service, saves_folder: str):

    print("\nSaving...")

    if not os.path.exists(saves_folder):
        print("\nSave folder not found.")
        return

    timestamp = int(time())
    backup_folder = os.path.join(saves_folder, f"BACKUP_{timestamp}")

    with open("games.json", "r") as file:
        games = load(file)

    os.mkdir(backup_folder)

    for game in games:
        
        if not os.path.exists(os.path.join(saves_folder, game)):
            print(f"\n{game} not found.")
            continue

        shutil.copytree(os.path.join(saves_folder, game), os.path.join(backup_folder, game))
        print(f"\n{game} saved.")
        
    shutil.make_archive(backup_folder, 'zip', backup_folder)  
    service.upload(backup_folder+".zip")

    shutil.rmtree(backup_folder)
    os.remove(backup_folder+".zip")

    print("\nSave uploaded successfully!")
