import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,speed,height):
        super().__init__()
        self.image = pygame.Surface((4,20))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed
        self.heigth_y_constraint = height

    def update(self):
        self.rect.y += self.speed
        self.destroy()

    def destroy(self):

        if self.rect.y <= -50 or self.rect.y >= self.heigth_y_constraint + 50:
            self.kill()
