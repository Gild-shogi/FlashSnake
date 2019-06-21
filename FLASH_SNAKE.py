#FLASH SNAKEというボールあてゲームです
#動き回るボールにパドルを当てましょう
#ボールが青の時に当てたら1点
#黄の時に当てたら10点入ります
#ボールを落としたら－5点です。
#出来るだけ高い点数を目指しましょう！




#使い方
#このウィンドウ（プログラム）1回クリックしてください
#F5でゲームスタート
#左矢印ボタンで左、右矢印で右にパドルが動きます
#ボールを五回落としたらゲーム終了
#ゲームはほおっておくと自動で終了します

#このプログラムは閉じないでください！

import pygame
import random
import time
import sys
import pygame.mixer

#set_color
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
YELLOW = (255,255,0)

#screen_draw
pygame.init()
pygame.display.set_caption('FLASH SNAKE')
screen = pygame.display.set_mode((700,500))

myclock = pygame.time.Clock()

#setting
flag = 0
x_paddle = 250
x_ball = 10
y_ball = 10
vector_x = 5
vector_y = 5
score = 0
result_score = 0
count = 0
v = 45

title = pygame.font.SysFont(None,100)
title_mode = title.render('FLASH SNAKE',True,(0,255,255))
screen.blit(title_mode,(0,100))
#timer
t = time.time()
while True:
    while flag == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = 1
        
            
    #paddle
        press = pygame.key.get_pressed()
        if(press[pygame.K_LEFT] and x_paddle > 0):
            x_paddle -= 10
            screen.fill(BLACK)
        if(press[pygame.K_RIGHT] and x_paddle < 600):
            x_paddle += 10

            screen.fill(BLACK)
            
        rect = pygame.Rect(x_paddle,400,100,30)
        pygame.draw.rect(screen,GREEN,rect)

    #ball
        if(y_ball == 390 and x_ball >= (x_paddle-5) and x_ball <= (x_paddle+95)):
            vector_y = -5
            score += 1
            result_score += 1
            screen.fill(BLACK)
            if kuji == 1:
                score += 10
                result_score += 10
                screen.fill(BLACK)
        #print(kuji)

        if(y_ball >= 500):
            x_ball = random.randrange(700)
            y_ball = 10
            vector_x = 5 * (random.randrange(0,3,2) - 1)
            vector_y = 5
            result_score -= 5
            score = 0
            count += 1

        if(y_ball <= 0):
            vector_y = 5
        if(x_ball >= 680):
            vector_x -= 5
        if(x_ball <= 0):
            vector_x = 5
        x_ball += vector_x
        y_ball += vector_y
    #bounus_time_color_shuffle
        kuji = random.randint(0,3)
        if kuji == 1:
           BALL = YELLOW
        else:
           BALL = BLUE
 
        pygame.draw.circle(screen,BALL,(x_ball,y_ball),10)

        if count == 5:
            screen.fill(YELLOW)
            pygame.init()
            break
    #score
        v = v + 0.01
        font = pygame.font.SysFont(None,80)
        score_text = font.render(str(score),True,(0,255,255))
        screen.blit(score_text,(630,10))

        pygame.display.flip()
        myclock.tick(v)
 

    pygame.quit()
    screen2 = pygame.display.set_mode((700,500))
    pygame.init()
    pygame.display.set_caption('FLASH SNAKE')

    while True:

        com = pygame.font.SysFont(None,80)
        comment = com.render('YOUR SCORE IS',True,(0,255,255))
        screen2.blit(comment,(0,100))
        scor = pygame.font.SysFont(None,200)
        scor_p = scor.render(str(result_score),True,(YELLOW))
        screen2.blit(scor_p,(200,300))
        pygame.display.update()

   
        press = pygame.key.get_pressed()
        time.sleep(10)
        break
    if(press[pygame.K_LEFT]):
        continue
    #for event in pygame.event.get():
      #  if event.type == QUIT:
         #   sys.exit()
pygame.quit()
#sys.exit()
