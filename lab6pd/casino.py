from random import randint
from casino_exceptions import (
    NoPlayersError,
    PlayersListError,
    AddPlayerError,
    DeletePlayerError
)


class Casino:
    """
    Class Casino. Contains attributes:
    :param: _players
    :type _player: list
    """

    def __init__(self, players=None):
        """
        Creates instance of casino

        Raises NoPlayersError if there are no players
        Raises PlayersListError if the players are repeating
        """
        if players:
            self._players = players
        else:
            raise NoPlayersError
        for player in players:
            if players.count(player) > 1:
                raise PlayersListError()

    def throw_dices(self):
        """
        Returns a list of four randomly picked numbers from one to six
        """
        diceees = []
        for dice in range(4):
            diceees.append(randint(1, 6))
        self._dices = diceees
        return self._dices

    def pick_winner(self):
        """
        Picks winner based on the score of the player.
        If two or more players have the same score then returns string 'Game unresolved'
        """
        max_score = 0
        for player in self._players:
            Player.set_score(player)
            if player._score == max_score:
                winner = 'Game unresolved'
            if player._score > max_score:
                max_score = player._score
                winner = player
        return winner

    def add_player(self, players_to_add):
        """
        Adds players to casino.
        If the players are repeating then raises AddPlayerError
        """
        for player in players_to_add:
            if player in self._players:
                raise AddPlayerError()
            self._players.append(player)

    def delete_player(self, players_to_delete):
        """
        Removes players from the casino.
        If the players aren't in the casino raise DeletePlayerError
        """
        for player in players_to_delete:
            if player in self._players:
                self._players.remove(player)
            else:
                raise DeletePlayerError()


class Player(Casino):
    def __init__(self, name=None):
        """
        Class Casino. Contain attributes:
        :param: _name
        "type name: str
        :param: _dices
        "type name: list
        :param: _score
        "type name: int
        """
        self._name = name
        self._dices = []
        self._score = 0

    def dices(self):
        """
        Sets the value of dices to thrown dices
        """
        self._dices = Casino.throw_dices(self)

    def score(self):
        """
        Returns the score of a player based on dices
        """
        score_from_even_odd = 0
        score_from_set = 0
        my_list = [0, 0, 0, 0, 0, 0, 0]
        for number in self._dices:
            my_list[number] += 1
        max_element = 0
        my_iterator = 0
        for element in my_list:
            if element >= max_element:
                max_element = element
                number_of_dice = my_iterator
            my_iterator += 1

        for number in self._dices:
            if number % 2 == 0:
                is_even = True
            else:
                is_even = False
                break

        for number in self._dices:
            if number % 2 == 1:
                is_odd = True
            else:
                is_odd = False
                break
        if max_element == 2:
            score_from_set = 2 * number_of_dice
        if max_element == 3:
            score_from_set = 4 * number_of_dice
        if max_element == 4:
            score_from_set = 6 * number_of_dice
        if is_even:
            score_from_even_odd = sum(self._dices) + 2
        if is_odd:
            score_from_even_odd = sum(self._dices) + 3
        return max(score_from_even_odd, score_from_set)

    def set_score(self):
        """
        Sets dices if the _dices are None type
        Sets score based on the function score
        """
        if not self._dices:
            self._dices = Player.dices(self)
        self._score = Player.score(self)
