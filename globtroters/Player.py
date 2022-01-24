from Pawn import Pawn
from unpack_settings import load_and_unpack_settings_yaml


class Player():
    def __init__(self, name, color, score=0):
        """
        Creates instance of Player class.

        :param name: Name of the player
        :type name: str

        :param color: Color of the player's pawns
        :type color: tuple
        """
        self._name = name
        self._score = score
        self._pawns = []
        self._color = color
        self.setting = load_and_unpack_settings_yaml()[1]

    def add_pawns(self, number_of_pawns_to_add):
        """
        Add pawns to player
        """
        for size in range(1, 4):
            for pawn in range(number_of_pawns_to_add):
                self._pawns.append(Pawn(size*self.setting['MULTIPLIEDSIZE'], self._color, self))
