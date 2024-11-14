
import os
import shutil

def restore_save(saves_folder: str):

    print("\nRestore save")

    if not os.path.exists(saves_folder):
        print("\nSave folder not found.")

    saves = input("Move the save file here and press Enter. ")

    # Parse the path
    saves = saves.strip()
    saves = saves.replace('"', "")
    saves = saves.replace("'", "")

    if not os.path.exists(saves):
        print("\nSaves not found.")
        restore_save(saves_folder)
        return
    
    print("\nRestoring...")
    
    shutil.copy(saves, "saves.zip")
    shutil.unpack_archive("saves.zip", "saves")

    for save in os.listdir("saves"):
        shutil.rmtree(os.path.join(saves_folder, save), ignore_errors=True)
        shutil.copytree(os.path.join("saves", save), os.path.join(saves_folder, save))

    shutil.rmtree("saves")
    os.remove("saves.zip")

    print("\nSave restored!")
