class Pawn():
    def __init__(self, size, color, owner, coordinates=None):
        self._size = size
        self._color = color
        self._owner = owner
        if coordinates:
            self._coordinates = coordinates

    def set_coordinates(self, new_coordinates):
        self._coordinates = new_coordinates

    def coordinates(self):
        return self._coordinates
