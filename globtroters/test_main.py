import pygame
from main import Board, Player, Pawn
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BANANA = (227, 207, 87)
DARKOCHID3 = (154, 50, 205)
WIDTHOFBOARD = 5
RESOLUTION = (900, 600)
WIN = pygame.display.set_mode(RESOLUTION)


def test_Board_init():
    player_one = Player('Filip', DARKOCHID3)
    player_two = Player('Janusz', BANANA)
    player_one.add_pawns(3)
    player_two.add_pawns(3)
    my_board = Board(RESOLUTION, WIN, WHITE, BLACK, [player_one, player_two], 3)
    assert my_board._players[0]._name == 'Filip'
    assert my_board._players[1]._name == 'Janusz'
    assert my_board._resolution == (900, 600)
    assert my_board._color_of_board == BLACK
    assert my_board._players[0]._pawns[0]._size == 7
    assert my_board._players[0]._pawns[3]._size == 14
    assert my_board._players[0]._pawns[6]._size == 21
    assert my_board._players[0]._pawns[0]._color == DARKOCHID3

def test_check_if_win_after_putting_a_pawn_over():
    player_one = Player('Filip', DARKOCHID3)
    player_two = Player('Janusz', BANANA)
    player_one.add_pawns(3)
    player_two.add_pawns(3)
    my_board = Board(RESOLUTION, WIN, WHITE, BLACK, [player_one, player_two], 3)
    my_board.add_a_pawn(player_one, player_one._pawns[0], (2, 0))
    my_board.add_a_pawn(player_one, player_one._pawns[0], (1, 1))
    my_board.add_a_pawn(player_two, player_two._pawns[4], (1, 1))
    my_board.add_a_pawn(player_one, player_one._pawns[0], (0, 2))
    assert my_board.check_if_won(3) == None

def test_check_if_win():
    player_one = Player('Filip', DARKOCHID3)
    player_two = Player('Janusz', BANANA)
    player_one.add_pawns(3)
    player_two.add_pawns(3)
    my_board = Board(RESOLUTION, WIN, WHITE, BLACK, [player_one, player_two], 3)
    my_board.add_a_pawn(player_one, player_one._pawns[0], (2, 0))
    my_board.add_a_pawn(player_one, player_one._pawns[0], (1, 1))
    my_board.add_a_pawn(player_one, player_one._pawns[0], (0, 2))
    assert my_board.check_if_won(3) == player_one