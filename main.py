import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000,400))
pygame.display.set_caption('Obstacle Game')
white = (255,255,255)
red = (255,0,0)

Red = pygame.image.load('red.png')
Blue = pygame.image.load('blue.png')
Green = pygame.image.load('green.png')
Yellow = pygame.image.load('yellow.png')
Yellow = pygame.transform.scale(Yellow,(50,50))
title = pygame.image.load('title.png')
title = pygame.transform.scale(title,(1000,400))
obs = pygame.image.load('obs.png')
obs = pygame.transform.scale(obs, (40, 200))
char = pygame.image.load('char.png')
char = pygame.transform.scale(char, (50, 50))
font = pygame.font.Font('freesansbold.ttf', 20)


def playgame():
    backx = 0
    backy = 0
    obs1x = 300
    obs1y = 200
    obs2x = 500
    obs2y = 0
    charx = 0
    chary = 10
    charvel = 0.3
    score = 0
    level = 1

    game = False
    gameover = False
    pause = False
    run = False

    backvel = 0


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_0:
                    if backy == 0:
                        backvel = 0.5
                        game = True
                if event.key == K_SPACE:
                    playgame()
                if event.key == K_LCTRL:
                    run = True
                if event.key == K_p:
                    pause = True
                if event.key == K_s:
                    pause = False
        if run==False:
            screen.blit(title,(0,0))
            pygame.display.update()
        if run==True:
            if pause == True:
                continue

            if game:
                score += 1

            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP] and chary > 0:
                chary -= charvel
            if keys[pygame.K_DOWN] and chary < 350:
                chary += charvel

            backx -= backvel
            obs1x -= backvel
            obs2x -= backvel

            text = font.render('Score: ' + str(score), True, white)
            text1 = font.render('Game Over Press Space To Start Again', True, white)
            text2 = font.render('Level: ' + str(level), True, white)

            if backx < -3600:
                backx = 0
                obs1x = 300
                obs2x = 500
                backvel += 0.05
                charvel += 0.05
                level += 1

            if chary<5 or chary>350:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs1x < charx + 50 < obs1x + 40 and obs1y < chary + 50 < obs1y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs1x + 400 < charx + 50 < obs1x + 440 and obs1y < chary + 50 < obs1y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs1x + 800 < charx + 50 < obs1x + 840 and obs1y < chary + 50 < obs1y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs1x + 1200 < charx + 50 < obs1x + 1240 and obs1y < chary + 50 < obs1y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs1x + 1600 < charx + 50 < obs1x + 1640 and obs1y < chary + 50 < obs1y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs1x + 2000 < charx + 50 < obs1x + 2040 and obs1y < chary + 50 < obs1y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs1x + 2400 < charx + 50 < obs1x + 2440 and obs1y < chary + 50 < obs1y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs1x + 2800 < charx + 50 < obs1x + 2840 and obs1y < chary + 50 < obs1y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs1x + 3200 < charx + 50 < obs1x + 3240 and obs1y < chary + 50 < obs1y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs2x < charx + 50 < obs2x + 40 and obs2y <= chary <= obs2y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs2x + 400 < charx + 50 < obs2x + 440 and obs2y <= chary <= obs2y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs2x + 800 < charx + 50 < obs2x + 840 and obs2y <= chary <= obs2y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs2x + 1200 < charx + 50 < obs2x + 1240 and obs2y <= chary <= obs2y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs2x + 1600 < charx + 50 < obs2x + 1640 and obs2y <= chary <= obs2y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs2x + 2000 < charx + 50 < obs2x + 2040 and obs2y <= chary <= obs2y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs2x + 2400 < charx + 50 < obs2x + 2440 and obs2y <= chary <= obs2y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            if obs2x + 2800 < charx + 50 < obs2x + 2840 and obs2y <= chary <= obs2y + 200:
                backvel = 0
                charvel = 0
                gameover = True
                game = False

            screen.fill(white)
            screen.blit(Red, (backx, backy))
            screen.blit(Red, (backx + 600, backy))
            screen.blit(Blue, (backx + 1200, backy))
            screen.blit(Blue, (backx + 1800, backy))
            screen.blit(Green, (backx + 2400, backy))
            screen.blit(Green, (backx + 3000, backy))
            screen.blit(Red, (backx + 3600, backy))
            screen.blit(obs, (obs1x, obs1y))
            screen.blit(obs, (obs2x, obs2y))
            screen.blit(obs, (obs1x + 400, obs1y))
            screen.blit(obs, (obs2x + 400, obs2y))
            screen.blit(obs, (obs1x + 800, obs1y))
            screen.blit(obs, (obs1x + 1200, obs1y))
            screen.blit(obs, (obs2x + 800, obs2y))
            screen.blit(obs, (obs1x + 1600, obs1y))
            screen.blit(obs, (obs2x + 1200, obs2y))
            screen.blit(obs, (obs1x + 2000, obs1y))
            screen.blit(obs, (obs2x + 1600, obs2y))
            screen.blit(obs, (obs1x + 2400, obs1y))
            screen.blit(obs, (obs2x + 2000, obs2y))
            screen.blit(obs, (obs1x + 2800, obs1y))
            screen.blit(obs, (obs2x + 2400, obs2y))
            screen.blit(obs, (obs1x + 3200, obs1y))
            screen.blit(obs, (obs2x + 2800, obs2y))
            screen.blit(char, (charx, chary))
            screen.blit(text, (450, 10))
            screen.blit(text2, (350, 10))

            if gameover:
                screen.blit(text1, (300, 200))

            pygame.display.update()
playgame()
