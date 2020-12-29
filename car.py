import pygame,os,random


def get_images():

    left_image_paths = [os.path.join('assets',path) for path in ('left_car1.png','left_car2.png')]
    
    right_image_paths = [os.path.join('assets',path) for path in ('right_car1.png','right_car2.png')]
    
    modern_cars = [pygame.image.load(os.path.join('assets',f'car{i}.png')).convert_alpha() for i in range(1,7)]
    
    left_images,right_images = [],[]


    for image_path in left_image_paths:
        left_image = pygame.image.load(image_path).convert_alpha()
        left_image = pygame.transform.scale(left_image,(left_image.get_width() + 10,40))
        left_images.append(left_image)
        right_image = pygame.transform.rotate(left_image,180)
        right_images.append(right_image)
    
    for image_path in right_image_paths:
        right_image = pygame.image.load(image_path).convert_alpha()
        right_image = pygame.transform.scale(right_image,(right_image.get_width() + 10,40))
        right_images.append(right_image)
        left_image = pygame.transform.rotate(right_image,180)
        left_images.append(left_image)
    
    for i,modern_car in enumerate(modern_cars):
        modern_cars[i] = pygame.transform.scale(modern_car,(modern_car.get_width() - 20,50))


    right_images.extend(modern_cars)
    return left_images,right_images





TOP_Y = 345
LEFT = 1
RIGHT = 2

direction_mapping = {1: LEFT, 2: RIGHT,3: LEFT,4: RIGHT,5: LEFT}

class Car(pygame.sprite.Sprite):

    y_positions = [TOP_Y + 50 * y for y in range(0,5)]
    left_y_indexes = [0,2,4]
    right_y_indexes = [1,3]

    left_images,right_images = get_images()

    def __init__(self,lane,screen_width,speed=2):
        super().__init__()

        self.direction = direction_mapping[lane]


        


        if self.direction == LEFT:
            self.y = self.y_positions[lane -1]
            self.image = random.choice(self.left_images)
            self.x = screen_width + 20
        else:
            self.y = self.y_positions[lane - 1]
            self.image = random.choice(self.right_images)
            self.x = -20 - self.image.get_width()

        self.rect = self.image.get_rect(topleft=(self.x,self.y))
        self.speed = speed

    def update(self):
        
        if self.direction == LEFT:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed






