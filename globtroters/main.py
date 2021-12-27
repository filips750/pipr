import pygame


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BANANA = (227, 207, 87)
DARKOCHID3 = (154, 50, 205)
WIDTHOFBOARD = 5
RESOLUTION = (1100, 600)

WIN = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption('Gobblet Gobblers')

pygame.draw.circle(WIN, BANANA, (450, 300), 20)
# pygame.display.flip()


class Board():
    def __init__(self, resolution, surface, color, color_of_board, players, size=3):
        self._resolution = resolution
        self._size = size
        self._pawns_on_board = []
        self._pawns_out_of_board = []
        self._surface = surface
        self._color = color
        self._color_of_board = color_of_board
        self._players = players
        self._square_size = min(resolution[0], resolution[1])//self._size

    def draw_a_board(self, turn=0):
        WIN.fill(WHITE)
        for line in range(1, self._size):
            pos_begin = (self._square_size*line, 0)
            pos_end = (self._square_size*line, self._resolution[0])
            pygame.draw.line(self._surface, self._color_of_board, pos_begin, pos_end, WIDTHOFBOARD)
        for line in range(1, self._size):
            pos_begin = (0, self._square_size*line)
            pos_end = (self._resolution[1], self._square_size*line)
            pygame.draw.line(self._surface, self._color_of_board, pos_begin, pos_end, WIDTHOFBOARD)

        if self._pawns_on_board:
            for pawn in self._pawns_on_board:
                self.draw_pawn(pawn)
        height_to_blit = 0

        pygame.font.init()
        my_font = pygame.font.SysFont('Comic Sans', 20)

        for player in self._players:
            string_to_print = f'The score of {player._name} is {player._score}'
            txt = my_font.render(string_to_print, True, BLACK)
            self._surface.blit(txt, (605, height_to_blit))
            height_to_blit += 30
        string_to_print = f"It's {self._players[turn]._name} move"
        height_to_blit += 30
        txt = my_font.render(string_to_print, True, BLACK)
        self._surface.blit(txt, (605, height_to_blit))
        height_to_blit += 90
        for pawn in self._players[turn]._pawns:
            if pawn._size == 10:
                new_coordinates = (620, height_to_blit)
                pawn.set_coordinates(new_coordinates)
                self.draw_pawn_by_coords(pawn)
            if pawn._size == 20:
                new_coordinates = (700, height_to_blit)
                pawn.set_coordinates(new_coordinates)
                self.draw_pawn_by_coords(pawn)
            if pawn._size == 30:
                new_coordinates = (780, height_to_blit)
                pawn.set_coordinates(new_coordinates)
                self.draw_pawn_by_coords(pawn)
        pygame.display.update()

    def check_if_won(self, number_in_row_to_win):
        currently_check = None
        number_in_row = 1
        for x_axis in range(self._size):
            for y_axis in range(self._size):
                pawn = self.get_biggest_pawn_by_coords((x_axis, y_axis))
                if pawn:
                    if currently_check == pawn._owner:
                        number_in_row += 1
                        if number_in_row_to_win == number_in_row:
                            return pawn._owner
                    else:
                        currently_check = pawn._owner
                        number_in_row = 1

                else:
                    currently_check = None

        currently_check = None
        number_in_row = 1

        for y_axis in range(self._size):
            for x_axis in range(self._size):
                pawn = self.get_biggest_pawn_by_coords((x_axis, y_axis))
                if pawn:
                    if currently_check == pawn._owner:
                        number_in_row += 1
                        if number_in_row_to_win == number_in_row:
                            return pawn._owner
                    else:
                        currently_check = pawn._owner
                        number_in_row = 1
                else:
                    currently_check = None

        currently_check = None
        number_in_row = 1

        for xy_axis in range(self._size):
            pawn = self.get_biggest_pawn_by_coords((x_axis, y_axis))
            if pawn:
                if currently_check == pawn._owner:
                    number_in_row += 1
                    if number_in_row_to_win == number_in_row:
                        return pawn._owner
                else:
                    currently_check = pawn._owner
                    number_in_row = 1
            else:
                currently_check = None

        currently_check = None
        number_in_row = 1

        for xy_axis in range(self._size):
            pawn = self.get_biggest_pawn_by_coords((self._size-xy_axis-1, xy_axis))
            if pawn:
                if currently_check == pawn._owner:
                    number_in_row += 1
                    if number_in_row_to_win == number_in_row:
                        return pawn._owner
                else:
                    currently_check = pawn._owner
                    number_in_row = 1
            else:
                currently_check = None


    def move_a_pawn(self, pawn_to_move, new_coordinates):
        self._pawns_on_board.remove(pawn_to_move)
        pawn_to_move.set_coordinates(new_coordinates)
        self._pawns_on_board.append(pawn_to_move)

    def add_a_pawn(self, player, pawn_to_add, new_coordinates):
        if self.compare_size_of_pawns(pawn_to_add, new_coordinates):
            pawn_to_add.set_coordinates(new_coordinates)
            self._pawns_on_board.append(pawn_to_add)
            player._pawns.remove(pawn_to_add)
        # self._pawns_out_of_board.remove(pawn_to_add)
        # to do delete added pawn from pawns_out_of_board

    def compare_size_of_pawns(self, pawn_to_add, new_coordinates):
        pawn = self.get_biggest_pawn_by_coords(new_coordinates)
        if pawn is None:
            return True
        if pawn_to_add._size > pawn._size:
            return True
        else:
            return False

    def get_biggest_pawn_by_coords(self, coords):
        possible_pawns = []
        for pawn in self._pawns_on_board:
            if pawn._coordinates == coords:
                possible_pawns.append(pawn)
        max_size = 0
        for pawn in possible_pawns:
            max_size = max(max_size, pawn._size)
        for pawn in possible_pawns:
            if max_size == pawn._size:
                return pawn

    def pawns_out_of_board(self):
        return self._pawns_out_of_board

    def draw_pawn(self, pawn):
        x = (pawn._coordinates[0]*self._square_size)+self._square_size//2
        y = (pawn._coordinates[1]*self._square_size)+self._square_size//2
        pygame.draw.circle(WIN, pawn._color, (x, y), pawn._size, pawn._size)

    def draw_pawn_by_coords(self, pawn):
        x = pawn._coordinates[0]
        y = pawn._coordinates[1]
        pygame.draw.circle(WIN, pawn._color, (x, y), pawn._size, pawn._size)

