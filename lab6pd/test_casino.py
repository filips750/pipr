from casino import Casino, Player
from pytest import MonkeyPatch

def test_something(monkeypatch):
    def fake_dices():
        return 1
    monkeypatch.setattr('classes.randint', fake_dices())
    gracz_one = Player('Filip')
    gracz_two = Player('Artór')
    mojekasynko = Casino([gracz_one, gracz_two])
    assert Casino.play_game(mojekasynko)) == 
