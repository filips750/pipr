import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BANANA = (227, 207, 87)
DARKOCHID3 = (154, 50, 205)
WIDTHOFBOARD = 5
RESOLUTION = (900, 600)

WIN = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption('Gobblet Gobblers')

pygame.draw.circle(WIN, BANANA, (450, 300), 20)
# pygame.display.flip()


class Board():
    def __init__(self, resolution, surface, color, color_of_board, size=3):
        self._resolution = resolution
        self._size = size
        self._pawns_on_board = []
        self._pawns_out_of_board = []
        self._surface = surface
        self._color = color
        self._color_of_board = color_of_board
        self._square_size = min(resolution[0], resolution[1])//self._size

    def draw_a_board(self):
        WIN.fill(WHITE)
        for line in range(self._size+1):
            pos_begin = (self._square_size*line, 0)
            pos_end = (self._square_size*line, self._resolution[0])
            pygame.draw.line(self._surface, self._color_of_board, pos_begin, pos_end, WIDTHOFBOARD)
        for line in range(self._size+1):
            pos_begin = (0, self._square_size*line)
            pos_end = (self._resolution[1], self._square_size*line)
            pygame.draw.line(self._surface, self._color_of_board, pos_begin, pos_end, WIDTHOFBOARD)

        if self._pawns_on_board:
            for pawn in self._pawns_on_board:
                self.draw_pawn(pawn)
        pygame.display.update()

    def check_if_won_draw_or_lost(self):
        pass

    def move_a_pawn(self, pawn_to_move, new_coordinates):
        self._pawns_on_board.remove(pawn_to_move)
        pawn_to_move.set_coordinates(new_coordinates)
        self._pawns_on_board.append(pawn_to_move)

    def add_a_pawn(self, pawn_to_add, new_coordinates):
        pawn_to_add.set_coordinates(new_coordinates)
        self._pawns_on_board.append(pawn_to_add)
        # self._pawns_out_of_board.remove(pawn_to_add)
        # to do delete added pawn from pawns_out_of_board

    def pawns_on_board(self):
        return self._pawns_on_board

    def pawns_out_of_board(self):
        return self._pawns_out_of_board

    def draw_pawn(self, pawn):
        x = (pawn._coordinates[0]*self._square_size)+self._square_size//2
        y = (pawn._coordinates[1]*self._square_size)+self._square_size//2
        pygame.draw.circle(WIN, pawn._color, (x, y), pawn._size, pawn._size)


class Player():
    def __init__(self, name, score=0):
        self._name = name
        self._score = score


class Pawn():
    def __init__(self, size, coordinates, owner, color):
        self._size = size
        self._color = color
        self._coordinates = coordinates
        self._owner = owner

    def size(self):
        return self._size

    def set_coordinates(self, new_coordinates):
        self._coordinates = new_coordinates

    def coordinates(self):
        return self._coordinates


def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()

# pygame.transform.scale()


def main():
    draw_window()
    # to do update window every click
    run = True
    player_one = Player('Filip')
    mypawn = Pawn(27, (0, 0), player_one, DARKOCHID3)
    my_board = Board(RESOLUTION, WIN, WHITE, BLACK, 10)
    my_board.draw_a_board()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # pygame.draw.circle(WIN, BANANA, (450, 300), 100, 80)
        # pygame.draw.circle(WIN, DARKOCHID3, (50, 50), 40, 40)
        mousepos = pygame.mouse.get_pos()
        isclick = pygame.mouse.get_pressed()
        xnewpos = mousepos[0]//my_board._square_size
        ynewpos = mousepos[1]//my_board._square_size
        newpos = (xnewpos, ynewpos)
        if isclick[0]:
            my_board.add_a_pawn(Pawn(20, newpos, player_one, BANANA), newpos)
        my_board.draw_a_board()
        # print(mousepos + isclick)
        # pygame.draw.circle(WIN, DARKOCHID3, mousepos, 40, 40)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
