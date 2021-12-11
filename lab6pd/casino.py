from random import randint


class Casino:
    def __init__(self, players):
        self._players = players

    def throw_dices(self):
        diceees = []
        for dice in range(4):
            diceees.append(randint(1, 6))
        self._number_dices = diceees
        return self._number_dices

    def pick_winner(self):
        max_score = -1
        for player in self._players:
            Player.set_score(self)
            if self._score == max_score:
                winner = 'Gra nierozstrzygnięta'
            if self._score > max_score:
                max_score = self._score
                winner = player
        return winner._name


class Player(Casino):
    def __init__(self, name, dices=[], score=0):
        self._name = name
        self._dices = dices
        self._score = score

    def set_dices(self):
        return Casino.throw_dices(self)

    # def dices(self):
    #     return self._dices

    def score(dices):
        score_from_even_odd = 0
        score_from_set = 0
        my_list = [0, 0, 0, 0, 0, 0, 0]
        for number in dices:
            my_list[number] += 1
        max_element = 0
        my_iterator = 0
        for element in my_list:
            if element >= max_element:
                max_element = element
                number_of_dice = my_iterator
            my_iterator += 1

        for number in dices:
            if number % 2 == 0:
                is_even = True
            else:
                is_even = False
                break

        for number in dices:
            if number % 2 == 1:
                is_odd = True
            else:
                is_odd = False
                break
        if max_element == 2:
            score_from_set = 2 * number_of_dice
        if max_element == 3:
            score_from_set = 4 * number_of_dice
        if max_element == 3:
            score_from_set = 6 * number_of_dice
        if is_even:
            score_from_even_odd = sum(dices) + 2
        if is_odd:
            score_from_even_odd = sum(dices) + 3
        return max(score_from_even_odd, score_from_set)

    def set_score(self):
        score1 = Player.set_dices(self)
        self._score = Player.score(score1)


gracz_one = Player('Filip')
gracz_two = Player('Artór')
mojekasynko = Casino([gracz_one, gracz_two])
print(Casino.pick_winner(mojekasynko))
