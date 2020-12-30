import pygame,os



lives_image_name = 'life.png'

class Info:
    

    lives_image = pygame.image.load(os.path.join('assets',lives_image_name))

    def __init__(self,screen_width,screen_height,lives=5):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.lives = lives
        left_gap = 5
        gap_between_images = 5
        self.lives_x_coordinates = [left_gap + (self.lives_image.get_width() + gap_between_images) * i for i in range(lives)]
        self.lives_y_coordinate = 2



    

    def draw_lives(self,screen):

        y = self.lives_y_coordinate
        for x in self.lives_x_coordinates[:self.lives]:
            screen.blit(self.lives_image,(x,y))


    

    def decrement_life(self):
        self.lives -= 1 








