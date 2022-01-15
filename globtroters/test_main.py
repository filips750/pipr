import pygame
from main import Board, Player, load_and_unpack_settings_yaml

colors, settings = load_and_unpack_settings_yaml


def test_Board_init():
    WIN = pygame.display.set_mode(settings['RESOLUTION'])
    player_one = Player('Filip', colors['DARKORCHID'])
    player_two = Player('Janusz', colors['BANANA'])
    player_one.add_pawns(3)
    player_two.add_pawns(3)
    my_board = Board(settings['RESOLUTION'], WIN, colors['WHITE'], colors['BLACK'], [player_one, player_two])
    assert my_board._players[0]._name == 'Filip'
    assert my_board._players[1]._name == 'Janusz'
    assert my_board._resolution == settings['RESOLUTION']
    assert my_board._color_of_board == colors['BLACK']
    assert my_board._players[0]._pawns[0]._size == settings['MULTIPLIEDSIZE']
    assert my_board._players[0]._pawns[3]._size == 2*settings['MULTIPLIEDSIZE']
    assert my_board._players[0]._pawns[6]._size == 3*settings['MULTIPLIEDSIZE']
    assert my_board._players[0]._pawns[0]._color == colors['DARKORCHID']


def test_get_biggest_pawn_by_coords():
    WIN = pygame.display.set_mode(settings['RESOLUTION'])
    player_one = Player('Filip', colors['DARKORCHID'])
    player_one.add_pawns(3)
    my_board = Board(settings['RESOLUTION'], WIN, colors['WHITE'], colors['BLACK'], [player_one])
    my_board.add_a_pawn(player_one, player_one._pawns[0], (2, 0))
    my_board.add_a_pawn(player_one, player_one._pawns[0], (2, 0))
    assert my_board._pawns_on_board[0]._coordinates == (2, 0)
    assert len(my_board._pawns_on_board) == 1
    assert len(player_one._pawns) == 8
    my_board.add_a_pawn(player_one, player_one._pawns[2], (2, 0))
    assert my_board.get_biggest_pawn_by_coords((2, 0))._size == settings['MULTIPLIEDSIZE']
    picked_pawn = my_board.pick_a_pawn((450, 100), 0)
    my_board.move_a_pawn(picked_pawn, (0, 2))
    assert my_board.get_biggest_pawn_by_coords((0, 2))._size == 2*['MULTIPLIEDSIZE']
    assert my_board._pawns_on_board[0]._coordinates == (2, 0)


def test_check_if_win_after_putting_a_pawn_over():
    WIN = pygame.display.set_mode(settings['RESOLUTION'])
    player_one = Player('Filip', colors['DARKORCHID'])
    player_two = Player('Janusz', colors['BANANA'])
    player_one.add_pawns(3)
    player_two.add_pawns(3)
    my_board = Board(settings['RESOLUTION'], WIN,  colors['WHITE'], colors['BLACK'], [player_one, player_two])
    my_board.add_a_pawn(player_one, player_one._pawns[0], (2, 0))
    my_board.add_a_pawn(player_one, player_one._pawns[0], (1, 1))
    my_board.add_a_pawn(player_two, player_two._pawns[4], (1, 1))
    my_board.add_a_pawn(player_one, player_one._pawns[0], (0, 2))
    assert my_board.check_if_won(3) is None


def test_check_if_win():
    WIN = pygame.display.set_mode(settings['RESOLUTION'])
    player_one = Player('Filip', colors['DARKORCHID'])
    player_two = Player('Janusz', colors['BANANA'])
    player_one.add_pawns(3)
    player_two.add_pawns(3)
    my_board = Board(settings['RESOLUTION'], WIN, colors['WHITE'], colors['BLACK'], [player_one, player_two])
    my_board.add_a_pawn(player_one, player_one._pawns[0], (2, 0))
    my_board.add_a_pawn(player_one, player_one._pawns[0], (1, 1))
    my_board.add_a_pawn(player_one, player_one._pawns[0], (0, 2))
    assert my_board.check_if_won(3) == player_one


def test_pickmove_a_pawn():
    WIN = pygame.display.set_mode(settings['RESOLUTION'])
    player_one = Player('Filip', colors['DARKORCHID'])
    player_one.add_pawns(3)
    my_board = Board(settings['RESOLUTION'], WIN, colors['WHITE'], colors['BLACK'], [player_one])
    my_board.add_a_pawn(player_one, player_one._pawns[0], (2, 0))
    assert my_board._pawns_on_board[0]._coordinates == (2, 0)
    picked_pawn = my_board.pick_a_pawn((450, 150), 0)
    my_board.move_a_pawn(picked_pawn, (0, 2))
    assert my_board._pawns_on_board[0]._coordinates == (0, 2)
