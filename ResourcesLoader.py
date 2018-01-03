import pygame as pg
import os

title = pg.image.load(os.path.join("res/title3.png"))
playerSelect = pg.image.load(os.path.join("res/player_select.png"))
background = pg.image.load(os.path.join("res/back.jpg"))
background2 = pg.image.load(os.path.join("res/back2.png"))
startBtn = pg.image.load(os.path.join("res/start_button3.png"))
exitBtn = pg.image.load(os.path.join("res/exit_button3.png"))
continueBtn = pg.image.load(os.path.join("res/continue_button.png"))
restartBtn = pg.image.load(os.path.join("res/restart_button2.png"))
startBtnHvr = pg.image.load(os.path.join("res/start_button_hover2.png"))
exitBtnHvr = pg.image.load(os.path.join("res/exit_button_hover2.png"))
continueBtnHvr = pg.image.load(os.path.join("res/continue_button_hover.png"))
restartBtnHvr = pg.image.load(os.path.join("res/restart_button_hover2.png"))
hole = pg.image.load(os.path.join("res/hole3.png"))
gameover = pg.image.load(os.path.join("res/gameover.png"))
life_img = pg.image.load(os.path.join("res/player/GreenHorn/life.png"))
shield_img = pg.image.load(os.path.join("res/shield.png"))

stand = pg.image.load(os.path.join("res/player/GreenHorn/Poses/player_stand.png"))
jump = pg.image.load(os.path.join("res/player/GreenHorn/Poses/player_jump.png"))
hurt = pg.image.load(os.path.join("res/player/GreenHorn/Poses/player_hurt.png"))
duck = pg.image.load(os.path.join("res/player/GreenHorn/Poses/player_duck.png"))
walk = ["res/player/GreenHorn/Poses/player_walk1.png","res/player/GreenHorn/Poses/player_walk2.png"]

character = [{"stand":"res/player/GreenHorn/Poses/player_stand.png",
                "jump": "res/player/GreenHorn/Poses/player_jump.png",
                "hurt":"res/player/GreenHorn/Poses/player_hurt.png",
                "duck":"res/player/GreenHorn/Poses/player_duck.png",
                "walk":["res/player/GreenHorn/Poses/player_walk1.png","res/player/GreenHorn/Poses/player_walk2.png"],
                "life_img":"res/player/GreenHorn/life.png"},
               {"stand":"res/player/SleepWalker/Poses/zombie_stand.png",
                "jump": "res/player/SleepWalker/Poses/zombie_jump.png",
                "hurt":"res/player/SleepWalker/Poses/zombie_hurt.png",
                "duck":"res/player/SleepWalker/Poses/zombie_duck.png",
                "walk":["res/player/SleepWalker/Poses/zombie_walk1.png","res/player/SleepWalker/Poses/zombie_walk2.png"],
                "life_img":"res/player/SleepWalker/life.png"},
                {"stand":"res/player/DukeCage/Poses/soldier_stand.png",
                "jump": "res/player/DukeCage/Poses/soldier_jump.png",
                "hurt":"res/player/DukeCage/Poses/soldier_hurt.png",
                "duck":"res/player/DukeCage/Poses/soldier_duck.png",
                "walk":["res/player/DukeCage/Poses/soldier_walk1.png","res/player/DukeCage/Poses/soldier_walk2.png"],
                "life_img":"res/player/DukeCage/life.png"},
                {"stand":"res/player/IndianaBones/Poses/adventurer_stand.png",
                "jump": "res/player/IndianaBones/Poses/adventurer_jump.png",
                "hurt":"res/player/IndianaBones/Poses/adventurer_hurt.png",
                "duck":"res/player/IndianaBones/Poses/adventurer_duck.png",
                "walk":["res/player/IndianaBones/Poses/adventurer_walk1.png","res/player/IndianaBones/Poses/adventurer_walk2.png"],
                "life_img":"res/player/IndianaBones/life.png"},
                {"stand":"res/player/LanaRoft/Poses/female_stand.png",
                "jump": "res/player/LanaRoft/Poses/female_jump.png",
                "hurt":"res/player/LanaRoft/Poses/female_hurt.png",
                "duck":"res/player/LanaRoft/Poses/female_duck.png",
                "walk":["res/player/LanaRoft/Poses/female_walk1.png","res/player/LanaRoft/Poses/female_walk2.png"],
                "life_img":"res/player/LanaRoft/life.png"}]


bird_dead = pg.image.load(os.path.join("res/bird/dead.png"))
bird_anim = ["res/bird/fly1.png","res/bird/fly2.png","res/bird/fly3.png","res/bird/fly4.png"]

hit_sound = "audio/hit.wav"
background_music = "audio/8bitloop.mp3"
gameover_sound = "audio/gameover3.wav"

title = pg.transform.scale(title,(500,100))
playerSelect = pg.transform.scale(playerSelect,(400,50))
bird_dead = pg.transform.scale(bird_dead,(100,50))
life_img = pg.transform.scale(life_img,(30,30))
shield_img = pg.transform.scale(shield_img,(160,160))
hole = pg.transform.scale(hole,(100,50))
gameover = pg.transform.scale(gameover,(800,450))
background = pg.transform.scale(background,(800,450))
background2 = pg.transform.scale(background2,(800,450))
startBtn = pg.transform.scale(startBtn, (100, 50))
exitBtn = pg.transform.scale(exitBtn, (100, 50))
continueBtn = pg.transform.scale(continueBtn, (150, 50))
restartBtn = pg.transform.scale(restartBtn, (150, 50))
startBtnHvr = pg.transform.scale(startBtnHvr, (100, 50))
exitBtnHvr = pg.transform.scale(exitBtnHvr, (100, 50))
continueBtnHvr = pg.transform.scale(continueBtnHvr, (150, 50))
restartBtnHvr = pg.transform.scale(restartBtnHvr, (150, 50))