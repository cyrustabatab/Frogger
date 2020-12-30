import pygame,sys,os,random,time

pygame.init()



screen_width = screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
FPS = 60

from frog import Frog
from car import Car
from info import Info


pygame.display.set_caption("FROGGER")

background = pygame.image.load(os.path.join('assets','background.png'))

frogger = pygame.sprite.GroupSingle(Frog(screen_width,screen_height))

cars = pygame.sprite.Group()


y_positions = [350 + 50 * y for y in range(0,5)]
#car = Car(screen_width)
#cars.add(car)

ADD_CAR = pygame.USEREVENT + 1

#pygame.time.set_timer(ADD_CAR,1000)

possible_gaps = (2,2.5,3,3.5,4)
lane_times = [[time.time(),0] for _ in range(5)]
info = Info(screen_width,screen_height)




def game_over_screen():
    game_over_image = pygame.image.load(os.path.join('assets','game_over.jpg')).convert()



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        

        screen.blit(game_over_image,(0,0))

        pygame.display.update()




while True:
    
    
    current_time = time.time()


    for i,(lane_time,gap) in enumerate(lane_times):

        if current_time - lane_time >= gap:
            cars.add(Car(i + 1,screen_width))
            lane_times[i][0] = current_time
            lane_times[i][1] = random.choice(possible_gaps)









    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()

            print(x,y)
        #if event.type == ADD_CAR:
        #    car = Car(screen_width)
        #    cars.add(car)


    keys_pressed = pygame.key.get_pressed()
    frogger.update(keys_pressed)
    cars.update()
    if pygame.sprite.spritecollideany(frogger.sprite,cars,collided=pygame.sprite.collide_mask):
        info.decrement_life()
        frogger.sprite.reset()
        frogger.sprite.lives -= 1
        if frogger.sprite.lives == 0:
            game_over_screen()
    screen.blit(background,(0,0))
    frogger.draw(screen)
    cars.draw(screen)
    info.draw_lives(screen)

    pygame.display.update()
    clock.tick(FPS)





