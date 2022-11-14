import pygame as pg
from random import randint
from spryte import*


pg.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RANDOM = (120,54,189)
GREY = (64,64,64)
FPS = 120
clock = pg.time.Clock()
x = 30
y = 30
speed = 5
life = 100
x2 = 670

y2 = 670

fps_counter = 0
direction_x = 1
direction_y = 1
box_color = RANDOM
direction_x2 = -1
direction_y2 = -1

screen = pg.display.set_mode((800,600))
samurai_img = pg.image.load("samurai.png")
samurai_img = pg.transform.scale(samurai_img, (100,130)) # endre størelse på karakter

all_spryte = pg.sprite.Group()
enemy_group = pg.sprite.Group()
Enemyattack_group = pg.sprite.Group()

enemy = Enemy()
samurai = player()


all_spryte.add(samurai)
all_spryte.add(enemy)


enemy_attack = EnemyAttack()
all_spryte.add(enemy_attack)
enemy_attack2 = EnemyAttack()
all_spryte.add(enemy_attack2)
Enemyattack_group.add(enemy_attack, enemy_attack2)

playing = True
while playing: # game loop
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing= False 
    

    screen.fill(GREY)
    all_spryte.update()


    hits = pg.sprite.spritecollide(samurai, Enemyattack_group,True)
    if hits:
        life -= 10
    if life < 1:
        playing = False
        
    all_spryte.draw(screen)
    
    


    #lage ny fiender 
    if len(Enemyattack_group) < 4:
        enemy_attack = EnemyAttack()
        all_spryte.add(enemy_attack)
        Enemyattack_group.add(enemy_attack)

    
#move box

   

    x2 += direction_x2

    y2 += direction_y2

    if x > 700:
        rand1 = randint(1,1)
        box_color = (randint(0,255),randint(0,255),randint(0,255))
        rand1 = rand1*-1
    
        
        x = 700

    if x < 0:
        rand2 = randint(1,1)
        box_color = (randint(0,255),randint(0,255),randint(0,255))
        
        x = 0
    
    if y > 500:
        rand3 = randint(1,1)
        rand3 = rand3*-1
        box_color = (randint(0,255),randint(0,255),randint(0,255))

        y = 500

    if y < 0:
        rand4 = randint(1,1)
        box_color = (randint(0,255),randint(0,255),randint(0,255))

        y = 0
    


  # SECOND BOX/ENEMY¨
    if x2 > 700:
        rand12 = randint(1,5)
        box_color = (randint(0,255),randint(0,255),randint(0,255))
        rand12 = rand12*-1
    
        
        direction_x2 = rand12

    if x2 < 0:
        rand22 = randint(1,5)
        box_color = (randint(4,255),randint(116,255),randint(24,255))
        
        direction_x2 = rand22
    
    if y2 > 500:
        rand32 = randint(1,5)
        rand32 = rand32*-1
        box_color = (randint(0,255),randint(0,255),randint(0,255))

        direction_y2 = rand32

    if y2 < 0:
        rand42 = randint(1,5)
        box_color = (randint(0,255),randint(0,255),randint(0,255))

        direction_y2 = rand42
    




 

   

    pg.display.update()
           







