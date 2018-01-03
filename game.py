import pygame as pg
import sys,random,os
from ResourcesLoader import *
from pygame.locals import * 

class startmenu():
    def __init__(self):
        self.screen = pg.display.set_mode((800,450))
        self.click0, self.loads = False, False

    def mainloop(self):
        #play_sound(background_music,True)
        while True:
            self.screen.blit(background2,background2.get_rect())
            self.screen.blit(title,(148,100))
            #make_text(self.screen, 400, 100, "JUNGLE RUN", color = (130, 82, 1), size = 100, a = True)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            
            pos = (150, 300,100,50)
            mouse = pg.mouse.get_pos()
            if (pos[0]+pos[2]) > mouse[0] > pos[0] and (pos[1]+pos[3]) > mouse[1] > pos[1]:
                self.screen.blit(startBtnHvr,(150, 300,100,50))
                self.screen.blit(exitBtn,(550, 300,100,50))
                click = pg.mouse.get_pressed()
                if click[0] == 1:
                    self.click0 = True
                if self.click0 == True:
                    if click[0] == 0:
                        play_sound(background_music,True)
                        self.start()
                        self.click0 = False
            elif (550+pos[2]) > mouse[0] > 550 and (pos[1]+pos[3]) > mouse[1] > pos[1]:
                self.screen.blit(startBtn,(150, 300,100,50))
                self.screen.blit(exitBtnHvr,(550, 300,100,50))
                click = pg.mouse.get_pressed()
                if click[0] == 1:
                    self.click0 = True
                if self.click0 == True:
                    if click[0] == 0:
                        self.exit()
                        self.click0 = False
            else:
                self.screen.blit(startBtn,(150, 300,100,50))
                self.screen.blit(exitBtn,(550, 300,100,50))

            pg.display.update()

    def start(self):
        start(1,1)

    def exit(self):
        sys.exit()

