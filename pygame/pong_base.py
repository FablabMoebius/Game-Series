import pygame

# ----- initialisation générale
pygame.init()
screen = pygame.display.set_mode((800, 600))  # fenêtre graphique de 800x600 pixels
clock = pygame.time.Clock()  # pour contrôler la vitesse de rafraîchissement

# ----- initialisation des éléments du jeu (création de surfaces, etc.)

# ----- boucle principale
going = True
while going:

    clock.tick(60)  # 60 FPS

    # ----- gestion des événements (souris, clavier, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False

    screen.fill((0, 0, 0))

    # ----- applique tous les changements effectués à l'écran
    pygame.display.flip()

pygame.quit()
