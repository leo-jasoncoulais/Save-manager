
from googledrive import GoogleClient
from local import LocalClient

from manage_games import manage_games
from backup_save import backup_save
from restore_save import restore_save

import os
from json import dump

def choose_cloud():

    print("\nChoose cloud service")

    for ele in ["1. Google Drive", "2. Dropbox", "3. OneDrive", "4. Box", "5. Local"]:
        print(ele)

    choice = input(": ")

    if not choice.isdigit():
        print("\nPlease enter valid option.")
        return choose_cloud()

    match int(choice):
        case 1:
            return "Google Drive"
        case 2:
            return "Dropbox"
        case 3:
            return "OneDrive"
        case 4:
            return "Box"
        case 5:
            return "Local"
        case _:
            print("\nPlease enter valid option.")
            return choose_cloud()

def main():

    drive_letter = os.environ.get("SystemDrive")
    current_user = os.environ.get("USERNAME")
    saves_folder = os.path.join(drive_letter,"\\","Users", current_user, "AppData", "Local")

    softwares = os.listdir(saves_folder)
    service = None
    
    while True:

        print("Welcome to Save Manager")

        if not os.path.exists("games.json"):
            with open("games.json", "w") as file:
                dump([], file)

        if not service:

            match choose_cloud():
                case "Google Drive":

                    client = GoogleClient(scopes=["https://www.googleapis.com/auth/drive"])
                    client.init()
                    service = client.get_service("drive", "v3")

                case "Dropbox":
                    pass
                case "OneDrive":
                    pass
                case "Box":
                    pass
                case "Local":
                    
                    client = LocalClient()
                    service = client.get_service()

        print("\nWhat do you want to do ?")

        for ele in ["1. Manage games", "2. Backup save", "3. Restore save", "4. Quit"]:
            print(ele)

        choice = input(": ")

        if not choice.isdigit():
            print("\nPlease enter valid option.")
            continue

        match int(choice):
            case 1:
                manage_games(games=softwares)
            case 2:
                backup_save(service=service, saves_folder=saves_folder)
            case 3:
                restore_save(saves_folder=saves_folder)
            case 4:
                break
            case _:
                print("\nPlease enter valid option.")
                continue

if __name__ == "__main__":
    main()
