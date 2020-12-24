import pygame,sys,os

pygame.init()



screen_width = screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

from frog import Frog


pygame.display.set_caption("FROGGER")

background = pygame.image.load(os.path.join('assets','background.png'))

frogger = pygame.sprite.GroupSingle(Frog(screen_width,screen_height))

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    keys_pressed = pygame.key.get_pressed()
    frogger.update(keys_pressed)
    screen.blit(background,(0,0))
    frogger.draw(screen)

    pygame.display.update()





