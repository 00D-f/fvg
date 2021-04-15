import pygame

sc = pygame.display.set_mode((600, 400))

player1X = 100
player1Y = 100

playerImage = pygame.image.load("image/idle.png")
playerImage = pygame.transform.scale(playerImage, (60, 60))

game = True
while game:

    for i in pygame.event.get():
        print(i)
        if i.type == pygame.TEXTINPUT:
            if i.text == "s":
                player1Y += 1
            if i.text == "w":
                player1Y -= 1
            if i.text == "a":
                player1X -= 1
            if i.text == "d":
                player1X += 1


        if i.type == pygame.QUIT:
            game = False


    sc.fill((255,255,255))

    #Игрок
    sc.blit(playerImage, (0, 0))

    pygame.display.update()

    pygame.time.delay(30)
