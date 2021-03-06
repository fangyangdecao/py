import sys
import pygame
from pygame.sprite import Group

from war.settings import Settings
from war.ship import Ship
from war.button import Button
from war.game_stats import GameStats
from war.scoreboard import Scoreboard
from war.alien import Alien
import war.game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("alien invasion".title())

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # alien = Alien(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏循环
    while True:
        # 监听键盘鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, bullets, aliens)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
