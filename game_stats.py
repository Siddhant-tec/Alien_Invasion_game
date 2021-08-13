class GameStats():
    def __init__(self, set):
        self.set = set
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.set.ship_limit

