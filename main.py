import pygame as pg
from random import randint
from spryte import*


pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RANDOM = (120,54,189)
GREY = (64,64,64)
FPS = 120
WIDTH = 800
HEIGHT = 600

clock = pg.time.Clock()

score = 0
comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)

speed = 5
life = 100

bg_img = pg.image.load("bakrund.png")
bg_img = pg.transform.scale(bg_img, (800,600))

screen = pg.display.set_mode((WIDTH,HEIGHT))
samurai_img = pg.image.load("samurai.png")
samurai_img = pg.transform.scale(samurai_img, (100,130)) # endre størelse på karakter

all_spryte = pg.sprite.Group()
enemy_group = pg.sprite.Group()
Enemyattack_group = pg.sprite.Group()

samurai = player()
all_spryte.add(samurai)

text_hp = comic_sans30.render("SCORE: " + str(score), True, WHITE)

playing = True
while playing: # game loop
   
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing= False 
    
    screen.blit(bg_img,(0,0))
    
    score += 1
    text_hp = comic_sans30.render("SCORE: " + str(score), True, WHITE)
    
    all_spryte.update()

    hits = pg.sprite.spritecollide(samurai, Enemyattack_group,True)
    if hits:
        life -= 10
    if life < 1:
        playing = False
        
    all_spryte.draw(screen)

    screen.blit(text_hp, (10,10)) # TENGER SCORE

    #lage ny fiender 
    if len(Enemyattack_group) < 3:
        enemy_attack = EnemyAttack()
        all_spryte.add(enemy_attack)
        Enemyattack_group.add(enemy_attack)

    pg.display.update()
           







