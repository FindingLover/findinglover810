import pygame
import os

pygame.init()
MENU_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "upgrade_menu.png")), (200, 200))
UPGRADE_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "upgrade.png")), (60, 35))
SELL_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "sell.png")), (40, 40))

HEALTHCARE_IMAGE= pygame.transform.scale(pygame.image.load(os.path.join("images", "healthcare.png")),  (41, 40))
ALCOHOL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "alcohol.png")), (41, 40))
VACCINE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "vaccine.png")),  (41, 40))
ISOLATE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "isolate.png")),  (41, 40))
MASK_IMAGE= pygame.transform.scale(pygame.image.load(os.path.join("images", "mask.png")),  (41, 40))

muse_button_image = pygame.transform.scale(pygame.image.load("images/muse.png"), (80, 80))
music_button_image = pygame.transform.scale(pygame.image.load("images/sound.png"), (80, 80))
continue_button_image = pygame.transform.scale(pygame.image.load("images/continue.png"), (80, 80))
pause_button_image = pygame.transform.scale(pygame.image.load("images/pause.png"), (80, 80))

heart_button_image = pygame.transform.scale(pygame.image.load("images/givelove.png"), (65, 65)) #love
loveletter_button_image = pygame.transform.scale(pygame.image.load("images/loveletter.png"), (74, 67))





class Button:
    def __init__(self, image, name: str, x: int, y: int):
        self.image = image
        self.name = name
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x, y):
        return True if self.rect.collidepoint(x, y) else False

    @property
    def response(self):
        return self.name


class Menu:
    def __init__(self, x: int, y: int):
        self.image = MENU_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self._buttons = []

    @property
    def buttons(self):
        return self._buttons


class UpgradeMenu(Menu):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._buttons = [Button(UPGRADE_BTN_IMAGE, "upgrade", self.rect.centerx, self.rect.centery - 70),
                         Button(SELL_BTN_IMAGE, "sell", self.rect.centerx, self.rect.centery + 75),
                         ]


class BuildMenu(Menu):
    def __init__(self, x, y):     #加上按鈕
        super().__init__(x, y)
        self._buttons = [Button(ALCOHOL_IMAGE, "alcohol", self.rect.centerx -2, self.rect.centery - 70),
                         Button(HEALTHCARE_IMAGE, "health food", self.rect.centerx, self.rect.centery + 75),
                         Button(VACCINE_IMAGE, "vaccine", self.rect.centerx - 70, self.rect.centery + 8),
                         
                         ]

class BlockMenu(Menu):        #加上新menu
    def __init__(self, x, y):     
        super().__init__(x, y)
        self._buttons = [
                         Button(MASK_IMAGE, "mask", self.rect.centerx + 70, self.rect.centery + 7),
                         Button(ISOLATE_IMAGE, "isolate", self.rect.centerx -2, self.rect.centery -70),
                         ]

class MainMenu:
    def __init__(self):
        self._buttons = [Button(music_button_image, "music", 765, 565),
                         Button(muse_button_image, "mute", 865, 565),]
                         #Button(continue_button_image, "continue", 905, 40),
                         #Button(pause_button_image, "pause", 990, 40)]

    @property
    def buttons(self):
        return self._buttons

class LoveMenu:
    def __init__(self):
        self._buttons = [Button(heart_button_image, "heart", 956, 380),
                        Button(loveletter_button_image, "loveletter", 880, 377),
                        ]
        ###[(881, 375), (960, 380)]
        self.heart_count = 0
        self.heart_max_count = 120  #4 sec
        self.loveletter_count = 0
        self.loveletter_max_count = 300 #10 sec
        ###
        
    @property
    def buttons(self):
        return self._buttons

    def heart_cool_down(self):
        if self.heart_count < self.heart_max_count:
            self.heart_count += 1
            return False
        else:
            return True
    
    def loveletter_cool_down(self):
        if self.loveletter_count < self.loveletter_max_count:
            self.loveletter_count += 1
            return False
        else:
            return True






