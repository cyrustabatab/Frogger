import pygame,os





class Car(pygame.sprite.Sprite):


    def __init__(self,x,y,speed=2):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(os.path.join('assets','left_car1.png'))
        self.rect = self.image.get_rect(topleft=(self.x,self.y))
        self.speed = speed

    

    def update(self):


        self.rect.x -= self.speed








