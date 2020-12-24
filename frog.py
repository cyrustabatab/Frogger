import pygame,os


def get_frog_images():

    images = []
    
    still_image = pygame.image.load(os.path.join('assets',"up_still.png")).convert_alpha()
    move_image = pygame.image.load(os.path.join('assets',"up_move.png")).convert_alpha()

    images = [still_image,move_image]

    return images




class Frog(pygame.sprite.Sprite):


    up_images = get_frog_images()


    def __init__(self,screen_width,screen_height,speed=2):
    
        super().__init__()
        
        self.image = self.up_images[0]
        self.x = screen_width//2 - self.image.get_width()//2
        self.y = screen_height - self.image.get_height()
        self.rect = self.image.get_rect(topleft=(self.x,self.y))
        self.speed = speed
        self.moving = False
        self.move_index = 0



    def update(self,keys_pressed):


        if keys_pressed[pygame.K_UP]:
            self.rect.y -= self.speed
            if not self.moving:
                self.start_moving_frame = 0
                self.moving = True
            self.start_moving_frame += 1
            if self.start_moving_frame == 10:
                self.start_moving_frame = 0
                self.move_index = (self.move_index + 1) % len(self.up_images)
                self.image = self.up_images[self.move_index]
        else:
            if self.moving:
                self.moving = False
                self.move_index = 0

            self.image = self.up_images[0]



    











