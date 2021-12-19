import pytest
from casino import Casino, Player
from pytest import MonkeyPatch
from casino_exceptions import (
    NoPlayersError,
    PlayersListError,
    AddPlayerError,
    DeletePlayerError
)


def test_roll_dices(monkeypatch: MonkeyPatch):
    player = Player('Bartek')

    def monkey_roll_dices(p, f):
        return 1
    monkeypatch.setattr('casino.randint', monkey_roll_dices)
    player.throw_dices()
    assert player._dices == [1, 1, 1, 1]


def test_full_mock(monkeypatch: MonkeyPatch):
    player = Player('Filip')

    def mock_throw(arg):
        return [1, 2, 3, 4]
    monkeypatch.setattr('casino.Player.dices', mock_throw)
    assert Player.dices(player) == [1, 2, 3, 4]


def test_score_odds(monkeypatch: MonkeyPatch):
    player_one = Player('player_one')
    casino = Casino([player_one])

    def mock_throw(arg):
        return [1, 3, 5, 3]
    monkeypatch.setattr('casino.Player.dices', mock_throw)
    result = casino.pick_winner()
    assert result.score() == 15


def test_pick_winner(monkeypatch: MonkeyPatch):
    player_one = Player('player_one')
    player_one._dices = [4, 4, 4, 4]
    player_two = Player('player_two')
    player_two._dices = [2, 2, 2, 2]
    casino = Casino([player_one, player_two])
    result = casino.pick_winner()
    assert result._name == 'player_one'
    assert result._dices == [4, 4, 4, 4]
    assert result.score() == 24


def test_winner_tie():
    player_one = Player('player_one')
    player_one._dices = [2, 2, 2, 6]
    player_two = Player('player_two')
    player_two._dices = [2, 6, 2, 2]
    casino = Casino([player_one, player_two])
    assert casino.pick_winner() == 'Game unresolved'


def test_init_Casino():
    player_one = Player('player_one')
    casino = Casino([player_one])
    assert casino._players[0] == player_one
    assert casino._players[0]._name == 'player_one'


def test_no_players_casino():
    with pytest.raises(NoPlayersError):
        casino = Casino()


def test_casino_players_list_error():
    player_one = Player('Filip')
    player_two = Player('Bartek')
    with pytest.raises(PlayersListError):
        casino = Casino([player_one, player_two, player_one])


def test_casino_add_player():
    player_one = Player('Filip')
    player_two = Player('Bartek')
    casino = Casino([player_one])
    assert casino._players == [player_one]
    Casino.add_player(casino, [player_two])
    assert casino._players == [player_one, player_two]


def test_casino_AddPlayerError():
    player_one = Player('Filip')
    casino = Casino([player_one])
    with pytest.raises(AddPlayerError):
        casino.add_player([player_one])


def test_casino_delete_player():
    player_one = Player('Filip')
    casino = Casino([player_one])
    assert casino._players == [player_one]
    casino.delete_player([player_one])
    assert casino._players == []


def test_casino_DeletePlayerError():
    player_one = Player('Filip')
    player_two = Player('Bartek')
    casino = Casino([player_one])
    assert casino._players == [player_one]
    with pytest.raises(DeletePlayerError):
        casino.delete_player([player_two])


def test_casino_NoPlayersError():
    with pytest.raises(NoPlayersError):
        casino = Casino([])
