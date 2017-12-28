import pygame as pg
import sys,random,os
from pygame.locals import * 

title = pg.image.load(os.path.join("res/title2.png"))
background = pg.image.load(os.path.join("res/back.jpg"))
background2 = pg.image.load(os.path.join("res/back2.png"))
startBtn = pg.image.load(os.path.join("res/start_button3.png"))
exitBtn = pg.image.load(os.path.join("res/exit_button3.png"))
restartBtn = pg.image.load(os.path.join("res/restart_button2.png"))
startBtnHvr = pg.image.load(os.path.join("res/start_button_hover2.png"))
exitBtnHvr = pg.image.load(os.path.join("res/exit_button_hover2.png"))
restartBtnHvr = pg.image.load(os.path.join("res/restart_button_hover2.png"))
hole = pg.image.load(os.path.join("res/hole3.png"))
gameover = pg.image.load(os.path.join("res/gameover.png"))

stand = pg.image.load(os.path.join("res/player/PNG/Player/Poses/player_stand.png"))
jump = pg.image.load(os.path.join("res/player/PNG/Player/Poses/player_jump.png"))
hurt = pg.image.load(os.path.join("res/player/PNG/Player/Poses/player_hurt.png"))
walk = ["res/player/PNG/Player/Poses/player_walk1.png","res/player/PNG/Player/Poses/player_walk2.png"]

hit_sound = "audio/collision.mp3"
background_music = "audio/8bitloop.mp3"
gameover_sound = "audio/gameover.mp3"

hole = pg.transform.scale(hole,(100,50))
gameover = pg.transform.scale(gameover,(800,450))
background = pg.transform.scale(background,(800,450))
background2 = pg.transform.scale(background2,(800,450))
startBtn = pg.transform.scale(startBtn, (100, 50))
exitBtn = pg.transform.scale(exitBtn, (100, 50))
restartBtn = pg.transform.scale(restartBtn, (150, 50))
startBtnHvr = pg.transform.scale(startBtnHvr, (100, 50))
exitBtnHvr = pg.transform.scale(exitBtnHvr, (100, 50))
restartBtnHvr = pg.transform.scale(restartBtnHvr, (150, 50))

class startmenu():
    def __init__(self):
        self.screen = pg.display.set_mode((800,450))
        self.click0, self.loads = False, False

    def mainloop(self):
        play_sound(background_music,True)
        while True:
            self.screen.blit(background2,background2.get_rect())
            self.screen.blit(title,(130,150))
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
        self.screen.blit(background2,background2.get_rect())
        self.plr = player(self.screen)
        self.holes = []
        self.score = 0
        self.click0 = False

    def make_text(self, x, y, text, size=20, color = (0,0,0), a = False):
        txts = pg.font.SysFont('Courier New', size).render(text, True, color)
        txtrect = txts.get_rect()
        txtrect.topleft = (x,y)
        if a == True:
            txtrect.center = (x,y)
        self.screen.blit(txts, txtrect)

    def loop(self):
        self.game_over = False
        x = 0
        hpos = 830
        while self.game_over != True:
            x -= self.speed
            xrel = x % background2.get_rect().width
            if xrel==0:
                x = 0
            self.screen.blit(background2,(xrel,0))
            self.screen.blit(background2,(-(background2.get_rect().width - xrel),0))

            self.plr.update()
            self.make_text(400, 50, str(self.score) + "m", color = (0,0,0), size = 50, a = True)

            if (pg.time.get_ticks() - self.timer) > self.hole_spawn_rate:
                self.score += 1
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

            player_rect = pg.Rect(self.plr.pwalk.get_rect())
            player_rect.left = self.plr.x
            player_rect.top = self.plr.y
            for h in self.holes:
                hole_rect = pg.Rect(h.rect)
                hole_rect.left = h.x
                hole_rect.top = h.y
                if player_rect.colliderect(hole_rect):
                    play_sound(hit_sound)
                    self.game_over = self.restartScreen(xrel)       
            pg.display.update()

    def restartScreen(self,xrel):
        while True:
            self.screen.blit(background2,(xrel,0))
            self.screen.blit(background2,(-(background2.get_rect().width - xrel),0))
            self.screen.blit(hurt,(self.plr.x,self.plr.y))
            for h in self.holes:
                self.screen.blit(hole,(h.x,h.y))        
            self.screen.blit(gameover,gameover.get_rect())
            self.make_text(400, 50, "Score: " + str(self.score) + "m", color = (255,255,255), size = 50, a = True)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            
            pos = (150, 300,100,50)
            mouse = pg.mouse.get_pos()
            if (pos[0]+pos[2]+50) > mouse[0] > pos[0] and (pos[1]+pos[3]) > mouse[1] > pos[1]:
                self.screen.blit(restartBtnHvr,(150, 300,150,50))
                self.screen.blit(exitBtn,(550, 300,100,50))
                click = pg.mouse.get_pressed()
                if click[0] == 1:
                    self.click0 = True
                if self.click0 == True:
                    if click[0] == 0:
                        self.click0 = False
                        play_sound(background_music,True)
                        return True
            elif (550+pos[2]) > mouse[0] > 550 and (pos[1]+pos[3]) > mouse[1] > pos[1]:
                self.screen.blit(restartBtn,(150, 300,150,50))
                self.screen.blit(exitBtnHvr,(550, 300,100,50))
                click = pg.mouse.get_pressed()
                if click[0] == 1:
                    self.click0 = True
                if self.click0 == True:
                    if click[0] == 0:
                        self.click0 = False
                        sys.exit()
            else:
                self.screen.blit(restartBtn,(150, 300,150,50))
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

        self.keys = self.get_user_input()
        self.handle_events()
        
        self.screen.blit(self.pwalk,(self.x,self.y))

    def get_user_input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        keys = pg.key.get_pressed()
        return keys

    def handle_events(self):
        x = self.x
        y = self.y
        vel = 2
        if self.keys[pg.K_UP] and self.jumping== False:
            self.jumping = True
        elif self.keys[pg.K_RIGHT] and x + vel + stand.get_rect().width < 800:
            self.x += vel
        elif self.keys[pg.K_LEFT] and x - vel > 0:
            self.x -= vel
        elif self.keys[pg.K_DOWN] and y + vel < 235:
            self.y += vel
        else:
            pass

class cavity:
    def __init__(self,screen,distance):
        self.screen = screen
        self.rect = hole.get_rect()
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

def play_sound(link,inf=False):
    pg.mixer.music.load(link)
    pg.mixer.music.set_volume(0.5)
    if inf:
        pg.mixer.music.set_volume(0.25)
        pg.mixer.music.play(-1, 0.0)
    else:
        pg.mixer.music.play(0, 0.0)
    
def menu():
    global m
    pg.init()
    pg.mixer.init()
    m = startmenu()
    m.mainloop()

menu()