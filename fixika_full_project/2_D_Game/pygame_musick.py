import pygame as p
while True:
    p.mixer.init()
    p.mixer.music.load("Jah Khalib - Доча.mp3")
    p.mixer.music.play()
    a = input('Напишите 1 если хотить на паузу'
              '\nНапишите 2 если хотить уменьшить звук '
              '\nНапишите 3 если хотить выйти из паузы '
              '\nНапишите 4 если хотите перезапустить музыку\n')
    if a == 1:
        p.mixer.music.pause()
    elif a == 2:
        p.mixer.music.set_volume(0.5)
    elif a == 3:
        p.mixer.music.unpause()
    elif a == 4:
        p.mixer.music.stop()
        p.mixer.music.play()
    elif a == 5:
        p.mixer.music.fadeout(1)


