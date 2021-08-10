import pygame
import os
import random
# screen size
WIN_WIDTH = 1024
WIN_HEIGHT = 600
# frame rate
FPS = 60
# color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (147, 0, 147)
# enemy path


PATH1=[(12, 386), (239, 341), (424, 238), (567, 296), (834, 288)]
PATH2 = [(15, 65), (62, 55), (120, 58), (276, 106), (383, 191), (518, 279), (670, 317), (833, 289)]
PATH3 = [(298, 591), (286, 556), (279, 507), (265, 458), (261, 436), (252, 409), (245, 386), (226, 360), (232, 344), (259, 337), (298, 316), (324, 302), (359, 293), (395, 264), (423, 238), (438, 220), (458, 252), (494, 270), (525, 282), (560, 299), (592, 303), (627, 309), (650, 311), (683, 313), (728, 317), (770, 311), (804, 297), (833, 290)]
#PATHALL = [PATH1,PATH2,PATH3]
#PATH = random.choice(PATHALL)

# base
BASE = pygame.Rect(827,244,90,100)
   # (430, 90, 195, 130)
#[(827, 244), (839, 322), (924, 221), (949, 308)]
# image
BACKGROUND_IMAGE = pygame.image.load(os.path.join("images", "Map.png"))
HP_GRAY_IMAGE = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (40, 23))
HP_IMAGE = pygame.transform.scale(pygame.image.load("images/hp.png"), (40, 23))

WAVE = ['E','E','E','v','v','v','a','a']
random.shuffle(WAVE)#'E','E','v','v',