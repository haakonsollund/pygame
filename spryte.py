import pygame as pg
from random import randint

player_img = pg.image.load("samurai.png")
player_img2 = pg.image.load("wizard_idle.png")
heroRun_img = pg.image.load("run.png")

herorunleft_img = pg.transform.flip(heroRun_img, True, False)
attack_img = pg.image.load("Attack1.png")
vec = pg.math.Vector2
player_img2 = pg.transform.scale(player_img2, (100,130))
attack_img = pg.transform.scale(attack_img, (100,130))
small_bullet_img = pg.image.load("bullet.png")
big_bullet_img = pg.image.load("bigbullet.png")
laser_beam_img = pg.image.load("langbeam.png")




class player(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = player_img
        self.pos = vec(50,50)
        self.rect = self.image.get_rect() # 
        self.rect.center = self.pos
        self.speed = 5
        self.projectile_speed = 5
        self.attack_direction_x, self.attack_direction_y = 0, 0

        self.life = 3

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

    def attack(self):
        Ranged_attack(self.game, self.pos.x, self.pos.y, self.attack_direction_x, self.attack_direction_y)



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


class laserbeam(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = laser_beam_img
        self.pos = vec (900,300)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.speed = 8

    def update(self):
        self.rect.center = self.pos

        self.pos.x -= self.speed




class Ranged_attack(pg.sprite.Sprite):
    def __init__(self, game, x ,y, direction_x, direction_y):
        self.groups = game.all_sprites, game.projectiles_grp # legger til i sprite gruppe
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface([50,50])
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) # start posisjon
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.rect.center = self.pos
 
    def update(self):
        self.rect.center = self.pos
        self.pos.x += self.direction_x
        self.pos.y += self.direction_y


        











