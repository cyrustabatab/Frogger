import pygame,sys,os

pygame.init()

screen_width = screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("FROGGER")

background = pygame.image.load(os.path.join('assets','background.png'))


while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    
    screen.blit(background,(0,0))
    pygame.display.update()





