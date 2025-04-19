import pygame

# Initialisation générale
pygame.init()
screen = pygame.display.set_mode((800, 600))  # fenêtre graphique de 800x600 pixels
clock = pygame.time.Clock()  # pour contrôler la vitesse de rafraîchissement

# Initialisation des éléments du jeu (création de surfaces, chargement d'images, etc.)
player_color = "pink"
player_position = (400, 300)  # coordonnées du joueur

# Boucle principale
going = True
while going:

    clock.tick(40)  # 40 FPS

    # Gestion des événements (souris, clavier, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            going = False

    screen.fill(color="dark green")
    pygame.draw.circle(screen, color=player_color, center=player_position, radius=25)

    # Applique tous les changements effectués à l'écran
    pygame.display.flip()
