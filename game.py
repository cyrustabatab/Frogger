import pygame,sys,os,random

pygame.init()



screen_width = screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
FPS = 60

from frog import Frog
from car import Car


pygame.display.set_caption("FROGGER")

background = pygame.image.load(os.path.join('assets','background.png'))

frogger = pygame.sprite.GroupSingle(Frog(screen_width,screen_height))

cars = pygame.sprite.Group()


y_positions = [355 + 50 * y for y in range(0,5)]
car = Car(screen_width +20,random.choice(y_positions))
cars.add(car)
while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    keys_pressed = pygame.key.get_pressed()
    frogger.update(keys_pressed)
    cars.update()
    screen.blit(background,(0,0))
    cars.draw(screen)
    frogger.draw(screen)

    pygame.display.update()
    clock.tick(FPS)





