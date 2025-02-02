import itertools
import random

class Enemy:
    id = itertools.count(0)
    def __init__(self):
        self._id = next(Enemy.id)

class Cultist(Enemy):
    def __init__(self):
        super().__init__()
        self._name = 'Cultist'
        self._hp = random.randint(42, 48)
        self._max_hp = self._hp

    def __repr__(self):
        return f'__repr__ for {self._name}, id: {self._id}'

    def summary(self):
        print(f'\n{self._name}')
        print(f'HP: {self._hp}/{self._max_hp}')

    def getName(self):
        return self._name

    def getHP(self):
        return self._hp
    
    def doDamage(self, damage):
        self._hp -= damage
        return self._hp

    def intent(self):
        intents = [state.ACTIONS[2], state.ACTIONS[3]]
        attackValues = 6
        intent = random.randint(1, 2)
        attack = random.choices(attackValues, weights=[1, 2, 6, 1])
        for i in attack:
            res = i
        block = random.choices(blockValues, weights=[1, 8, 3, 2])
        for i in block:
            res = i
        if intent == 1:
            return intent, res
        else:
            return intent, res

