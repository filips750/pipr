from Play import play_game
from UI import ui


def main():
    """
    Main func.
    Gets list of players from ui function.
    If list of player exists calls play_game function.
    """
    list_of_players = ui()
    if list_of_players:
        play_game(list_of_players)


if __name__ == '__main__':
    main()
