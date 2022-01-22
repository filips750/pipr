import pygame
from globtroters.classes.Board import Board
from globtroters.classes.Player import Player

from globtroters.unpack_settings import load_and_unpack_settings_yaml


def main():
    colors, settings = load_and_unpack_settings_yaml()
    WIN = pygame.display.set_mode(settings['RESOLUTION'])
    pygame.display.set_caption('Gobblet Gobblers')
    run = True
    player_one = Player('Filip', colors['DARKORCHID'])
    player_two = Player('Najlepszy ziomek', colors['TAN'])
    player_one.add_pawns(2)
    player_two.add_pawns(2)
    my_board = Board(settings['RESOLUTION'], WIN, colors['BLACK'], colors['WHITE'], [player_one, player_two], 3)
    turn = 0
    picked_pawn_from_board = None
    picked_pawn_from_set = None
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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
            winner = my_board.check_if_won(3)
            if winner:
                winner._score += 1
                my_board.remove_all_pawns()
                winner = None
                player_one.add_pawns(3)
                player_two.add_pawns(3)
            turn = turn % len(my_board._players)
            my_board.draw_a_board(turn)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
