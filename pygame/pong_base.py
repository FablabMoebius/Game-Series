import pygame

# Initialisation générale
pygame.init()
screen = pygame.display.set_mode((800, 600))  # fenêtre graphique de 800x600 pixels
clock = pygame.time.Clock()  # pour contrôler la vitesse de rafraîchissement

# Initialisation des éléments du jeu (création de surfaces, etc.)

# Boucle principale
going = True
while going:

    clock.tick(60)  # 60 FPS

    # Gestion des événements (souris, clavier, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False

    # Opérations à effectuer à chaque frame
    screen.fill(color="black")

    # Application des changements effectués à l'écran
    pygame.display.flip()

pygame.quit()
