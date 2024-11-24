class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y


player1 = Player(1, 2)
player2 = Player(36, 89)
player3 = Player(62, 60)

players = [player1, player2, player3]

for player in players:
    print(player.x, player.y)