class game():
    def __init__(self,speed):
        self.screen = pg.display.set_mode((800,450))
        pg.display.set_caption('Surakshit Karo')
        self.screen.fill([255, 255, 255])
        self.speed = speed
        self.timer = 0.0
        self.hole_spawn_rate = 1000
        self.bird_spawn_rate = 1000
        self.screen.blit(background2,background2.get_rect())
        self.plr = player(self.screen)
        self.brd = None
        self.holes = []
        self.dead_bird = []
        self.lives = 3
        self.score = 0
        self.distance = 0
        self.click0 = False

    def loop(self):
        self.game_over = False
        x = 0
        hpos = 830
        while self.game_over != True:
            #BACKGROUND
            x -= self.speed
            xrel = x % background2.get_rect().width
            if xrel==0:
                x = 0
            self.screen.blit(background2,(xrel,0))
            self.screen.blit(background2,(-(background2.get_rect().width - xrel),0))

            #PLAYER
            self.plr.update()

            #BIRD
            if (pg.time.get_ticks() - self.timer) > self.bird_spawn_rate and self.brd==None:
                height = random.randrange(50,300)
                self.brd = bird(self.screen,height)

            if self.brd!=None:
                self.brd.update()
                if self.brd.x < -(self.brd.bfly.get_rect().width):
                    self.brd = None
            
            for b in self.dead_bird:
                self.screen.blit(bird_dead,(b.x,b.y))    
                b.y += 1
                if b.y == 320:
                    self.dead_bird.remove(b)

            #HUD
            bird_k = pg.image.load(os.path.join(bird_anim[0]))
            bird_k = pg.transform.scale(bird_k,(50,30))
            if self.lives==3:
                self.screen.blit(life_img,(30,50))
                self.screen.blit(life_img,(30 + life_img.get_rect().width,50))
                self.screen.blit(life_img,(30 + 2 * life_img.get_rect().width ,50))
            elif self.lives==2:
                self.screen.blit(life_img,(30,50))
                self.screen.blit(life_img,(30 + life_img.get_rect().width,50))
            elif self.lives==1:
                self.screen.blit(life_img,(30,50))
            self.screen.blit(bird_k,(350,30))
            make_text(self.screen,80, 30, "LIVES", color = (0,0,0), size=38, a = True)
            make_text(self.screen,380 + bird_k.get_rect().width, 50, "X" + str(self.score), color = (0,0,0), size=40, a = True)
            make_text(self.screen, 700, 50, str(self.distance) + "m", color = (0,0,0), size = 40, a = True)

            #HOLES
            if (pg.time.get_ticks() - self.timer) > self.hole_spawn_rate:
                self.distance += 1
                gap = random.randrange(100,800) 
                if len(self.holes) == 0:       
                    self.holes.append(cavity(self.screen,hpos + gap))
                else:
                    addhole = True
                    for h in self.holes:
                        if abs(hpos + gap - h.x) < 250:
                            addhole = False
                            break
                    if addhole:
                        self.holes.append(cavity(self.screen,hpos + gap))
                self.timer = pg.time.get_ticks()
            

            for h in self.holes:
                if h.x < -(hole.get_rect().width):
                    self.holes.remove(h)
                else:
                    h.update()

            #COLLISION
            player_rect = pg.Rect(self.plr.pwalk.get_rect())
            player_rect.left = self.plr.x
            player_rect.top = self.plr.y
            for h in self.holes:
                hole_rect = pg.Rect((h.x + 50,h.y),(5,50))
                if player_rect.colliderect(hole_rect) and self.plr.protection==False:
                    play_sound(gameover_sound)
                    self.lives -= 1
                    self.game_over = self.restartScreen(xrel)   
                    if self.game_over==False:
                        self.plr.protection = True  
                        self.plr.safe_timer = pg.time.get_ticks()

            if self.brd!=None:
                bird_rect = pg.Rect((self.brd.x + 20,self.brd.y + 10),(30,20))
                if player_rect.colliderect(bird_rect) and self.plr.protection==False:
                    if player_rect.top + player_rect.height/2 > bird_rect.top:
                        play_sound(gameover_sound)
                        self.lives -= 1
                        self.game_over = self.restartScreen(xrel)  
                        if self.game_over==False:
                            self.plr.protection = True  
                            self.plr.safe_timer = pg.time.get_ticks()  
                    else:
                        hit.play()
                        self.score += 1
                        self.dead_bird.append(self.brd)
                        self.brd = None

            pg.display.update()

    def restartScreen(self,xrel):
        while True:
            self.screen.blit(background2,(xrel,0))
            self.screen.blit(background2,(-(background2.get_rect().width - xrel),0))
            self.screen.blit(hurt,(self.plr.x,self.plr.y))
            for h in self.holes:
                self.screen.blit(hole,(h.x,h.y))     
            if self.brd!=None:
                self.screen.blit(self.brd.bfly,(self.brd.x,self.brd.y))       
            self.screen.blit(gameover,gameover.get_rect())
            make_text(self.screen, 400, 50, "Score: " + str(self.score * 30 + self.distance) + " pts", color = (255,255,255), size = 50, a = True)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            
            pos = (150, 300,100,50)
            mouse = pg.mouse.get_pos()
            if (pos[0]+pos[2]+50) > mouse[0] > pos[0] and (pos[1]+pos[3]) > mouse[1] > pos[1]:
                if self.lives==0:
                    self.screen.blit(restartBtnHvr,(150, 300,150,50))
                else:
                    self.screen.blit(continueBtnHvr,(150, 300,150,50))
                self.screen.blit(exitBtn,(550, 300,100,50))
                click = pg.mouse.get_pressed()
                if click[0] == 1:
                    self.click0 = True
                if self.click0 == True:
                    if click[0] == 0:
                        self.click0 = False
                        #self.lives -= 1
                        if self.lives==0:
                            return True
                        else:
                            play_sound(background_music,True)
                            return False
            elif (550+pos[2]) > mouse[0] > 550 and (pos[1]+pos[3]) > mouse[1] > pos[1]:
                if self.lives==0:
                    self.screen.blit(restartBtn,(150, 300,150,50))
                else:
                    self.screen.blit(continueBtn,(150, 300,150,50))
                self.screen.blit(exitBtnHvr,(550, 300,100,50))
                click = pg.mouse.get_pressed()
                if click[0] == 1:
                    self.click0 = True
                if self.click0 == True:
                    if click[0] == 0:
                        self.click0 = False
                        sys.exit()
            else:
                if self.lives==0:
                    self.screen.blit(restartBtn,(150, 300,150,50))
                else:
                    self.screen.blit(continueBtn,(150, 300,150,50))
                self.screen.blit(exitBtn,(550, 300,100,50))

            pg.display.update()
        

