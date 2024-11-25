import random


class Die:
    def __init__(self):
        self._value = None

    def roll_die(self):
        print('Rolling die...')
        random_value = random.randint(1,6)
        print(f'The die value is: {random_value}')
        self._value = random_value
        return  self._value


class Player:
    def __init__(self, die:Die, is_computer=False):
        self._is_computer = is_computer
        self._counter = 10
        self._die = die

    @property
    def counter(self):
        return self._counter

    def roll_die(self):
       die_value =  self._die.roll_die()
       return die_value

    def increment_counter(self):
        self._counter+=1

    def decrement_counter(self):
        self._counter-=1


class DiceGame:
    def __init__(self, human_player:Player, computer_player:Player):
        self._player = human_player
        self._computer = computer_player

    def start_game(self):
        print('Dice game is starting')
        while self._player.counter > 0 < self._computer.counter:
            self._start_round_()

    def _start_round_(self):
        human_player_die = self._player.roll_die()
        computer_player_die = self._computer.roll_die()

        if human_player_die > computer_player_die:
            print('Player win')
            self._player.decrement_counter()
            self._computer.increment_counter()
        elif computer_player_die > human_player_die:
            print('Computer win')
            self._computer.decrement_counter()
            self._player.increment_counter()


player_die = Die()
computer_die = Die()

player = Player(player_die, is_computer=False)
computer = Player(computer_die, is_computer=True)

game = DiceGame(player, computer)



game.start_game()