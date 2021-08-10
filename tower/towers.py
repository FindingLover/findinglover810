from tower.attack_strategy import AOE, SingleAttack, Snipe, Slow, Stop    # 加上Stop8/8
import os
import pygame


PLOT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "vacant_lot.png")), (20, 20))
ALCOHOL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "alcohol.png")), (81, 80))
VACCINE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "vaccine.png")),  (81, 80))
ISOLATE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "isolate.png")),  (54, 50))
HEALTHCARE_IMAGE= pygame.transform.scale(pygame.image.load(os.path.join("images", "healthcare.png")),  (81, 80))
MASK_IMAGE= pygame.transform.scale(pygame.image.load(os.path.join("images", "mask.png")),  (54, 50))
class Vacancy:
    def __init__(self, x, y):
        self.image = PLOT_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.identify=1

    def clicked(self, x: int, y: int) -> bool:

        return True if self.rect.collidepoint(x, y) else False

class BlockVacancy:         #新增
    def __init__(self, x, y):
        self.image = PLOT_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.identify=0

    def clicked(self, x: int, y: int) -> bool:
        
        return True if self.rect.collidepoint(x, y) else False

    
class Tower:
    """ super class of towers """
    def __init__(self, x: int, y: int, attack_strategy, image):
        self.image = image  
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  
        self.level = 0  
        self._range = [100, 110, 120, 130, 140, 150] 
        self._damage = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5]   
        self.cd_count = 0  
        self.cd_max_count = 60  
        self.attack_strategy = attack_strategy  
        self.value = [100, 140, 200, 300, 380, 460]
        self.hp = 300  #塔的血量 (用來破壞塔) 新增
        self.identify = 1  # 用來辨識地面和高台塔的 8/8

    @classmethod
    def HealthFood(cls, x, y):  #範圍傷害
        healthfood = cls(x, y, AOE(), HEALTHCARE_IMAGE)
        healthfood._range = [130, 140, 150, 160, 170, 180]
        healthfood._damage = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5]
        healthfood.value = [100, 140, 200, 280, 360, 450]
        return healthfood

    @classmethod
    def Alcohol(cls, x, y):     #單體攻擊
        alcohol = cls(x, y, SingleAttack(), ALCOHOL_IMAGE)
        alcohol._range = [120, 125, 130, 135, 140, 145]
        alcohol._damage = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
        alcohol.value = [120, 160, 220, 320, 400, 500]
        return alcohol

    @classmethod
    def Vaccine(cls, x, y):   #狙擊
        vaccine = cls(x, y, Snipe(), VACCINE_IMAGE)
        vaccine._range = [100, 105, 110, 115, 120, 125]  
        vaccine.cd_max_count = 120  
        vaccine.value = [120, 140, 200, 280, 360, 400]
        return vaccine

    @classmethod
    def Isolate(cls, x, y):  # 全部緩速
        isolate = cls(x, y, Slow(), ISOLATE_IMAGE)
        isolate._range = [0]  # 8/8
        isolate.cd_max_count = 1
        isolate.identify = 0  # 8/8
        return isolate

    @classmethod
    def Mask(cls, x, y):    #8/8 加上新塔(Block)，擋人+傷害
        mask = cls(x, y, Stop(), MASK_IMAGE)
        mask._range = [5]
        mask.cd_max_count = 1
        mask.identify=0
        return mask

    def attack(self, enemy_group: list):
        
        if self.cd_count < self.cd_max_count:
            self.cd_count += 1
            return
        
        self.cd_count = self.attack_strategy.attack(enemy_group, self, self.cd_count)

    def get_upgrade_cost(self):
        return self.value[self.level+1] - self.value[self.level]

    def get_cost(self):
        return self.value[self.level]

    @property
    def range(self):
        return self._range[self.level]

    @property
    def damage(self):
        return self._damage[self.level]

    def clicked(self, x: int, y: int) -> bool:
        
        return True if self.rect.collidepoint(x, y) else False





