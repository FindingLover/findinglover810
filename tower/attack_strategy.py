import math
from abc import ABC, abstractmethod


def in_range(enemy, tower):
    x1, y1 = enemy.rect.center
    x2, y2 = tower.rect.center
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance <= tower.range:
        return True
    return False


"""
syntax: attack_strategy().attack(tower, enemy_group, cd_count)
It's something like you hire a "Strategist" to decide how to attack the enemy
You can add other ways of attack just by expand this module
"""


class AttackStrategy(ABC):
    """Abstract class of attack method"""
    @ abstractmethod
    def attack(self, enemies, tower, cd_count):
        return "Please implement this method"


class SingleAttack(AttackStrategy):
    """attack an enemy once a time"""
    def attack(self, enemies: list, tower, cd_count):
        for en in enemies:
            if in_range(en, tower):
                en.health -= tower.damage
                cd_count = 0
                return cd_count
        return cd_count


class AOE(AttackStrategy):
    """attack all the enemy in range once a time"""
    def attack(self, enemies: list, tower, cd_count):
        for en in enemies:
            if in_range(en, tower):
                en.health -= tower.damage
                cd_count = 0
        return cd_count


class Snipe(AttackStrategy):
    """eliminate an enemy all in once"""
    def attack(self, enemies: list, tower, cd_count):
        for en in enemies:
            if in_range(en, tower):
                en.health = 0
                cd_count = 0
                return cd_count
        return cd_count

#class Slow(AttackStrategy):                      #範圍內緩
    #def attack(self, enemies, tower, cd_count):
        #for en in enemies:
            #if in_range(en, tower):
                #en.stride=0.5
                #cd_count = 0
            #else:
                #en.stride=1
        #return cd_count

class Slow(AttackStrategy):                      #全緩 N秒 (新增)
    def attack(self, enemies, tower, cd_count):
        if tower.hp>1:
            for en in enemies:
                en.move_count -= 0.5  # 更改緩速機制 8/8
            tower.hp-=1
            return cd_count  
            
        else:
            for en in enemies:
                en.stride=1
            tower.hp=0
            return cd_count


class Stop(AttackStrategy):  # 擋人+傷害 8/8
    def attack(self, enemies, tower, cd_count):
        if tower.hp > 1:
            for en in enemies:
                if in_range(en, tower):
                    en.health -= 0.03
                    en.move_count -= 1
                    tower.hp -= 1
                    return cd_count
            tower.hp -= 1
            return cd_count

        else:
            tower.hp = 0
            return cd_count
