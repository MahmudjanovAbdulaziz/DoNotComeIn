import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
TILE = 32

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Tank:
    def __init__(self, color, px, py, direct, keyList):
        objects.append(self)
        self.type = 'tank'

        self.color = color
        self.rect = pygame.Rect(px, py, TILE, TILE)
        self.direct = direct
        self.moveSpeed = 2

        self.keyLEFT = keyList[0]
        self.keyRIGHT = keyList[1]
        self.keyUP = keyList[2]
        self.keyDOWN = keyList[3]
        self.keySHOT = keyList[4]

    def update(self):
        if keys[self.keyLEFT]:
            self.rect.x -= self.moveSpeed
        elif keys[self.keyRIGHT]:
            self.rect.x += self.moveSpeed
        elif keys[self.keyUP]:
            self.rect.y -= self.moveSpeed
        elif keys[self.keyDOWN]:
            self.rect.y += self.moveSpeed

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)

objects = []
Tank('blue', 100, 275, 0, (pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_SPACE))


play = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()
    for obj in objects: obj.update()

    window.fill('black')
    for obj in objects: obj.draw()

    pygame.display.update()
    clock.tick(FPS)

    pygame.quit()