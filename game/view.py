import pygame
from settings import WIN_WIDTH, WIN_HEIGHT, HP_IMAGE, HP_GRAY_IMAGE, BACKGROUND_IMAGE
from color_settings import *
from menu.menus import music_button_image, muse_button_image

#love
LOVE_GRAY_IMAGE = pygame.transform.scale(pygame.image.load("images/love_gray.png"), (28, 26))
LOVE_IMAGE = pygame.transform.scale(pygame.image.load("images/love.png"), (28, 26))

class GameView:
    def __init__(self):
        self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.font = pygame.font.SysFont("arial",24)

    def draw_bg(self):
        self.win.blit(BACKGROUND_IMAGE, (0, 0))

    def draw_sound(self):
        self.win.blit(music_button_image, (725, 525))
        self.win.blit(muse_button_image, (825, 525))


    def draw_towers(self, towers):
        # draw tower
        for tw in towers:
            self.win.blit(tw.image, tw.rect)

    def draw_enemies(self, enemies):
        for en in enemies.get():
            self.win.blit(en.image, en.rect)
            # draw health bar
            bar_width = en.rect.w * (en.health / en.max_health) *0.77
            max_bar_width = en.rect.w *0.77
            bar_height = 5
            pygame.draw.rect(self.win, RED, [en.rect.x+3, en.rect.y - 10, max_bar_width, bar_height])
            pygame.draw.rect(self.win, GREEN, [en.rect.x+3, en.rect.y - 10, bar_width, bar_height])

    def draw_range(self, selected_tower):
        # draw tower range
        if selected_tower is not None:
            tw = selected_tower
            # create a special surface that is able to render semi-transparent image
            surface = pygame.Surface((WIN_WIDTH, WIN_HEIGHT), pygame.SRCALPHA)
            transparency = 120
            pygame.draw.circle(surface, (128, 128, 128, transparency), tw.rect.center, tw.range)
            self.win.blit(surface, (0, 0))

    def draw_menu(self, menu):
        self.win.blit(menu.image, menu.rect)
        for btn in menu.buttons:
            self.win.blit(btn.image, btn.rect)

    def draw_lovemenu(self, lovemenu): #love
        for btn in lovemenu.buttons:
            self.win.blit(btn.image, btn.rect)

    def draw_plots(self, plots):
        for pt in plots:
            self.win.blit(pt.image, pt.rect)

    def draw_money(self, money: int):
        """ (Q2.1)render the money"""
        pygame.draw.rect(self.win, (205,175 ,149), [1024-300, 520, 300,80])
        text = self.font.render(f"Money: {money}", True, (139,69 ,19))
        self.win.blit(text, (1024-115, 565))

    def draw_wave(self, wave: int):
        """(Q2.2)render the wave"""
        text = self.font.render(f"Wave: {wave}/5", True, (139,69 ,19))
        self.win.blit(text, (1024-115, 535))


    def draw_hp(self, lives):
        # draw_lives
        hp_rect = HP_IMAGE.get_rect()
        for i in range(9):
            self.win.blit(HP_GRAY_IMAGE, (619+39 * ( i % 9 ),45))

        for i in range(lives):
            self.win.blit(HP_IMAGE,(619+39 * ( i % 9 ),45))



    def draw_love_grade(self, love_grade): #love
        love_rect = LOVE_IMAGE.get_rect()
        for i in range(7):
            self.win.blit(LOVE_GRAY_IMAGE, (632.5+ 50.7* ( i % 7), 90))
        for i in range(love_grade):
            self.win.blit(LOVE_IMAGE, (632.5+ 50.7* ( i % 7), 90))

