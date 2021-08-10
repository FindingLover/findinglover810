import pygame  # 8/10
from settings import WIN_WIDTH, WIN_HEIGHT
GAMEOVER_IMAGE = pygame.transform.scale(pygame.image.load("images/gameover.png"), (WIN_WIDTH, WIN_HEIGHT))

class GameEnd:
    def run(self, quit):
        stop = False
        while not stop:
            self.win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
            self.win.blit(GAMEOVER_IMAGE, (0, 0))
            for event in pygame.event.get():
                pygame.display.update()
                if event.type == pygame.QUIT:
                    quit = True
                    return quit
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    stop = True