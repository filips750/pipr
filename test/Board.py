import pygame
from unpack_settings import load_and_unpack_settings_yaml


class Board():
    def __init__(self, resolution, surface, color, color_of_board, players, size=3):
        self._resolution = resolution
        self._size = size
        self._pawns_on_board = []
        self._surface = surface
        self._color = color
        self._color_of_board = color_of_board
        self._players = players
        self._board_size = min(resolution[0], resolution[1])
        self._square_size = self._board_size//self._size
        self._height_blit = 5
        self._picked_pawn = None
        self.colors = load_and_unpack_settings_yaml()[0]
        self.settings = load_and_unpack_settings_yaml()[1]

    def draw_a_board(self, turn=0):
        self._surface.fill((self._color))
        for line in range(1, self._size):
            pos_begin = (self._square_size*line, 0)
            pos_end = (self._square_size*line, self._resolution[0])
            pygame.draw.line(self._surface, self._color_of_board, pos_begin, pos_end, self.settings['WIDTHOFBOARD'])
        for line in range(1, self._size):
            pos_begin = (0, self._square_size*line)
            pos_end = (self._resolution[1], self._square_size*line)
            pygame.draw.line(self._surface, self._color_of_board, pos_begin, pos_end, self.settings['WIDTHOFBOARD'])

        if self._pawns_on_board:
            for pawn in self._pawns_on_board:
                self.draw_pawn(pawn, True)
        self._height_blit = 0

        pygame.font.init()
        my_font = pygame.font.SysFont(self.settings['FONT'], self.settings['FONTSIZE'])

        for player in self._players:
            string_to_print = f'The score of {player._name} is {player._score}'
            txt = my_font.render(string_to_print, True, self._color_of_board)
            self._surface.blit(txt, (self._board_size + 10, self._height_blit))
            self._height_blit += 30
        string_to_print = f"It's {self._players[turn]._name} move"
        self._height_blit += 30
        txt = my_font.render(string_to_print, True, self._color_of_board)
        self._surface.blit(txt, (self._board_size + 10, self._height_blit))
        self._height_blit += 90
        for pawn in self._players[turn]._pawns:
            if pawn._size == self.settings['MULTIPLIEDSIZE']:
                new_coordinates = (self._board_size + 4*self.settings['MULTIPLIEDSIZE'], self._height_blit)
                pawn.set_coordinates(new_coordinates)
                self.draw_pawn(pawn, False)
            if pawn._size == 2*self.settings['MULTIPLIEDSIZE']:
                new_coordinates = (self._board_size + 8*self.settings['MULTIPLIEDSIZE'], self._height_blit)
                pawn.set_coordinates(new_coordinates)
                self.draw_pawn(pawn, False)
            if pawn._size == 3*self.settings['MULTIPLIEDSIZE']:
                new_coordinates = (self._board_size + 14*self.settings['MULTIPLIEDSIZE'], self._height_blit)
                pawn.set_coordinates(new_coordinates)
                self.draw_pawn(pawn, False)
        if self._picked_pawn:
            for colorname, color in self.colors.items():
                if self._picked_pawn._color == colorname:
                    colornametp = colorname
                    break
            sizetp = self._picked_pawn._size // self.settings['MULTIPLIEDSIZE']
            string_to_print = f"The picked pawn is {colornametp}, size:{sizetp}"
            self._height_blit += 90
            txt = my_font.render(string_to_print, True, self._color_of_board)
            self._surface.blit(txt, (self._board_size + 10, self._height_blit))
            self._height_blit -= 90
        else:
            string_to_print = "No picked pawn"
            self._height_blit += 90
            txt = my_font.render(string_to_print, True, self._color_of_board)
            self._surface.blit(txt, (self._board_size + 10, self._height_blit))
            self._height_blit -= 90
        pygame.display.update()

    def check_if_won(self, number_in_row_to_win):
        for x_axis in range(self._size):
            number_in_row = 1
            currently_check = None
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
                    number_in_row = 1

        for y_axis in range(self._size):
            number_in_row = 1
            currently_check = None
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
                    number_in_row = 1

        currently_check = None
        number_in_row = 1

        for xy_axis in range(self._size):
            pawn = self.get_biggest_pawn_by_coords((xy_axis, xy_axis))
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
                number_in_row = 1

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
                number_in_row = 1

    def move_a_pawn(self, pawn_to_move, new_coordinates):
        if pawn_to_move and new_coordinates[0] < self._size:
            if self.compare_size_of_pawns(pawn_to_move, new_coordinates):
                pawn_to_move.set_coordinates(new_coordinates)
                self._pawns_on_board.append(pawn_to_move)
                self._picked_pawn = None
                return True

    def add_a_pawn(self, player, pawn_to_add, new_coordinates):
        if pawn_to_add and new_coordinates[0] < self._size:
            if self.compare_size_of_pawns(pawn_to_add, new_coordinates):
                pawn_to_add.set_coordinates(new_coordinates)
                self._pawns_on_board.append(pawn_to_add)
                player._pawns.remove(pawn_to_add)
                self._picked_pawn = None
                return True

    def compare_size_of_pawns(self, pawn_to_add, new_coordinates):
        pawn = self.get_biggest_pawn_by_coords(new_coordinates)
        if pawn is None or pawn_to_add._size > pawn._size:
            return True
        else:
            return False

    def get_pawn_by_size(self, size, turn):
        for pawn in self._players[turn]._pawns:
            if pawn._size == size:
                return pawn
        else:
            return None

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

    def draw_pawn(self, pawn, on_board):
        if on_board:
            x = (pawn._coordinates[0]*self._square_size)+self._square_size//2
            y = (pawn._coordinates[1]*self._square_size)+self._square_size//2
        else:
            x = pawn._coordinates[0]
            y = pawn._coordinates[1]
        pygame.draw.circle(self._surface, pawn._color, (x, y), pawn._size, pawn._size)

    def pick_a_pawn(self, coords, turn):
        xnewpos = coords[0]//self._square_size
        ynewpos = coords[1]//self._square_size
        newpos = (xnewpos, ynewpos)
        if coords[0] <= self._board_size:
            pawn = self.get_biggest_pawn_by_coords(newpos)
            if pawn:
                self._pawns_on_board.remove(pawn)
                self._picked_pawn = pawn
                return pawn
        if self._height_blit-30 < coords[1] < self._height_blit+30:
            if self._board_size < coords[0] < self._board_size + self.settings['MULTIPLIEDSIZE']*6:
                pawn = self.get_pawn_by_size(self.settings['MULTIPLIEDSIZE'], turn)
                self._picked_pawn = pawn
                return pawn
            elif self._board_size + self.settings['MULTIPLIEDSIZE']*6 < coords[0] < self._board_size + self.settings['MULTIPLIEDSIZE']*10:
                pawn = self.get_pawn_by_size(self.settings['MULTIPLIEDSIZE']*2, turn)
                self._picked_pawn = pawn
                return pawn
            elif self._board_size + self.settings['MULTIPLIEDSIZE']*11 < coords[0] < self._board_size + self.settings['MULTIPLIEDSIZE']*18:
                pawn = self.get_pawn_by_size(self.settings['MULTIPLIEDSIZE']*3, turn)
                self._picked_pawn = pawn
                return pawn
        else:
            self._picked_pawn = None
            return None

    def add_pawns_to_players(self, number_of_pawns):
        for player in self._players:
            player.add_pawns(number_of_pawns)

    def remove_all_pawns(self):
        self._pawns_on_board.clear()
        for player in self._players:
            player._pawns.clear()
