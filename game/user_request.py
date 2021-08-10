import pygame
from tower.towers import Tower, Vacancy


"""This module is import in model.py"""

"""
Here we demonstrate how does the Observer Pattern work
Once the subject updates, it will notify all the observer who has register the subject
"""


class RequestSubject:
    def __init__(self, model):
        self.__observers = []
        self.model = model

    def register(self, observer):
        self.__observers.append(observer)

    def notify(self, user_request):
        for o in self.__observers:
            o.update(user_request, self.model)


class EnemyGenerator:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """add new enemy"""
        if user_request == "start wave":
            model.enemies.add(8)
            model.wave += 1



class TowerSeller:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """sell tower"""
        if user_request == "sell":
            x, y = model.selected_tower.rect.center
            model.money += model.selected_tower.get_cost()
            model.plots.append(Vacancy(x, y))
            model.towers.remove(model.selected_tower)
            model.selected_tower = None


class TowerDeveloper:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """ upgrade tower"""
        if user_request == "upgrade" and model.selected_tower.level < 5:
            if model.money > model.selected_tower.get_upgrade_cost():     
                model.money -= model.selected_tower.get_upgrade_cost()    
                model.selected_tower.level += 1                           

class HeartDeveloper:
    def __init__(self, subject):
        subject.register(self)
    def update(self, user_request: str, model):
        if model._love_menu.heart_cool_down():
            if user_request == "heart":
                if model.love_grade < 10:
                    model.love_grade += 1
                    model._love_menu.heart_count = 0

class LoveletterDeveloper:
    def __init__(self, subject):
        subject.register(self)
    def update(self, user_request: str, model):
        if model._love_menu.loveletter_cool_down():
            if user_request == "loveletter":
                if model.money > 149 and model.love_grade < 10:
                    model.money -= 150
                    model._love_menu.loveletter_count = 0
                    for count in range (0, 3):
                        if model.love_grade < 10:
                            model.love_grade += 1   

class TowerFactory:
    def __init__(self, subject):
        subject.register(self)
        self.tower_name = ["vaccine", "health food", "alcohol","isolate","mask"]     #加上其他塔

    def update(self, user_request: str, model):
        """add new tower"""
        for name in self.tower_name:
            if user_request == name:
                x, y = model.selected_plot.rect.center
                tower_dict = {"vaccine": Tower.Vaccine(x, y), "health food": Tower.HealthFood(x, y),
                              "alcohol": Tower.Alcohol(x, y), "isolate": Tower.Isolate(x, y),
                              "mask": Tower.Mask(x, y)}  #加上新塔 8/8
                new_tower = tower_dict[user_request]
                if model.money > new_tower.get_cost():
                    model.money -= new_tower.get_cost()
                    model.towers.append(new_tower)
                    model.plots.remove(model.selected_plot)
                    model.selected_plot = None


class Music:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music on"""
        if user_request == "music":
            pygame.mixer.music.unpause()
            #model.sound.play()


class Muse:
    def __init__(self, subject):
        subject.register(self)

    def update(self, user_request: str, model):
        """music off"""
        if user_request == "mute":
            pygame.mixer.music.pause()
            #model.sound.play()

