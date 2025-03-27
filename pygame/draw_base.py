import pygame

WHITE = (0, 0, 0)  # Blanc (RGB)
RED = (255, 0, 0)  # Rouge Pur (RGB)
YELLOW = (239, 216, 91) # Jaune pastel (RGB)

pygame.init()
clock = pygame.time.Clock()  # Pour pouvoir contrôler la vitesse de rafraîchissement
screen = pygame.display.set_mode((800, 600))  # Fenêtre graphique de 800x600 pixels

screen.fill(WHITE)  # Remplit l'écran en blanc
pygame.draw.circle(screen, color=YELLOW, center=(100, 200), radius=25)  # Dessine un cercle jaune
pygame.display.flip()  # Applique les changements graphiques effectués sur l'écran

while True:
    clock.tick(10)  # 10 FPS (10 itérations par seconde)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

