import pygame
import sys

sc = pygame.display.set_mode((600, 400))

animateIndex = 0

animateWalk = (
    pygame.image.load("image/Walk/walkcolor0001.png"),
    pygame.image.load("image/Walk/walkcolor0002.png"),
    pygame.image.load("image/Walk/walkcolor0003.png"),
    pygame.image.load("image/Walk/walkcolor0004.png"),
    pygame.image.load("image/Walk/walkcolor0005.png"),
    pygame.image.load("image/Walk/walkcolor0006.png"),
    pygame.image.load("image/Walk/walkcolor0007.png"),
    pygame.image.load("image/Walk/walkcolor0008.png"),
    pygame.image.load("image/Walk/walkcolor0009.png"),
    pygame.image.load("image/Walk/walkcolor0010.png"),
    pygame.image.load("image/Walk/walkcolor0011.png"),
    pygame.image.load("image/Walk/walkcolor0012.png")
)

w_press = False
s_press = False
a_press = False
d_press = False

x = 0
y = 0

while True:
    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_w:
                w_press = False
            if i.key == pygame.K_s:
                s_press = False
            if i.key == pygame.K_a:
                a_press = False
            if i.key == pygame.K_d:
                d_press = False

        if i.type == pygame.KEYUP:
            if i.key == pygame.K_w:
                w_press = True
            if i.key == pygame.K_s:
                s_press = True
            if i.key == pygame.K_a:
                a_press = True
            if i.key == pygame.K_d:
                d_press = True

        if i.type == pygame.QUIT:
            sys.exit()

    if w_press:
        y -= 1
    if s_press:
        y += 1

    if a_press:
        x -= 1
    if d_press:
        x += 1

    sc.fill((255, 255, 255))

    sc.blit(animateWalk[animateIndex], (x, y))

    animateIndex += 1
    if animateIndex == 12:
        animateIndex = 0

    pygame.display.update()
    pygame.time.delay(30)
