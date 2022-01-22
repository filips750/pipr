import pygame
from unpack_settings import load_and_unpack_settings_yaml
import pygame
from Player import Player
from Board import Board
from UI import ui


def play_game(list_of_players):
    list_to_play = []
    for player in list_of_players:
        player[1] = player[1].upper()
        list_to_play.append(Player(player[0], player[1]))
    colors, settings = load_and_unpack_settings_yaml()
    WIN = pygame.display.set_mode(settings['RESOLUTION'])
    my_board = Board(settings['RESOLUTION'], WIN, colors['BLACK'], colors['WHITE'], list_to_play, 3)
    my_board.add_pawns_to_players(settings['NUMBEROFPAWNS'])
    turn = 0
    picked_pawn_from_board = None
    picked_pawn_from_set = None
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                continue
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()
                xnewpos = mousepos[0]//my_board._square_size
                ynewpos = mousepos[1]//my_board._square_size
                newpos = (xnewpos, ynewpos)
                if picked_pawn_from_set:
                    if my_board.add_a_pawn(my_board._players[turn], picked_pawn_from_set, newpos):
                        turn += 1
                        picked_pawn_from_set = None
                        continue
                if picked_pawn_from_board:
                    if my_board.move_a_pawn(picked_pawn_from_board, newpos):
                        turn += 1
                        picked_pawn_from_board = None
                        continue
                if mousepos[0] < my_board._board_size and not (picked_pawn_from_board or picked_pawn_from_set):
                    picked_pawn_from_board = my_board.pick_a_pawn(mousepos, turn)
                if mousepos[0] > my_board._board_size and not picked_pawn_from_board:
                    picked_pawn_from_set = my_board.pick_a_pawn(mousepos, turn)
            winner = my_board.check_if_won(settings['NUMBERINROWTOWIN'])
            if winner:
                winner._score += 1
                my_board.remove_all_pawns()
                winner = None
                my_board.add_pawns_to_players(settings['NUMBEROFPAWNS'])
            turn = turn % len(my_board._players)
            my_board.draw_a_board(turn)
        pygame.display.update()
    pygame.quit()