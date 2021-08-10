import pygame
import os
from tower.towers import Tower, Vacancy, BlockVacancy
from enemy.enemies import EnemyGroup,Enemy
from menu.menus import UpgradeMenu, BuildMenu, MainMenu, BlockMenu, LoveMenu
from game.user_request import RequestSubject, TowerFactory, TowerSeller, TowerDeveloper, EnemyGenerator, Muse, Music, HeartDeveloper, LoveletterDeveloper
from settings import WIN_WIDTH, WIN_HEIGHT, BACKGROUND_IMAGE
from menu.menus import UpgradeMenu, BuildMenu, MainMenu, LoveMenu

class GameModel:
    def __init__(self):
        
        self.bg_image = pygame.transform.scale(BACKGROUND_IMAGE, (WIN_WIDTH, WIN_HEIGHT))
        self.__towers = [Tower.Alcohol(250, 380), Tower.HealthFood(180, 300)]   #改名字
        self.__enemies = EnemyGroup()
        self.__menu = None
        self.__main_menu = MainMenu()
        self._love_menu = LoveMenu()  # love
        self.__plots = [Vacancy(50, 350), Vacancy(350, 280), BlockVacancy(504, 275)]  # 改Block的位置 8/8

        self.selected_plot = None
        self.selected_tower = None
        self.selected_button = None
        
        self.subject = RequestSubject(self)
        self.seller = TowerSeller(self.subject)
        self.developer = TowerDeveloper(self.subject)

        self.loveletter_developer = LoveletterDeveloper(self.subject) #love
        self.heartdeveloper = HeartDeveloper(self.subject) #love

        self.factory = TowerFactory(self.subject)
        self.generator = EnemyGenerator(self.subject)
        self.muse = Muse(self.subject)
        self.music = Music(self.subject)


        self.wave = 0
        self.money = 500
        self.money = 500
        self.max_hp = 9
        self.hp = self.max_hp
        self.max_love_grade = 7  #戀愛指數滿分10 #更改
        self.love_grade = self.max_love_grade  #戀愛指數初始10
        self.loss_love_count = 0
        self.loss_max_count = 300
        self.sound = pygame.mixer.Sound(os.path.join("sound", "sound.flac"))
        self.sound.set_volume(0.2)  #音量調小

    def user_request(self, user_request: str):
        """ add tower, sell tower, upgrade tower"""
        self.subject.notify(user_request)



    def get_request(self, events: dict) -> str:
        self.selected_button = None
       
        if events["keyboard key"] is not None:
            return "start wave"
        
        if events["mouse position"] is not None:
            x, y = events["mouse position"]
            self.select(x, y)
            if self.selected_button is not None:
                return self.selected_button.response    #回傳名字
            return "nothing"
        return "nothing"

    def select(self, mouse_x: int, mouse_y: int) -> None:
        
        
        for tw in self.__towers:
            if tw.clicked(mouse_x, mouse_y):
                self.selected_tower = tw
                self.selected_plot = None
                return

        for pt in self.__plots:
            if pt.clicked(mouse_x, mouse_y):
                self.selected_tower = None
                self.selected_plot = pt
                return

        
        if self.__menu is not None:
            for btn in self.__menu.buttons:
                if btn.clicked(mouse_x, mouse_y):
                    self.selected_button = btn
            if self.selected_button is None:
                self.selected_tower = None
                self.selected_plot = None
        
        for btn in self.__main_menu.buttons:
            if btn.clicked(mouse_x, mouse_y):
                self.selected_button = btn

        # lovemenu btn
        for btn in self._love_menu.buttons:
            if btn.clicked(mouse_x, mouse_y):
                self.selected_button = btn

    def call_menu(self):
        if self.selected_tower is not None:          #選擇秀出哪種menu
            x, y = self.selected_tower.rect.center
            if self.selected_tower.identify == 1:#8/8
                self.__menu = UpgradeMenu(x, y)
        elif self.selected_plot is not None:
            if self.selected_plot.identify==1:      #新增
                x, y = self.selected_plot.rect.center
                self.__menu = BuildMenu(x, y)
            elif self.selected_plot.identify==0:
                x, y = self.selected_plot.rect.center
                self.__menu = BlockMenu(x, y)
        else:
            self.__menu = None
    
    def loss_love(self):
        if self.loss_love_count < self.loss_max_count:
            self.loss_love_count += 1
        else:
            self.love_grade -= 1
            self.loss_love_count = 0
    
    def towers_attack(self):
        for tw in self.__towers:
            tw.attack(self.__enemies.get())
            
    def towers_collapse(self):                  #讓block種類的塔過n秒後自動倒塌
        for tw in self.__towers:
            if tw.hp==0:
                x, y = tw.rect.center
                self.__plots.append(BlockVacancy(x, y))
                self.__towers.remove(tw)
    
    def enemies_advance(self):
        self.__enemies.advance(self)

    def gameover(self):                #8/9
        if self.love_grade==0 or self.hp==0:
            return True
        else:
            return False
    
    def win(self):                     #8/10
        if self.wave > 2 and self.__enemies.is_empty2():
            if self.love_grade > 0 and self.hp > 0:
                return True
    
    @property
    def enemies(self):
        return self.__enemies

    @property
    def towers(self):
        return self.__towers

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, new_menu):
        self.__menu = new_menu

    @property
    def plots(self):
        return self.__plots











