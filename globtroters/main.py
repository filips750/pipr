import pygame
from Play import play_game
from UI import ui


pygame.init()


def main():
    list_of_players = ui()
    if list_of_players:
        play_game(list_of_players)


if __name__ == '__main__':
    main()
