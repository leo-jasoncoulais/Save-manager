
from json import load, dump

def add_game(games: list[str]):

    print("\nAdd game")
    
    for i, game in enumerate(games):
        print(f"{i+1}. {game}")

    game = input("Game ID: ")

    if not game.isdigit():
        print("\nPlease enter valid ID.")
        add_game(games)
        return
    
    game = int(game)
    
    if not 1 <= game <= len(games):
        print("\nPlease enter valid ID.")
        add_game(games)
        return
    
    with open("games.json", "r") as file:
        data = load(file)

    if games[game-1] in data:
        print("\nGame is already registed.")
        add_game(games)
        return
    
    data.append(games[game-1])

    with open("games.json", "w") as file:
        dump(data, file)

    print("Game added!")

def remove_game():

    print("\nRemove game")

    with open("games.json", "r") as file:
        data = load(file)
    
    for i, game in enumerate(data):
        print(f"{i+1}. {game}")

    game = input("Game ID: ")

    if not game.isdigit():
        print("\nPlease enter valid ID.")
        remove_game()
        return
    
    game = int(game)
    
    if not 1 <= game <= len(data):
        print("\nPlease enter valid ID.")
        remove_game()
        return
    
    data.pop(game-1)

    with open("games.json", "w") as file:
        dump(data, file)

    print("\nGame removed!")

def manage_games(games: list[str]):

    while True:
        print("\nManage games")
        for ele in ["1. Add a game", "2. Remove a game", "3. Quit"]:
            print(ele)
        
        choice = input(": ")

        if not choice.isdigit():
            print("\nPlease enter valid option.")
            continue

        match int(choice):
            case 1:
                add_game(games)
            case 2:
                remove_game()
            case 3:
                break
            case _:
                print("\nPlease enter valid option.")
                continue
