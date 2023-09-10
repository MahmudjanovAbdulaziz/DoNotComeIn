import pygame

pygame.init()
win=pygame.display.set_mode((500, 500))

pygame.display.set_caption('Cubes Game')



x=50
y=50
width=40
height=60
speed=5



run =True
while True:
    pygame.time.delay(100)

    pygame.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed

    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.display.update()
    pygame.quit()