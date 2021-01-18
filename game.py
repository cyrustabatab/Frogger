import pygame,sys,os,random,time


pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()



screen_width = screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms",42)
FPS = 60
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

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
log_gaps =(2,3,4) #(4,5,6)
lane_times = [[time.time(),0] for _ in range(10)]
amount_to_win = 5
info = Info(screen_width,screen_height)

croak_sound = pygame.mixer.Sound(os.path.join('assets','croak.wav'))
splat_sound = pygame.mixer.Sound(os.path.join('assets','splat.wav'))
trill_sound = pygame.mixer.Sound(os.path.join('assets','trill.wav'))
splash_sound = pygame.mixer.Sound(os.path.join('assets','plunk.wav'))

frog_image= pygame.image.load(os.path.join('assets','down_still.png'))


logs = pygame.sprite.Group()



def game_over_screen():
    game_over_image = pygame.image.load(os.path.join('assets','gameover2.png')).convert()
    game_over_image = pygame.transform.scale(game_over_image,(screen_width,screen_height))

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



def reset(lose=True,splat=True):

    if lose:
        if splat:
            splat_sound.play()
        else:
            splash_sound.play()
        info.decrement_life()
        frogger.sprite.lives -= 1
        if frogger.sprite.lives == 0:
            game_over_screen()
            pygame.time.set_timer(CROAK,0)
            frogger.sprite.lives = 5
            info.reset()
    frogger.sprite.reset()





def main():
    score = 0
    score_right_gap = 5
    score_top_gap = 0
    score_text =font.render(str(score),True,BLACK)
    locations = []
    win_text = None
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

            if frogger.sprite.out_of_bounds:
                reset()

            sprites = pygame.sprite.spritecollide(frogger.sprite,logs,collided=pygame.sprite.collide_mask,dokill=False)

            
            


            
            if sprites:
                sprite = sprites[0]

                if isinstance(sprite,Log):
                    frogger.sprite.place_on_log(sprite)
                else:
                    reset()


            else:
                reset(splat=False)
        elif frogger.sprite.at_top:
            frogger_win,location = frogger.sprite.is_touching_lily_pad()

            if frogger_win:
                locations.append(frog_image.get_rect(center=location))
                print('win')
                score += 1
                score_text = font.render(str(score),True,BLACK)
                if score == amount_to_win:
                    win_text = font.render("YOU WIN!",True,BLACK)


                print(score)
                reset(lose=False)
            else:
                print('lose')
                info.decrement_life()
                frogger.sprite.lives -= 1
                reset()
            

        else:
            frogger.sprite.on_log = False



        screen.blit(background,(0,0))
        cars.draw(screen)
        logs.draw(screen)
        frogger.draw(screen)
        info.draw_lives(screen)
        for frog_rect in locations:
            #frog_image_rect = frog_image.get_rect(center=(x,y))
            screen.blit(frog_image,frog_rect)
        screen.blit(score_text,(screen_width - score_right_gap - score_text.get_width(),score_top_gap - 10))
        if win_text:
            screen.blit(win_text,(screen_width//2 - win_text.get_width()//2,screen_height//2 - win_text.get_height()//2))
        pygame.display.update()
        clock.tick(FPS)

def menu():
    
    top_gap = 40
    bottom_gap = 50
    pygame.mixer.music.load(os.path.join('assets','frogger-music.mp3'))
    pygame.mixer.music.play()
    background_image = pygame.image.load(os.path.join('assets','frogger3.jpg'))
    background_image = pygame.transform.scale(background_image,(screen_width,screen_height))
    title_font = pygame.font.SysFont("comicsansms",80)
    sub_font = pygame.font.SysFont("comicsansms",40)
    title_text = title_font.render("FROGGER",True,BLACK)
    sub_text = sub_font.render("Press ENTER to play!",True,BLACK)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    main()

        


        screen.blit(background_image,(0,0))
        screen.blit(title_text,(screen_width//2 - title_text.get_width()//2,top_gap))
        screen.blit(sub_text,(screen_width//2 - sub_text.get_width()//2,screen_height - 50 - sub_text.get_height()))

        pygame.display.update()



if __name__ == "__main__":
    menu()