class player():
    def __init__(self,screen):
        self.screen = screen       
        self.x = 20
        self.gravity = 1
        self.y = 235
        self.counter = 0
        self.jumping = False
        self.protection = False
        self.safe_time = 5000
        self.safe_timer = 0.0
        self.ducking = False
        self.velocity = [-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.velocity_index = 0
        self.timer = 0.0
        self.jump_timer = 0.0
        self.jump_speed = 20
        self.walk_speed = 300
        self.screen.blit(stand,(self.x,self.y))

    def update(self):
        if (pg.time.get_ticks() - self.timer) > self.walk_speed:
            self.counter = (self.counter + 1) % len(walk) 
            self.timer = pg.time.get_ticks()

        self.pwalk = pg.image.load(walk[self.counter])

        if self.jumping == True:
            self.pwalk = jump
            if (pg.time.get_ticks() - self.jump_timer) > self.jump_speed:
                if self.y + self.velocity[self.velocity_index] < 235:
                    self.y += self.velocity[self.velocity_index]
                else:
                    self.y = 235
                self.velocity_index = (self.velocity_index + 1) % len(self.velocity)
                if self.velocity_index == 0:
                    self.jumping = False
                self.jump_timer = pg.time.get_ticks()

        if self.ducking == True:
            self.pwalk = duck
            self.y -= 10
            self.ducking = False

        #self.keys = self.get_user_input()
        self.handle_events(self.get_user_input())
        if self.protection==True:
            if (pg.time.get_ticks() - self.safe_timer) > self.safe_time:
                self.protection = False
            else:
                self.screen.blit(shield_img,(self.x-35,self.y-15))
        self.screen.blit(self.pwalk,(self.x,self.y))

    def get_user_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        keys = pg.key.get_pressed()
        return keys

    def handle_events(self,keys):
        x = self.x
        y = self.y
        vel = 2
        if keys[pg.K_UP] and self.jumping== False:
            self.jumping = True
        elif keys[pg.K_RIGHT] and x + vel + stand.get_rect().width < 800:
            self.x += vel
        elif keys[pg.K_LEFT] and x - vel > 0:
            self.x -= vel
        elif keys[pg.K_DOWN]:
            if y + vel < 235:
                self.y += vel
            else:
                self.y += 10
                self.ducking = True
        else:
            pass

class bird():
    def __init__(self,screen,distance):
        self.screen = screen
        self.y = distance
        self.x = 820
        self.timer = 0.0
        self.counter = 0
        self.bird_flap_speed = 60
        self.bird_fly_speed = 2

    def update(self):
        self.x -= self.bird_fly_speed
        self.bfly = pg.image.load(bird_anim[self.counter])
        self.bfly = pg.transform.scale(self.bfly,(100,50))
        if (pg.time.get_ticks() - self.timer) > self.bird_flap_speed:
            self.counter = (self.counter + 1) % len(bird_anim) 
            self.timer = pg.time.get_ticks()
        
        self.screen.blit(self.bfly,(self.x,self.y))

class cavity:
    def __init__(self,screen,distance):
        self.screen = screen
        self.x = distance
        self.y = 340
        self.timer = 0.0

    def update(self):
        self.x -= 1
        self.screen.blit(hole,(self.x,self.y))

def start(speed,size):
    global g
    g = game(speed)
    g.loop()

def make_text(screen,x, y, text, size=20, color = (0,0,0), a = False):
    txts = pg.font.SysFont('Courier New', size).render(text, True, color)
    txtrect = txts.get_rect()
    txtrect.topleft = (x,y)
    if a == True:
        txtrect.center = (x,y)
    screen.blit(txts, txtrect)

def play_sound(link,inf=False):
    pg.mixer.music.load(link)
    pg.mixer.music.set_volume(0.5)
    if inf:
        pg.mixer.music.set_volume(0.25)
        pg.mixer.music.play(-1, 0.0)
    else:
        pg.mixer.music.play(0, 0.0)
    
def menu():
    global m,hit
    pg.init()
    pg.mixer.init()
    hit = pg.mixer.Sound(hit_sound)
    m = startmenu()
    m.mainloop()

menu()