import pygame

RED = (255, 0, 0)  # rouge (RGB)
BLUE = (0, 0, 255)  # bleu (RGB)

pygame.init()
clock = pygame.time.Clock()  # pour pouvoir contrôler la vitesse de rafrachissement
screen = pygame.display.set_mode((800, 600))  # fenêtre graphique de 800x600 pixels

screen.fill(BLUE)  # remplir l'écran en bleu
pygame.draw.circle(screen, RED, center=(100, 200), radius=25)  # dessine un cercle rouge
pygame.display.flip()  # applique les changements graphiques effectués sur l'écran

while True:
    clock.tick(10)  # 10 FPS (10 itérations par seconde)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

