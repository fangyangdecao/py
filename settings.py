class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        # 设置背景颜色
        self.bg_color = (192, 192, 192)

        # 飞船的设置
        # self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        # self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # 外星人
        # self.alien_speed_factor = 10
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 外星人点数提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """随着游戏的进行"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_point = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.score_scale)
