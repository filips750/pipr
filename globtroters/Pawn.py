class Pawn():
    def __init__(self, size, color, owner, coordinates=None):
        """
        Creates instance of pawn.

        :param size: An integer from 1-3 describing a size of pawn
        If 'MULTIPLIEDSIZE' in config yaml is higher than 1,
        then drawn pawn will have radius of size*'MULTIPLIEDSIZE'
        :type size: int

        :param color: Color of the pawn
        :type color: tuple

        :param owner: Owner of a pawn
        :type owner: Player object
        """
        self._size = size
        self._color = color
        self._owner = owner
        if coordinates:
            self._coordinates = coordinates

    def set_coordinates(self, new_coordinates):
        self._coordinates = new_coordinates

    def coordinates(self):
        return self._coordinates
