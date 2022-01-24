import pygame
from unpack_settings import load_and_unpack_settings_yaml
from Player import Player
from Board import Board


def play_game(list_of_players):
    """
    Makes Board instance with 'RESOLUTION' and colors,
    and uses it to play game, based on list_of_players.
    Starts game by adding 'NUMBEROFPAWNS' pawns.
    'NUMBEROFPAWNS' and colors can be changed in config_file.json
    After any movements calls check_if_win function.
    If there is winner clears board and adds score and pawns.
    """
    list_to_play = []
    for player in list_of_players:
        player[1] = player[1].upper()
        list_to_play.append(Player(player[0], player[1]))
    colors, settings = load_and_unpack_settings_yaml()
    WIN = pygame.display.set_mode(settings['RESOLUTION'])
    board = Board(settings['RESOLUTION'], WIN, colors['SURFACE'], colors['BOARDCOLOR'], list_to_play, settings['BOARDSIZE'])
    board.add_pawns_to_players(settings['NUMBEROFPAWNS'])
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
                xnewpos = mousepos[0]//board._square_size
                ynewpos = mousepos[1]//board._square_size
                newpos = (xnewpos, ynewpos)
                picked_pawn = picked_pawn_from_board or picked_pawn_from_set
                if picked_pawn_from_set:
                    if board.add_a_pawn(board._players[turn], picked_pawn_from_set, newpos):
                        turn += 1
                        picked_pawn_from_set = None
                        continue
                if picked_pawn_from_board:
                    if board.move_a_pawn(picked_pawn_from_board, newpos):
                        turn += 1
                        picked_pawn_from_board = None
                        continue
                if mousepos[0] < board._board_size and not picked_pawn:
                    picked_pawn_from_board = board.pick_a_pawn(mousepos, turn)
                if mousepos[0] > board._board_size and not picked_pawn_from_board:
                    picked_pawn_from_set = board.pick_a_pawn(mousepos, turn)
            winner = board.check_if_won(settings['NUMBERINROWTOWIN'])
            if winner:
                winner._score += 1
                board.remove_all_pawns()
                winner = None
                board.add_pawns_to_players(settings['NUMBEROFPAWNS'])
            turn = turn % len(board._players)
            board.draw_a_board(turn)
        pygame.display.update()
    pygame.quit()
