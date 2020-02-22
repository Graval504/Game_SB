# Game
# Author : Graval504
# Version : 0.1.0

from random import randint
from enum import Enum
from time import sleep
from sys import exit
from os import system

i = 0
class Player:
    def __init__(self,name):
        self.name = name
        self.HP = 10
        self.CRI = 0
        self.ATK = 0
        self.DEF = 0
    def __str__(self):
        pass

    def attack(self, enemy):

        if self.ATK <= 0:
            print("{}은 아무런 행동도 하지 못한다!".format(self.name))
        else:
            chance = randint(1,10)
            if chance <= self.CRI:
                print("특수공격 발동!")
                self.special_attack(enemy)
            else:
                if self.ATK > 0:
                    print("{}이 {}을 공격!".format(self.name, enemy.name))
                chance2 = randint(1,10)
                if chance2 <= enemy.DEX:
                    print("특수방어 발동!")
                    enemy.special_defense(self)
                else:
                    damage = self.ATK - enemy.DEF
                    if damage < 0:
                        damage = 0
                        print("아무런 피해도 입히지 못했다!")
                    enemy.HP -= damage

    def special_attack(self, enemy):
        pass

    def special_defense(self, enemy):
        pass

    def is_dead(self):
        return self.HP <= 0

class Warrior(Player):
    def __init__(self,name):
        self.name = name
        self.HP = 10
        self.ATK = 4
        self.DEF = 2
        self.DEX = 4
        self.CRI = 3

    def __str__(self):
        return("NAME : {}. JOB: Warrior\nHP : {}"
.format(self.name, self.HP))
    def special_attack(self , enemy):
       enemy.DEF -= 1
       print("""
       {}의 물렁해지기! : {}의 방어력이 1만큼 감소시킨후, 공격합니다.
       {}의 현재 방어력 : {}
       """.format(self.name,enemy.name, enemy.name, enemy.DEF))
       damage = self.ATK - enemy.DEF
       if damage < 0:
             damage = 0
       enemy.HP -= damage
    def special_defense(self, enemy):
        print("""
        {}의 단단해지기! : 공격을 무시하며, {}의 방어력이 1만큼 상승합니다.
        {}의 현재 방어력 :{}
        """.format(self.name,self.name, self.name,self.DEF))

class Thief(Player):
    def __init__(self,name):
        self.name = name
        self.HP = 5
        self.DEX = 8
        self.ATK = 3
        self.DEF = 1
        self.CRI = 3
    
    def __str__(self):
        return("NAME : {}. JOB: Thief\nHP : {}"
.format(self.name, self.HP))
    def special_attack(self, enemy):
        if enemy.ATK > 1:
            try:
                if enemy.FixedATK == 3:
                    if enemy.Ammo == 0:
                        self.HP += 1
                        print("""
                        {}은 포션을 빼앗았다! : {}의 체력이 1만큼 상승합니다.
                        """.format(self.name,self.name))
                    else:
                        enemy.Ammo -= 1
                        self.ATK += 1
                        print("""
                        {}이 총알을 빼앗았다! : {}의 탄약이 1만큼 감소하고, 그만큼 {}의 공격력이 상승합니다.
                        {}의 현재 탄약 : {} , {}의 현재 공격력 : {}
                        """.format(self.name,enemy.name, self.name, enemy.name, enemy.Ammo, self.name, self.ATK))
            except:
                enemy.ATK -= 1
                self.ATK += 1
                print("""
                {}이 무기를 빼앗았다! : {}의 공격력이 1만큼 감소하고, 그만큼 {}의 공격력이 상승합니다.
                {}의 현재 공격력 : {} , {}의 현재 공격력 : {}
                """.format(self.name,enemy.name, self.name, enemy.name, enemy.ATK, self.name, self.ATK))
        else:
            self.HP += 1
            print("""
            {}은 포션을 빼앗았다! : {}의 체력이 1만큼 상승합니다.
            """.format(self.name,self.name))
    
    def special_defense(self, enemy):
        print("""
        {}의 회피! : 공격을 맞지 않습니다.
        """.format(self.name))

class Shieldbearer(Player):
    def __init__(self,name):
        self.name = name
        self.HP = 8
        self.ATK = 3
        self.DEF = 2
        self.CRI = 3
        self.DEX = 7
        self.SAVEATK = 0
        self.SAVEDEF = 0

    def __str__(self):
        return("NAME : {}. JOB: Shieldbearer\nHP : {}"
.format(self.name, self.HP))
    def special_attack(self,enemy):
        if self.ATK != 0:
            print("""
            {}은 평범하게 공격했다!
            """.format(self.name))
            damage = self.ATK - enemy.DEF
            if damage < 0:
                    damage = 0
            enemy.HP -= damage

        else:
            print("""
            {}가 갑자기 방패를 내리며 치명타를 입혔다! : 3배의 공격력인 {}으로 상대를 공격합니다.
            """.format(self.name,3 * self.SAVEATK * 3))
            self.ATK = self.SAVEATK
            self.DEF = self.SAVEDEF
            self.ATK *= 3
            self.attack(enemy)
            self.ATK = self.ATK/3
    def special_defense(self,enemy):
        if self.ATK != 0:
            print("""
            {}는 방패를 들어올렸다! : 무적이 되지만, 동시에 공격을 할 수 없게 됩니다.
            """.format(self.name))
            self.SAVEATK = self.ATK
            self.SAVEDEF = self.DEF
            self.ATK = 0
            self.DEF = 999
        else:
            luckypunch = randint(1,10)
            if luckypunch <= self.CRI:
                self.special_attack(enemy)
            else:
                print("{}은 아무런 행동도 하지 않았다!".format(self.name))

