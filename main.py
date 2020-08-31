# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:46:41 2020

@author: KSHITIJ

credits : 
Pygame Tutorial for Beginners - Python Game Development Course < https://www.youtube.com/watch?v=FfWpgLFMI7w&t=662s >
alien.png ->  Icon made by <a href="http://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
88652_800x600.jpg -> Icon made by <a href='https://www.freepik.com/photos/abstract'>Abstract photo created by rawpixel.com - www.freepik.com</a>
spaceship.png ->  Icon made by <a href="https://www.flaticon.com/authors/smalllikeart" title="smalllikeart">smalllikeart</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
explosion.png ->  Icon made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
bullet.png -> # Icons made by <a href="https://www.flaticon.com/authors/good-ware" title="Good Ware">Good Ware</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
"""


import pygame
import random
from math import hypot
from time import sleep
from pygame import mixer


#initialize pygame

pygame.init()
pygame.key.set_repeat(100,100)

#create window 
mywindow  = pygame.display.set_mode((800,600))

#title of window
pygame.display.set_caption("Little Green Men")

#icon = pygame.image.load("abc.png")
#pygame.display.set_icon(icon)  

#background
background = pygame.image.load("88652_800x600.jpg") 

#Game over
game_end = 0 


#score system
score_val = 0
lives_val = 3
display_font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf',20)

def score_display(x,y):
    score  = display_font.render("Score: " + str(score_val), True, (255, 255, 255))
    mywindow.blit(score,(x,y))

def lives_display(x,y):
    lives = display_font.render("Lives: "+ str(lives_val),True, (255,255,255))
    mywindow.blit(lives,(x,y))


# Game over message
game_over_font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf',64)
your_score_font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf',32)

def game_over_message():
    game_over  = game_over_font.render("GAME OVER" , True, (255, 255, 255))
    your_score = your_score_font.render("Your Score: " + str(score_val), True, (255, 255, 255))
    mywindow.blit(game_over, (200,250))
    mywindow.blit(your_score,(280,330))

#player
player_image = pygame.image.load("spaceship.png") 
X_player = 350 #mod(730)
Y_player = 500 #mod(530)
X_delta = 0
Y_delta = 0
def player(x,y):
    mywindow.blit(player_image,(x,y))



# enemy (change enemy images btw)
enemy_image = []
X_enemy = []
Y_enemy = []
X_delta_enemy = []
Y_delta_enemy = []
num_of_enemy = 5

for i in range(0,num_of_enemy):
    enemy_image.append(pygame.image.load("alien.png")) 
    X_enemy.append(random.randint(0,739))
    Y_enemy.append(random.randint(0,150))
    X_delta_enemy.append(random.choice((-1,1))*2)
    Y_delta_enemy.append(random.random())

def enemy(x,y,i):
    mywindow.blit(enemy_image[i],(x, y))

#explosion
#explosion_img = pygame.image.load("explosion.png")
#def explosion(x,y):
#   mywindow.blit(explosion_img,(x,y)) 


#bullet
bullet_image = pygame.image.load("bullet.png")
X_bullet = X_player
Y_bullet = Y_player
Y_delta_bullet = -4
bullet_state = 0 # 0 => loaded, 1 => fired

def fire_bullet(x,y):
    global bullet_state
    bullet_state = 1
    mywindow.blit(bullet_image,(x + 16, y + 5))



#collision
def collision(x,y,a,b):
    if hypot(abs(a-x), abs(b-y)) < 20:
        return True
    else:
        return False


running = True

#game running while while running
while running:

    #background colour
    mywindow.fill((23,19,19))
    #background image
    mywindow.blit(background,(0,0))

    #handling events
    for event in pygame.event.get():

        #closing condition
        if event.type == pygame.QUIT:
            running = False

        #movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_a or event.key == pygame.K_KP4:
                #print("left")
                X_delta -= 3
            if event.key == pygame.K_RIGHT or  event.key == pygame.K_d or event.key == pygame.K_KP6:
                #print("right")
                X_delta += 3
            if event.key == pygame.K_UP or  event.key == pygame.K_w or event.key == pygame.K_KP8:
                #print("up")
                Y_delta -= 2.7
            if event.key == pygame.K_DOWN or  event.key == pygame.K_s or event.key == pygame.K_KP5:
                #print(Y_delta) #check when T_delta = 0 and multiple down presses
                Y_delta += 2.7
            if event.key == pygame.K_SPACE: #(add mouseclick)
                if bullet_state is 0 and game_end is 0:
                    bullet_sound = mixer.Sound('gun+shot2.wav')
                    bullet_sound.play()
                    X_bullet = X_player
                    fire_bullet(X_bullet,Y_bullet)
        

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_KP4 or event.key == pygame.K_RIGHT or  event.key == pygame.K_d or event.key == pygame.K_KP6:
                #print("key released")
                X_delta = 0
            if event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_KP8 or event.key == pygame.K_DOWN or  event.key == pygame.K_s or event.key == pygame.K_KP5:
                Y_delta = 0


    X_player = X_player + X_delta
    Y_player = Y_player + Y_delta

    if Y_player >= 530 or Y_player <= 0:
        Y_delta = 0

    if X_player >= 739 or X_player <= 0:
        X_delta = 0
    
    

    #enemy movement

    for i in range(num_of_enemy):
        
        # game over
        if Y_enemy[i] >= Y_player and Y_enemy[i] < 1000:
            Y_enemy[i] = 2000
            lives_val -= 1
            if lives_val == 0:
                for j in Y_enemy:
                    j = 2000
                game_end = 1    
                

                

        if X_enemy[i] <= 0 or X_enemy[i] >= 739:
            X_delta_enemy[i] = -(X_delta_enemy[i])
            #Y_enemy += Y_delta_enemy

        X_enemy[i] += X_delta_enemy[i]
        # For continuous downward movement: use the following here and remove this from if statement
        Y_enemy[i] += Y_delta_enemy[i]

        if collision(X_enemy[i], Y_enemy[i], X_bullet, Y_bullet) and bullet_state is 1:
            explosion_sound = mixer.Sound('explosion+7.wav')
            explosion_sound.play()
            Y_bullet = Y_player
            bullet_state = 0
            score_val += 1
            #explosion(X_enemy, Y_enemy) implement explosion
            X_enemy[i] = random.randint(0,739)
            Y_enemy[i] = random.randint(0,150)
    
        enemy(X_enemy[i],Y_enemy[i],i)

    
    if bullet_state is 1:
        fire_bullet(X_bullet, Y_bullet)
        Y_bullet += Y_delta_bullet

    if Y_bullet < 0:
        bullet_state = 0
        #X_bullet = X_player
        Y_bullet = Y_player
    
    if game_end == 0:
    
        player(X_player,Y_player)
        score_display(20,20)
        lives_display(710,20)
    
    else:
        game_over_message()



    pygame.display.update()
