import pygame,os


def get_frog_images():

    up_images,left_images,right_images = [],[],[]
    

    lists = [up_images,left_images,right_images]
    prefixes = ('up','left','right')

    for l,prefix in zip(lists,prefixes):
        still_image = pygame.image.load(os.path.join('assets',f"{prefix}_still.png")).convert_alpha()
        move_image = pygame.image.load(os.path.join('assets',f"{prefix}_move.png")).convert_alpha()
        l.append(still_image)
        l.append(move_image)

    
    down_images = []

    for up_image in up_images:
        down_image = pygame.transform.rotate(up_image,180)
        down_images.append(down_image)

    lists.append(down_images)

    
    return lists



ranges = {(67,103): (86,25),(184,220): (203,30),(303,337): (322,29),(419,453): (436,31),(534,570): (553,28)}

class Frog(pygame.sprite.Sprite):

    

    UP = 0
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    up_images,left_images,right_images,down_images = get_frog_images()


    def __init__(self,screen_width,screen_height,lives=5,speed=2):
    
        super().__init__()
        
        self.image = self.up_images[0]
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = screen_width//2 - self.image.get_width()//2
        self.y = screen_height - self.image.get_height()
        self.rect = self.image.get_rect(topleft=(self.x,self.y))
        self.lives = lives
        self.speed = speed
        self.moving = False
        self.move_index = 0
        self.direction = self.UP
        self.images = self.up_images
        self.on_log = False
        self.x_speed = None #will have x_speed if on log
    
    
    def is_touching_lily_pad(self):
        for (start,end),center in ranges.items():
            if self.rect.left >= start and self.rect.right <= end:
                return True,center

        return False,None
    def place_on_log(self,log):
        self.on_log=True
        self.x_speed = log.speed * log.direction
    
    def reset(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.direction = self.UP
        self.images = self.up_images
        self.image = self.up_images[0]
        self.rect = self.image.get_rect(center=self.rect.center)
        self.on_log = False
        self.x_speed = None
    

    @property
    def in_water(self):
        
        top,bottom = 45,297
        return self.rect.bottom <= bottom and self.rect.top >= top

    
    @property
    def at_top(self):
        top = 43
        

        




        return self.rect.top <= top





    def update(self,keys_pressed):

        
        if self.on_log:
            self.rect.x += self.x_speed

        moving = False
        if keys_pressed[pygame.K_UP]:
            self.move_up(self.moving)
            moving = True
        elif keys_pressed[pygame.K_LEFT]:
            self.move_left(self.moving)
            moving = True
        elif keys_pressed[pygame.K_RIGHT]:
            self.move_right(self.moving)
            moving = True
        elif keys_pressed[pygame.K_DOWN]:
            self.move_down(self.moving)
            moving = True
        else:
            if self.moving:
                self.moving = False
                self.move_index = 0
                self.image = self.images[0]
        if moving:
            if not self.moving:
                self.start_moving_frame = 0
                self.moving = True

            self.start_moving_frame += 1
            if self.start_moving_frame == 5:
                self.start_moving_frame = 0
                self.move_index = (self.move_index + 1) % len(self.images)
                self.image = self.images[self.move_index]




    def move_left(self,moving):
        
        if self.direction != self.LEFT:
            self.image = self.left_images[1]
            self.rect = self.image.get_rect(center=self.rect.center)
            self.move_index = 1
            self.images = self.left_images
            self.direction = self.LEFT
        
        if not moving:
            self.image = self.images[1]
            self.rect = self.image.get_rect(center=self.rect.center)

        self.rect.x -= self.speed
        if self.rect.left <= 0:
            self.rect.left = 0

    def move_up(self,moving):

        if self.direction != self.UP:
            self.image = self.up_images[1]
            self.rect = self.image.get_rect(center=self.rect.center)
            self.move_index = 1
            self.images = self.up_images
            self.direction = self.UP

        if not moving:
            self.image = self.images[1]
            self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.y -= self.speed
        if self.rect.top <= 0:
            self.rect.top = 0


    def move_right(self,moving):
        
        if self.direction != self.RIGHT:
            self.image = self.right_images[1]
            self.rect = self.image.get_rect(center=self.rect.center)
            self.move_index = 1
            self.images = self.right_images
            self.direction = self.RIGHT

        if not moving:
            self.image = self.images[1]
            self.rect = self.image.get_rect(center=self.rect.center)

        self.rect.x += self.speed
        if self.rect.right >= self.screen_width:
            self.rect.right = self.screen_width


    def move_down(self,moving):
        
        if self.direction != self.DOWN:
            self.image = self.down_images[1]
            self.rect = self.image.get_rect(center=self.rect.center)
            self.move_index = 1
            self.images = self.down_images
            self.direction = self.DOWN

        if not moving:
            self.image = self.images[1]
            self.rect = self.image.get_rect(center=self.rect.center)

        self.rect.y += self.speed

        if self.rect.bottom >= self.screen_height:
            self.rect.bottom = self.screen_height 












