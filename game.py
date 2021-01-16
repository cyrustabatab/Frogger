import pygame,sys,os,random,time


pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()



screen_width = screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
FPS = 60

from frog import Frog
from car import Car
from info import Info
from log import Log
from log import Gator


pygame.display.set_caption("FROGGER")

background = pygame.image.load(os.path.join('assets','background.png'))

frogger = pygame.sprite.GroupSingle(Frog(screen_width,screen_height))

cars = pygame.sprite.Group()


y_positions = [350 + 50 * y for y in range(0,5)]
#car = Car(screen_width)
#cars.add(car)

ADD_CAR = pygame.USEREVENT + 1
CROAK =pygame.USEREVENT + 2
TRILL = pygame.USEREVENT + 3

#pygame.time.set_timer(ADD_CAR,1000)
pygame.time.set_timer(TRILL,5000)
pygame.time.set_timer(CROAK,3000)

possible_gaps = (2.5,3,3.5,4)
log_gaps =(1,2,3) #(4,5,6)
lane_times = [[time.time(),0] for _ in range(10)]
info = Info(screen_width,screen_height)

croak_sound = pygame.mixer.Sound(os.path.join('assets','croak.wav'))
splat_sound = pygame.mixer.Sound(os.path.join('assets','splat.wav'))
trill_sound = pygame.mixer.Sound(os.path.join('assets','trill.wav'))

frog_image= pygame.image.load(os.path.join('assets','down_still.png'))


logs = pygame.sprite.Group()




def game_over_screen():
    game_over_image = pygame.image.load(os.path.join('assets','game_over.jpg')).convert()



    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return




        

        screen.blit(game_over_image,(0,0))

        pygame.display.update()



def reset():
    splat_sound.play()
    info.decrement_life()
    frogger.sprite.reset()
    frogger.sprite.lives -= 1
    if frogger.sprite.lives == 0:
        game_over_screen()
        pygame.time.set_timer(CROAK,0)
        frogger.sprite.lives = 5
        info.reset()


score = 0
locations = []
while True:
    
    
    current_time = time.time()


    for i,(lane_time,gap) in enumerate(lane_times):

        if current_time - lane_time >= gap:
            if i >= 5:
                cars.add(Car(i + 1 - 5,screen_width))
                lane_times[i][1] = random.choice(possible_gaps)
            else:
                if random.randint(1,5) <= 4:
                    logs.add(Log(i +1,screen_width))
                else:
                    logs.add(Gator(i + 1,screen_width))
                lane_times[i][1] = random.choice(log_gaps)

            lane_times[i][0] = current_time









    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            print(x,y)
            #print(frogger.sprite.in_water)



        if event.type == CROAK:
            croak_sound.play()


        if event.type == TRILL:
            trill_sound.play()
        #if event.type == ADD_CAR:
        #    car = Car(screen_width)
        #    cars.add(car)


    keys_pressed = pygame.key.get_pressed()
    frogger.update(keys_pressed)
    cars.update()
    logs.update()
    
    if not frogger.sprite.in_water and pygame.sprite.spritecollideany(frogger.sprite,cars,collided=pygame.sprite.collide_mask):
        splat_sound.play()
        info.decrement_life()
        frogger.sprite.reset()
        frogger.sprite.lives -= 1
        if frogger.sprite.lives == 0:
            game_over_screen()
            pygame.time.set_timer(CROAK,0)
            frogger.sprite.lives = 5
            info.reset()
    elif not frogger.sprite.at_top and frogger.sprite.in_water:
        sprites = pygame.sprite.spritecollide(frogger.sprite,logs,collided=pygame.sprite.collide_mask,dokill=False)

        
        if sprites:
            sprite = sprites[0]

            if isinstance(sprite,Log):
                frogger.sprite.place_on_log(sprite)
            else:
                reset()


        else:
            info.decrement_life()
            frogger.sprite.reset()
            frogger.sprite.lives -= 1
    elif frogger.sprite.at_top:
        frogger_win,location = frogger.sprite.is_touching_lily_pad()

        if frogger_win:
            locations.append(location)
            print('win')
            score += 1
            print(score)
        else:
            print('lose')
            info.decrement_life()
            frogger.sprite.lives -= 1


        frogger.sprite.reset()
    else:
        frogger.sprite.on_log = False









    screen.blit(background,(0,0))
    cars.draw(screen)
    logs.draw(screen)
    frogger.draw(screen)
    info.draw_lives(screen)
    for x,y in locations:
        screen.blit(frog_image,(x,y))

    pygame.display.update()
    clock.tick(FPS)





