import pygame as pg
from random import randint

player_img = pg.image.load("samurai.png")
player_img2 = pg.image.load("wizard_idle.png")
heroRun_img = pg.image.load("run.png")

herorunleft_img = pg.transform.flip(heroRun_img, True, False)
attack_img = pg.image.load("Attack1.png")
vec = pg.math.Vector2
player_img2 = pg.transform.scale(player_img2, (100,130))
attack_img = pg.transform.scale(attack_img, (90,120))


class player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = player_img
        self.pos = vec(50,50)
        self.rect = self.image.get_rect() # 
        self.rect.center = self.pos
        self.speed = 5

        self.life = 100

    def update(self):
        self.rect.center = self.pos
  
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos.y -= self.speed
        
        if keys[pg.K_s]:
            self.pos.y += self.speed

        if keys[pg.K_d]:
            self.pos.x += self.speed
            self.image = heroRun_img
        if keys[pg.K_a]:
            self.pos.x -= self.speed
            self.image = herorunleft_img



class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = player_img2
        self.image = pg.transform.flip(self.image,True, False)
        self.pos = vec(750,300)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.speed = 5


    def update(self):
        self.rect.center = self.pos
    





class EnemyAttack(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = attack_img
        self.image = pg.transform.flip(self.image,True, False)
        self.pos = vec(randint(900,1200),randint(0,600))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.speed = 6


    def update(self):
        self.rect.center = self.pos

        self.pos.x -= self.speed

        if self.pos.x < -100:
            self.pos.x = 900
            self.pos.y = randint(0,550)











