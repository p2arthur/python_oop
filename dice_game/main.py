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
        while True:
            self._start_round_()
            game_over = self._check_game_over()
            if game_over:
                break

    def _start_round_(self):
        self._print_round_welcome()
        self._roll_dice()
        self._print_dice()
        self._check_winner()
        self._print_game_score()

    @staticmethod
    def _print_round_welcome():
        print('\n--------- NEW ROUND ----------')
        input('Press any key to roll the dice')

    def _roll_dice(self):
        self._player.roll_die()
        self._computer.roll_die()

    def _print_game_score(self):
        print(f'\nPlayer counter:{self._player.counter} | Computer counter: {self._computer.counter}')

    def _print_dice(self):
        print(f'Player die:{self._player.die.value} | Computer die: {self._computer.die.value}')

    def _check_winner(self):
        if self._player.die.value > self._computer.die.value:
            self._update_players_counter(self._player, self._computer)
        elif self._computer.die.value > self._player.die.value:
            self._update_players_counter(self._computer, self._player)
        else:
            print('Its a tie')

    @staticmethod
    def _update_players_counter(winner:Player, loser:Player):
        winner.decrement_counter()
        loser.increment_counter()

    def _check_game_over(self)->bool:

        if self._computer.counter == 0:
            print('---------------------Computer wins-------------------')
            self._show_game_over(self._computer)
            return True
        if self._player.counter == 0:
            self._show_game_over(self._player)
            print('---------------------Player wins---------------------')
            return True
        else:
            return False

    @staticmethod
    def _show_game_over(winner:Player):
       print(f'{"Computer" if winner.is_computer else "Player"}')




player_die = Die()
computer_die = Die()

player = Player(player_die, is_computer=False)
computer = Player(computer_die, is_computer=True)

game = DiceGame(player, computer)



game.start_game()