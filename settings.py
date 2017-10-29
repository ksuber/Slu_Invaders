class Settings():
    """All the settings for the game are stored here ."""
    def __init__(self):
        """Initializes the static settings"""
        # Screen settings
        self.screen_width = 1300
        self.screen_height = 700
        self.bg_color = (230,230,230)
        #Ship settings
        self.ship_limit = 3
        #Bullet settings

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 5
        #Alien settings

        self.fleet_drop_speed = 10


        #increases game speed
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initalize_dynamic_settings()

    def initalize_dynamic_settings(self):
        """Starts dynamic settings that change"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_points = 50
        # fleet direction 1 means right -1 means left
        self.fleet_direction = 1

    def increase_speed(self):
        """increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