class Player():
    def __init__(self, name, color, score=0):
        # to do fix problem with data assignment
        self._name = name
        self._score = score
        self._pawns = []
        self._color = color

    def add_pawns(self, number_of_pawns_to_add):
        for size in range(1, 4):
            for pawn in range(number_of_pawns_to_add):
                self._pawns.append(Pawn(size*10, self._color, self))


class Pawn():
    def __init__(self, size, color, owner, coordinates=None):
        self._size = size
        self._color = color
        if coordinates:
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
    player_one = Player('Filip', DARKOCHID3)
    player_two = Player('Najlepszy ziomek', BANANA)
    player_one.add_pawns(3)
    player_two.add_pawns(3)
    my_board = Board(RESOLUTION, WIN, WHITE, BLACK, [player_one, player_two], 3)
    my_board.draw_a_board()
    turn = 0
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # remember about situation when something gets off the board
            mousepos = pygame.mouse.get_pos()
            isclick = pygame.mouse.get_pressed()
            xnewpos = mousepos[0]//my_board._square_size
            ynewpos = mousepos[1]//my_board._square_size
            newpos = (xnewpos, ynewpos)
            if my_board._players[turn]._pawns:
                mousepos = pygame.mouse.get_pos()
                isclick = pygame.mouse.get_pressed()
                xnewpos = mousepos[0]//my_board._square_size
                ynewpos = mousepos[1]//my_board._square_size
                newpos = (xnewpos, ynewpos)
                if isclick[0] and xnewpos < my_board._size and ynewpos < my_board._size:
                    my_board.add_a_pawn(my_board._players[turn], my_board._players[turn]._pawns[0], newpos)
                    turn += 1
            turn = turn % len(my_board._players)
            winner = my_board.check_if_won(3)
            if winner:
                winner._score += 1
            my_board.draw_a_board(turn)

        # print(mousepos + isclick)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
