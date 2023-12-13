import pygame

# ----- initialisation générale
pygame.init()
screen = pygame.display.set_mode((800, 600))  # fenêtre graphique de 800x600 pixels
clock = pygame.time.Clock()  # pour contrôler la vitesse de rafrachissement

# ----- initialisation des éléments du jeu (création de surfaces, chargement d'images, etc.)

# ----- boucle principale
going = True
while going:

    clock.tick(40)  # 40 FPS

    # ----- gestion des événements (souris, clavier, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            going = False

    screen.fill((77, 111, 66))
    pygame.draw.circle(screen, color=(255, 192, 203), center=(400, 300), radius=25)

    # ----- applique tous les changements effectués à l'écran
    pygame.display.flip()

pygame.quit()
