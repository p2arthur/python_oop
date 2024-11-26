import random


class Die:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll_die(self):
        print('Rolling die...')
        random_value = random.randint(1,6)
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

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

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
        print('=====================================')
        print('Welcome to Roll the Dice game!')
        print('=====================================')
        while self._player.counter > 0 < self._computer.counter:
            self._start_round_()
            game_over = self.check_game_over()
            if game_over:
                break

    def _start_round_(self):
        self.print_round_welcome()
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()
        self.print_dice()
        self.check_winner(player_value, computer_value)
        self.print_game_score()

    @staticmethod
    def print_round_welcome():
        print('--------- NEW ROUND ----------')
        input('Press any key to roll the dice')

    def print_game_score(self):
        print(f'Player counter:{self._player.counter} | Computer counter: {self._computer.counter}')

    def print_dice(self):
        print(f'Player die:{self._player.die.value} | Computer die: {self._computer.die.value}')

    def check_winner(self, player_value, computer_value):
        if player_value > computer_value:
            self.update_counter(self._player, self._computer)
        elif computer_value > player_value:
            self.update_counter(self._computer, self._player)
        else:
            print('Its a tie')

    @staticmethod
    def update_counter( winner:Player, loser:Player):
        winner.decrement_counter()
        loser.increment_counter()

    def check_game_over(self)->bool:

        if self._computer.counter == 0:
            print('---------------------Computer wins-------------------')
            self.show_game_over(self._computer)
            return True
        if self._player.counter == 0:
            self.show_game_over(self._player)
            print('---------------------Player wins---------------------')
            return True
        else:
            return False

    @staticmethod
    def show_game_over(winner:Player):
        if winner.is_computer:
            print('-----------------------------------------------')
            print('Computer wins')
            print('-----------------------------------------------')
        else:
            print('-----------------------------------------------')
            print('Player wins')
            print('-----------------------------------------------')



player_die = Die()
computer_die = Die()

player = Player(player_die, is_computer=False)
computer = Player(computer_die, is_computer=True)

game = DiceGame(player, computer)



game.start_game()