import pygame


pygame.init()
win = pygame.display.set_mode((600, 550))

pygame.display.set_caption("aboba")

walk = [pygame.image.load("image/Walk/walkcolor0001.png"),
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
]

player = pygame.image.load('image/noshadow.png')

phon = pygame.image.load('o.jpg')

clock = pygame.time.Clock()

x = 50
y = 425
widht = 60
height = 60
speed = 5

s = False
st = 10

left = False
right = False
anim = 0
last = "right"

class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draww(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def wer(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

walkRight = [
    pygame.transform.flip(walk[0], True, False),
    pygame.transform.flip(walk[1], True, False),
    pygame.transform.flip(walk[2], True, False),
    pygame.transform.flip(walk[3], True, False),
    pygame.transform.flip(walk[4], True, False),
    pygame.transform.flip(walk[5], True, False),
    pygame.transform.flip(walk[6], True, False),
    pygame.transform.flip(walk[7], True, False),
    pygame.transform.flip(walk[9], True, False),
    pygame.transform.flip(walk[10], True, False),
    pygame.transform.flip(walk[11], True, False),
]

def draw123():
    global anim
    win.blit(phon, (0, 0))

    if anim + 1 >= 30:
        anim = 0

    if left:
        win.blit(walkRight[anim // 5], (x, y))
        anim += 1
    elif right:
        win.blit(walk[anim // 5], (x, y))
        anim += 1
    else:
        win.blit(player, (x, y))

    for bullet in bullets:
        bullet.wer(win)

    pygame.display.update()

pygame.mixer.music.load('wee.mp3')
pygame.mixer.music.play(-1)

run = True

bullet = []
bullets = []
while run:
    clock.tick(30)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    draw123()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if last == "right":
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(snaryad(round(x + widht // 2), round(y + height // 2), 5, (255, 0, 0), facing))

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        last = "left"
    elif keys[pygame.K_RIGHT] and x < 500 - widht -5:
        x += speed
        left = False
        right = True
        last = "right"
    else:
        left = False
        right = False
        anim = 0
    if not(s):
        if keys[pygame.K_DOWN] and y < 500 - height - 5:
            y += speed
        if keys[pygame.K_SPACE]:
            s = True
    else:
        if st >= -10:
            if st < 0:
                y += (st ** 2) / 2
            else:
                y -= (st ** 2) / 2
            st -= 1
        else:
            s = False
            st = 10

pygame.quit()