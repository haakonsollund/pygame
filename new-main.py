import pygame as pg
from random import randint
from spryte import *
from pygame import mixer

class Game():
    def __init__(self): # init skjer når vi lager game classen
        pg.init()
        self.WHITE = (255,255,255)
        self.BLACK = (0,0,0)
        self.RANDOM = (120,54,189)
        self.GREY = (64,64,64)
        self.FPS = 120
        self.WIDTH = 800
        self.HEIGHT = 600
        self.clock = pg.time.Clock()
        self.comic_sans30 = pg.font.SysFont("Comic Sans MS", 30)
        self.bg_img = pg.image.load("bakrund.png")
        self.bg_img = pg.transform.scale(self.bg_img, (800,600))
        self.screen = pg.display.set_mode((self.WIDTH,self.HEIGHT))
        self.samurai_img = pg.image.load("samurai.png")
        self.samurai_img = pg.transform.scale(self.samurai_img, (100,130)) # endre størelse på karakter
        self.Wizzard = pg.image.load("wizard_idle.png")
        self.Wizzard = pg.transform.scale(self.Wizzard, (100,130))
        mixer.music.load("Doom - Main Theme.mp3")
        mixer.music.play(-1)
        self.sound = pg.mixer.Sound("oof.mp3.mp3")
        pg.display.set_caption('ok        ')
       
        self.new()

    def game_over_loop(self):
        mixer.music.stop()
        mixer.music.load("end music.mp3")
        mixer.music.play(-1)
        self.game_over = True
        while self.game_over:
            self.clock.tick(self.FPS)
            self.game_over_text = self.comic_sans30.render("du døde trykk r for å restarte ", False, (255,0,0))


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_over = False
                    pg.quit()
 
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:  # om vi clicker på R, avslutter vi game over loop, og går derett til self.new() som ligger etter game_over loop
                        self.game_over = False  
 
            self.screen.fill(self.BLACK)
            self.screen.blit(self.game_over_text,(30,30))  # tegner tekst på skjerm. 
            self.text_hp = self.comic_sans30.render("SCORE: " + str(self.score), True, self.WHITE)
            self.screen.blit(self.text_hp,(30,60))
            
 
            pg.display.update()


        self.new()

    def game_win_loop(self):

        mixer.music.stop()
        mixer.music.load("end music.mp3")
        mixer.music.play(-1)
        self.game_over = True
        while self.game_over:
            self.clock.tick(self.FPS)
            self.game_over_text = self.comic_sans30.render("gratulerer du vant trykk r for å spille igjen ", False, (0,150,0))


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game_over = False
                    pg.quit()
 
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:  # om vi clicker på R, avslutter vi game over loop, og går derett til self.new() som ligger etter game_over loop
                        self.game_over = False  
 
            self.screen.fill(self.BLACK)
            self.screen.blit(self.game_over_text,(30,30))  # tegner tekst på skjerm. 
            self.text_hp = self.comic_sans30.render("SCORE: " + str(self.score), True, self.WHITE)
            self.screen.blit(self.text_hp,(30,60))


            pg.display.update()

        self.new()
            


    def new(self): # all kode som trengs for å starte en runde
        self.score = 0
        self.next_level_counter = 1000
        self.speed = 5
        self.life = 3
        self.level = 1
        self.boss_life = 1000
        mixer.music.stop
        mixer.music.load("Doom - Main Theme.mp3")
        mixer.music.play(-1)

        self.all_spryte = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        self.Enemyattack_group = pg.sprite.Group()
        self.Laserbeam_group = pg.sprite.Group()
        self.projectiles_grp = pg.sprite.Group()

        self.enemy = Enemy() 
        self.samurai = player(self)
        self.all_spryte.add(self.samurai)
        self.all_spryte.add(self.enemy)

        self.text_hp = self.comic_sans30.render("SCORE: " + str(self.score), True, self.WHITE)
        self.run()

    def level_select(self):

        if self.level == 1:
            if len(self.Enemyattack_group) < 3:
                enemy_attack = EnemyAttack()
                self.all_spryte.add(enemy_attack)
                self.Enemyattack_group.add(enemy_attack)
      

        elif self.level == 2:
            if len(self.Laserbeam_group) < 2:
                laser_beam = laserbeam()
                self.all_spryte.add(laser_beam)
                self.Laserbeam_group.add(laser_beam)
                self.Enemyattack_group.add(laser_beam)


    def run(self):            
        playing = True
        while playing: # game loop

            self.clock.tick(self.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    playing= False 
            
            self.screen.blit(self.bg_img,(0,0))
            
            
            self.score += 1
            text_hp = self.comic_sans30.render("SCORE: " + str(self.score), True, self.WHITE)
            
            self.all_spryte.update()

            hits = pg.sprite.spritecollide(self.samurai, self.Enemyattack_group,True)
            if hits:
                self.life -= 1
                pg.mixer.Sound.play(self.sound)
            
            if self.life < 1:
                playing = False

            hits2 = pg.sprite.groupcollide(self.projectiles_grp, self.Enemyattack_group, True, True)


            hits3 = pg.sprite.spritecollide(self.enemy, self.projectiles_grp,True)
            if hits3:
                self.boss_life -= 50
                
            
            if self.boss_life < 1:
             self.game_win_loop()
                
            self.all_spryte.draw(self.screen)

            self.screen.blit(text_hp, (10,10)) # TENGER SCORE

            #lage ny fiender 
            self.level_select()
            
            if (self.score > self.next_level_counter):
                self.level += 1
                self.next_level_counter += 1000
                for enemy in self.Enemyattack_group:
                    enemy.kill()
                self.Enemyattack_group = pg.sprite.Group()

            print(self.level)

            pg.display.update()
            
        self.game_over_loop() 

g = Game()


   