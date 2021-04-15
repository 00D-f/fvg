import pygame
import socket
import pickle

name = input("имя")


soc = socket.socket()

soc.connect(("192.168.71.240", 5000))

sc = pygame.display.set_mode((600, 400))

image = pygame.image.load("h/ghostbob0002.png")

data = {
    "name": name,
    "speed": 2,
    "x": 0,
    "y": 0
}

pygame.font.init()
f1 = pygame.font.Font(None, 16)

game = True
while game:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False

    soc.send(pickle.dumps(data))
    answer = soc.recv(2048)
    obj = pickle.loads(answer)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        data["y"] -= data["speed"]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        data["y"] += data["speed"]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        data["x"] -= data["speed"]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        data["x"] += data["speed"]

    sc.fill((255, 255, 255))




    sc.blit(image, (data["x"], data["y"]))

    for player in obj:
        if "name" in obj[player]:
            n = f1.render(obj[player]["name"],True, (0, 0, 0))
            sc.blit(n, (obj[player]["x"], obj[player]["y"]- 20))
            sc.blit(image, (obj[player]["x"], obj[player]["y"] ))



    pygame.display.update()
