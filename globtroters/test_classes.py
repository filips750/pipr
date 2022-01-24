import pygame
import pytest
from unpack_settings import (
    load_and_unpack_settings_yaml,
    check_if_settings_are_correct
)
from UI import check_if_color
from Player import Player
from Board import Board
from exceptions import (
    ColorInConfigIsNotATuple,
    MissingArgumentsConfigFile
)


def test_Board_init():
    colors, settings = load_and_unpack_settings_yaml()
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
    colors, settings = load_and_unpack_settings_yaml()
    WIN = pygame.display.set_mode(settings['RESOLUTION'])
    player_one = Player('Filip', colors['DARKORCHID'])
    player_one.add_pawns(3)
    my_board = Board(settings['RESOLUTION'], WIN, colors['WHITE'], colors['BLACK'], [player_one])
    my_board.add_a_pawn(player_one, player_one._pawns[0], (2, 0))
    my_board.add_a_pawn(player_one, player_one._pawns[0], (2, 0))
    assert my_board._pawns_on_board[0]._coordinates == (2, 0)
    assert len(my_board._pawns_on_board) == 1
    assert len(player_one._pawns) == 8
    my_board.add_a_pawn(player_one, player_one._pawns[0], (2, 0))
    assert my_board.get_biggest_pawn_by_coords((2, 0))._size == settings['MULTIPLIEDSIZE']
    picked_pawn = my_board.pick_a_pawn((450, 100), 0)
    my_board.move_a_pawn(picked_pawn, (0, 2))
    assert my_board.get_biggest_pawn_by_coords((0, 2))._size == settings['MULTIPLIEDSIZE']
    assert my_board._pawns_on_board[0]._coordinates == (0, 2)
    my_board.add_a_pawn(player_one, player_one._pawns[2], (0, 2))
    assert my_board.get_biggest_pawn_by_coords((0, 2))._size == 2*settings['MULTIPLIEDSIZE']


def test_check_if_win_after_putting_a_pawn_over():
    colors, settings = load_and_unpack_settings_yaml()
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
    colors, settings = load_and_unpack_settings_yaml()
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


def test_check_if_win_row():
    colors, settings = load_and_unpack_settings_yaml()
    WIN = pygame.display.set_mode(settings['RESOLUTION'])
    player_one = Player('Filip', colors['RED'])
    player_two = Player('Janusz', colors['BLUE'])
    player_one.add_pawns(3)
    player_two.add_pawns(3)
    my_board = Board(settings['RESOLUTION'], WIN, colors['WHITE'], colors['BLACK'], [player_one, player_two])
    my_board.add_a_pawn(player_one, player_one._pawns[0], (1, 0))
    my_board.add_a_pawn(player_one, player_one._pawns[0], (1, 1))
    my_board.add_a_pawn(player_one, player_one._pawns[0], (1, 2))
    assert my_board.check_if_won(3) == player_one


def test_pickmove_a_pawn():
    colors, settings = load_and_unpack_settings_yaml()
    WIN = pygame.display.set_mode(settings['RESOLUTION'])
    player_one = Player('Filip', colors['DARKORCHID'])
    player_one.add_pawns(3)
    my_board = Board(settings['RESOLUTION'], WIN, colors['WHITE'], colors['BLACK'], [player_one])
    my_board.add_a_pawn(player_one, player_one._pawns[0], (2, 0))
    assert my_board._pawns_on_board[0]._coordinates == (2, 0)
    picked_pawn = my_board.pick_a_pawn((450, 150), 0)
    my_board.move_a_pawn(picked_pawn, (0, 2))
    assert my_board._pawns_on_board[0]._coordinates == (0, 2)


def test_add_pawns_to_players():
    colors, settings = load_and_unpack_settings_yaml()
    WIN = pygame.display.set_mode(settings['RESOLUTION'])
    player_one = Player('Filip', colors['DARKORCHID'])
    player_two = Player('Janusz', colors['BLUE'])
    my_board = Board(settings['RESOLUTION'], WIN, colors['WHITE'], colors['BLACK'], [player_one, player_two])
    my_board.add_pawns_to_players(3)
    assert len(player_one._pawns) == 9
    assert len(player_two._pawns) == 9


def test_remove_all_players():
    colors, settings = load_and_unpack_settings_yaml()
    WIN = pygame.display.set_mode(settings['RESOLUTION'])
    player_one = Player('Filip', colors['DARKORCHID'])
    player_two = Player('Janusz', colors['BLUE'])
    my_board = Board(settings['RESOLUTION'], WIN, colors['WHITE'], colors['BLACK'], [player_one, player_two])
    my_board.add_pawns_to_players(3)
    my_board.add_a_pawn(player_one, player_one._pawns[0], (2, 0))
    my_board.add_a_pawn(player_one, player_one._pawns[0], (1, 0))
    my_board.add_a_pawn(player_one, player_one._pawns[0], (0, 0))
    assert my_board.check_if_won(3) == player_one
    my_board.remove_all_pawns()
    assert len(my_board._pawns_on_board) == 0
    assert len(player_one._pawns) == 0
    assert len(player_two._pawns) == 0


