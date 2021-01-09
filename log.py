import pygame,random,os


# later make it more generic by passing in directory name
def get_log_images():

    images = []
    for image in ('small_log.png','medium_log.png','long_log.png'):
        image = pygame.image.load(os.path.join('assets',image)).convert_alpha()
        image = pygame.transform.scale(image,(image.get_width(),image.get_height() + 20))
        images.append(image)

    
    return images

def get_gator_images():
    left_images = []

    for image in ('close_gator.png','open_gator.png'):
        image = pygame.image.load(os.path.join('assets',image)).convert_alpha()
        image = pygame.transform.scale(image,(image.get_width(),image.get_height() + 20))
        left_images.append(image)
    right_images = []
    for image in left_images:
        image = pygame.transform.flip(image,True,False)
        right_images.append(image)


    return left_images,right_images

LEFT = -1
RIGHT = 1


y_positions = [55 + i * 50 for i in range(5)]
directions = {}


for i in range(1,6):
    if i % 2 == 1:
        directions[i] = RIGHT
    else:
        directions[i] = LEFT



class WaterObject(pygame.sprite.Sprite):


    def __init__(self,lane,screen_width,images,speed=2):
        super().__init__()
        self.screen_width = screen_width
        self.speed = speed
        self.images = images
        self.direction = directions[lane]
        
        self.image = self.images[0]
        if self.direction == RIGHT:
            self.x = -10 - self.image.get_width()
        else:
            self.x = screen_width + 10

        self.y = y_positions[lane -1]



    def update(self):

        self.rect.x += self.direction * self.speed



class Gator(WaterObject):
    
    gator_left_images,gator_right_images = get_gator_images()
    
    def __init__(self,lane,screen_width,speed=2):
        super().__init__(lane,screen_width,self.gator_left_images,speed)
        
        if self.direction == LEFT:
            self.images = self.gator_right_images
        self.image = self.images[0]

        self.rect = self.image.get_rect(topleft=(self.x,self.y))





class Log(pygame.sprite.Sprite):
    
    

    log_images = get_log_images()
    def __init__(self,lane,screen_width,speed=2):
        super().__init__()
        self.screen_width = screen_width

        self.image = random.choice(self.log_images)
        self.speed = speed

        self.direction = directions[lane]

        if self.direction == RIGHT:
            self.x = -10 - self.image.get_width()
        else:
            self.x = screen_width + 10

        self.y = y_positions[lane -1]


        self.rect = self.image.get_rect(topleft=(self.x,self.y))


    def update(self):

        self.rect.x += self.direction * self.speed














