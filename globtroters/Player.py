from Pawn import Pawn
from unpack_settings import load_and_unpack_settings_yaml

colors, settings = load_and_unpack_settings_yaml()


class Player():
    def __init__(self, name, color, score=0):
        # to do move picked pawn to this function?
        self._name = name
        self._score = score
        self._pawns = []
        self._color = color
        self._picked_pawn = None

    def add_pawns(self, number_of_pawns_to_add):
        for size in range(1, 4):
            for pawn in range(number_of_pawns_to_add):
                self._pawns.append(Pawn(size*settings['MULTIPLIEDSIZE'], self._color, self))


    def set_picked_pawn(self, pawn_to_pick):
        self._picked_pawn = pawn_to_pick