def test_check_if_color():
    colors, settings = load_and_unpack_settings_yaml()
    assert check_if_color("RED") is True
    assert check_if_color("123") is False
    assert check_if_color((192, 192, 192)) is False
    assert check_if_color('red') is False


def test_check_if_settings_are_correct():
    settings = {
        'colors': {
            "BLACK": '(0, 0, 0)',
            "WHITE": '(255, 255, 255)',
            "RED": '(255, 0, 0)',
            "BLUE": '(0, 0, 255)',
            "YELLOW": '(255, 255, 0)',
            "GREEN": '(0, 215, 0)',
            "CYAN": '(0, 215, 175)',
        },
        'RESOLUTION': '(1032, 600)',
        'FONT': 'Comic Sans',
        'FONTSIZE': 20,
        'WIDTHOFBOARD': 5,
        'MULTIPLIEDSIZE': 24,
        'NUMBERINROWTOWIN': 3,
        'NUMBEROFPAWNS': 3,
        'BOARDSIZE': 3
    }
    assert check_if_settings_are_correct(settings) is True


def test_check_if_settings_are_correct_float():
    settings = {
        'colors': {
            "BLACK": '(0, 0, 0)',
            "WHITE": '(255, 255, 255)',
            "RED": '(255, 0, 0)',
            "BLUE": '(0, 0, 255)',
            "YELLOW": '(255, 255, 0)',
            "GREEN": '(0, 215, 0)',
            "CYAN": '(0, 215, 175)',
        },
        'RESOLUTION': '(1032, 600)',
        'FONT': 'Comic Sans',
        'FONTSIZE': 20,
        'WIDTHOFBOARD': 5,
        'MULTIPLIEDSIZE': 24,
        'NUMBERINROWTOWIN': 3,
        'NUMBEROFPAWNS': 3,
        'BOARDSIZE': 3.5
    }
    assert check_if_settings_are_correct(settings) == 'BOARDSIZE'


def test_check_if_settings_are_correct_missing_argument():
    settings = {
        'colors': {
            "BLACK": '(0, 0, 0)',
            "WHITE": '(255, 255, 255)',
            "RED": '(255, 0, 0)',
            "BLUE": '(0, 0, 255)',
            "YELLOW": '(255, 255, 0)',
            "GREEN": '(0, 215, 0)',
            "CYAN": '(0, 215, 175)',
        },
        'RESOLUTION': '(1032, 600)',
        'FONT': 'Comic Sans',
        'FONTSIZE': 20,
        'WIDTHOFBOARD': 5,
        'MULTIPLIEDSIZE': 24,
        'NUMBERINROWTOWIN': 3,
        'NUMBEROFPAWNS': 3
    }
    with pytest.raises(MissingArgumentsConfigFile):
        check_if_settings_are_correct(settings)


def test_check_if_settings_are_correct_color_is_not_a_tuple():
    settings = {
        'colors': {
            "BLACK": [0, 0, 0],
            "WHITE": '(255, 255, 255)',
            "RED": '(255, 0, 0)',
            "BLUE": '(0, 0, 255)',
            "YELLOW": '(255, 255, 0)',
            "GREEN": '(0, 215, 0)',
            "CYAN": '(0, 215, 175)',
        },
        'RESOLUTION': '(1032, 600)',
        'FONT': 'Comic Sans',
        'FONTSIZE': 20,
        'WIDTHOFBOARD': 5,
        'MULTIPLIEDSIZE': 24,
        'NUMBERINROWTOWIN': 3,
        'NUMBEROFPAWNS': 3
    }
    with pytest.raises(ColorInConfigIsNotATuple):
        check_if_settings_are_correct(settings)


def test_check_resolution():
    settings1 = {
        'colors': {
            "BLACK": '(0, 0, 0)',
            "WHITE": '(255, 255, 255)',
            "RED": '(255, 0, 0)',
            "BLUE": '(0, 0, 255)',
            "YELLOW": '(255, 255, 0)',
            "GREEN": '(0, 215, 0)',
            "CYAN": '(0, 215, 175)',
        },
        'RESOLUTION': '(1032, 600, 300)',
        'FONT': 'Comic Sans',
        'FONTSIZE': 20,
        'WIDTHOFBOARD': 5,
        'MULTIPLIEDSIZE': 24,
        'NUMBERINROWTOWIN': 3,
        'NUMBEROFPAWNS': 3,
        'BOARDSIZE': 3
    }
    assert check_if_settings_are_correct(settings1) == 'RESOLUTION'
