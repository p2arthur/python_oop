class Player:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def move_up(self, change=5):
        self._y += change

    def move_down(self, change=5):
        self._y -= change

    def move_left(self, change=5):
        self._x -= change

    def move_right(self, change=5):
        self._x += change

    @property
    def position(self):
        print(f"x:{self._x}, y:{self._y}")
        return {self._x, self._y}

my_player = Player(0,0)


my_player.move_up()

my_player.move_right()
my_player.move_right()
my_player.move_right()

my_player.get_player_position()

