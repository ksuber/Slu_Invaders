


class GameStats():
    """Tracks all the stats"""
    def __init__(self, si_settings):
        self.si_settings = si_settings
        self.reset_stats()
        #Starts game in inactive state
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """ stats that can change during the game"""
        self.ships_left = self.si_settings.ship_limit
        self.score = 0
        self.level = 1