class Fighter(Player):
    def __init__(self,name):
        self.name = name
        self.HP =  15
        self.ATK = 3
        self.DEF = 0
        self.CRI = 3
        self.DEX = 2
    def __str__(self):
        return("NAME : {}. JOB: Fighter\nHP : {}"
.format(self.name, self.HP))
    def special_attack(self,enemy):
        print("""
        연타! : {}가 한번 더 공격할 기회를 가집니다.
        """.format(self.name))
        sleep(2)
        self.attack(enemy)
        sleep(2)
        self.attack(enemy)
        sleep(2)

    def special_defense(self,enemy):
        damage = enemy.ATK - self.DEF
        if damage < 0:
            damage = 0
        self.HP -= damage
        self.ATK += damage
        print("""
        인내! : 공격당한 후, 받은 피해량 만큼 {}의 공격력이 증가합니다.
        """.format(self.name))

class Gunner(Player):
    def __init__(self,name):
        self.name = name
        self.HP =  8
        self.ATK = 4
        self.FixedATK = 4
        self.DEF = 2
        self.CRI = 3
        self.DEX = 2
        self.MAmmo = 3
        self.Ammo = 0
        self.SAVECRI = 0
    def __str__(self):
        return("NAME : {}. JOB: Gunner\nHP : {} Ammo : {}"
.format(self.name, self.HP, self.Ammo))

    def attack(self, enemy):
        if self.Ammo == 0:
            print("""
            총알을 장전합니다
            """)
            self.Ammo = self.MAmmo
        else:
            if self.ATK != self.FixedATK:
                self.ATK = self.FixedATK
            chance = randint(1,10)
            if chance <= self.CRI:
                print("특수공격 발동!")
                self.special_attack(enemy)
            else:
                print("{}이 {}을 공격!".format(self.name, enemy.name))
                chance2 = randint(1,10)
                if chance2 <= enemy.DEX:
                    self.Ammo -= 1
                    print("특수방어 발동!")
                    enemy.special_defense(self)
                else:
                    damage = self.ATK - enemy.DEF
                    if damage != 0:
                        mis = randint(1,10)
                        shot = randint(1,100)
                        if mis == 1:
                            print("""
                            아쉽게도 빗나갔다!
                            """)
                            damage = 0
                        else:
                            if shot >= 1 and shot < 37:
                                enemy.DEX -= 1
                                if enemy.DEX < 0:
                                    enemy.DEX = 0
                                    print("""
                                    다리에 적중하였으나 더 이상 민첩이 감소하지 않습니다.
                                    """)
                                else:
                                    print("""
                                    다리에 적중하였다! : {}의 민첩이 1 감소합니다.
                                    {}의 현재 민첩 : {}
                                    """.format(enemy.name, enemy.name, enemy.DEX))
                            
                            if shot >= 37 and shot < 55:
                                enemy.CRI -= 1
                                if enemy.CRI < 0:
                                    enemy.CRI = 0
                                    print("""
                                    팔에 적중하였으나 더 이상 특수공격 발동률이 줄어들지 않습니다.
                                    """)
                                else:
                                    print("""
                                    팔에 적중하였다! : {}의 특수공격 발동률이 1 감소합니다.
                                    {}의 현재 특수공격 발동률 : {}
                                    """.format(enemy.name,enemy.name,enemy.CRI))
                        
                            if shot >= 55 and shot < 65:
                                print("""
                                머리에 적중하였다! :죽음에 가까운 피해를 입힙니다.
                                """)
                                if enemy.HP > 1:
                                    damage = enemy.HP - 1
                                    if damage < self.ATK - enemy.DEF:
                                        damage = self.ATK - enemy.DEF
                                else:
                                    damage = 1

                            if shot >= 65:
                                print("""
                                몸에 적중하였다! : 일반적인 피해를 입힙니다.
                                """)
                    enemy.HP -= damage
                    self.Ammo -= 1

    def special_attack(self,enemy):
        print("""
        속사! : 남은 총알 {}발을 전부 발사합니다
        """.format(self.Ammo))
        m = self.Ammo
        self.SAVECRI = self.CRI
        self.CRI = 0
        for _i in range(0,m):
            self.attack(enemy)
            sleep(2)
        self.CRI = self.SAVECRI

    def special_defense(self,enemy):
        print("""
        {}은 굴러서 회피후 공격하였다!
        """.format(self.name))
        spmis = randint(1,5)
        if spmis <= 1:
            print("""
            하지만 공격은 빗나갔다!
            """)
            self.Ammo -= 1
        else:
            self.attack(enemy)
def turn(p1,p2):
    print("==================================")
    print("{}의 차례.".format(p1.name))
    sleep(1)
    p1.attack(p2)
    print("현재 상태")
    print()
    print(p1)
    print()
    print(p2)
    print("==================================")
    ###########################################################
    if p2.is_dead():
        print("{}은 사망하셨습니다.".format(p2.name))
        print("{}의 승리!".format(p1.name))
        exit(1)
    ###########################################################
    input()
    system("clear")
    print("==================================")
    print("{}의 차례.".format(p2.name))
    sleep(1)
    p2.attack(p1)
    print("현재 상태")
    print()
    print(p1)
    print()
    print(p2)
    print("==================================")
    ###########################################################
    if p1.is_dead():
        print("{}은 사망하셨습니다.".format(p1.name))
        print("{}의 승리!".format(p2.name))
        exit(1)
    input()
    system("clear")
p1 = Gunner("A")
p2 = Shieldbearer("B")

coin = randint(1,2)
if coin == 1:
    pass
else:
    (p1,p2) = (p2,p1)

print("게임을 시작합니다.")
n = True
while n:
    turn(p1,p2)
    if p1.is_dead() or p2.is_dead == True:
        n = False