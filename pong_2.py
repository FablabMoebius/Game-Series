import pygame
from pygame.locals import *

pygame.init()  # initialize pygame
screen = pygame.display.set_mode((800, 600))  # create the screen object
clock = pygame.time.Clock()


class Bar(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.surface = pygame.Surface((25, 50))
        self.surface.fill((0, 0, 0))
        self.rect = self.surface.get_rect(center=position)

    def update(self, y_position):
        self.rect.top = max(0, y_position - self.rect.width)


class Ball(pygame.sprite.Sprite):

    def bounce(self, horizontal=False):
        if horizontal:
            self.direction = (self.direction[0], -self.direction[1])
        else:
            self.direction = (-self.direction[0], self.direction[1])

    def update(self):
        self.rect.move_ip(self.speed * self.direction[0], self.speed * self.direction[1])
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.bounce(horizontal=True)

    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((25, 25))
        self.surface.fill((0, 0, 0))
        self.rect = self.surface.get_rect(center=(400, 300))
        self.speed = 5
        self.direction = (1, 1)


player_bar = Bar((50, 300))
computer_bar = Bar((750, 300))
ball = Ball()

all_sprites = pygame.sprite.Group(player_bar, computer_bar, ball)
vertical_bars = pygame.sprite.Group(player_bar, computer_bar)

# Main loop
running = True
while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEMOTION:
            player_bar.update(pygame.mouse.get_pos()[1])

    ball.update()
    if pygame.sprite.spritecollideany(ball, vertical_bars):
        ball.bounce(horizontal=False)
    computer_bar.update(ball.rect.center[1])

    screen.fill((255, 255, 255))
    for entity in all_sprites:
        screen.blit(entity.surface, entity.rect)
    pygame.display.flip()

pygame.quit()
