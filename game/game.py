import pygame
from game.controller import GameControl
from game.model import GameModel
from game.view import GameView
from settings import FPS
from game.gameover import GameOver   #8/9
from game.gameend import GameEnd
from menu.menus import music_button_image,muse_button_image

class Game:
    def run(self):
        
        pygame.init()
        game_model = GameModel()
        game_view = GameView()  
        game_control = GameControl(game_model, game_view)  
        win_game = False
        quit_game = False
        while not quit_game:
            pygame.time.Clock().tick(FPS)  
            game_control.receive_user_input()  
            game_control.update_model()  
            game_control.update_view()  
            pygame.display.update()
            win_game = game_model.win()   #8/10
            quit_game = game_control.quit_game
            
            if win_game:   #8/10
                game_end = GameEnd()
                quit_game = game_end.run(quit_game)
                pygame.init()
                game_model = GameModel()
                game_view = GameView()
                game_control = GameControl(game_model, game_view)
                win_game = False
                pygame.mixer.music.load("./sound/menu.wav")
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play()
                
            
            if game_model.gameover():  # 8/9
                gameover = GameOver()
                quit_game = gameover.run(quit_game)
                pygame.init()
                game_model = GameModel()
                game_view = GameView()
                game_control = GameControl(game_model, game_view)
                win_game = False
                
                
                
                
                
                
                
                
                
                
                
                