import pygame

RED = (255, 0, 0)  # Rouge (RGB)
BLUE = (0, 0, 255)  # Bleu (RGB)

pygame.init()
clock = pygame.time.Clock()  # Pour pouvoir contrôler la vitesse de rafrachissement
screen = pygame.display.set_mode((800, 600))  # Fenêtre graphique de 800x600 pixels

screen.fill(BLUE)  # Remplit l'écran en bleu
pygame.draw.circle(screen, RED, center=(100, 200), radius=25)  # Dessine un cercle rouge
pygame.display.flip()  # Applique les changements graphiques effectués sur l'écran

while True:
    clock.tick(10)  # 10 FPS (10 itérations par seconde)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

