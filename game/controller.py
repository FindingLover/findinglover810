import pygame


# controller
class GameControl:
    def __init__(self, game_model, game_view):
        self.model = game_model
        self.view = game_view
        self.events = {"game quit": False,
                       "mouse position": [0, 0],
                       "keyboard key": 0
                       }
        self.request = None
        #self.__enemies = EnemyGroup()

    def update_model(self):
        """update the model and the view here"""
        self.request = self.model.get_request(self.events)
        self.model.user_request(self.request)
        self.model.call_menu()
        self.model.towers_attack()
        self.model.towers_collapse()   #新增
        self.model.enemies_advance()
        self.model.loss_love()   #love

    def receive_user_input(self):
        self.events = {"game quit": False,
                       "mouse position": None,
                       "keyboard key": None
                       }
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.events["game quit"] = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n :
                    self.events["keyboard key"] = pygame.K_n
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.events["mouse position"] = [x, y]

    def update_view(self):
        self.view.draw_bg()
        
        self.view.draw_hp(self.model.hp)
        self.view.draw_love_grade(self.model.love_grade)
        self.view.draw_towers(self.model.towers)
        self.view.draw_enemies(self.model.enemies)

        self.view.draw_range(self.model.selected_tower)
        self.view.draw_plots(self.model.plots)
        self.view.draw_money(self.model.money)  #畫出money
        self.view.draw_wave(self.model.wave)    #畫出wave
        self.view.draw_sound()
        self.view.draw_lovemenu(self.model._love_menu) #love

        if self.model.menu is not None:
            self.view.draw_menu(self.model.menu)

    @property
    def quit_game(self):
        return self.events["game quit"]


