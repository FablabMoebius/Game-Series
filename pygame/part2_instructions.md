# Partie 2 - Rencontre de l'Autre

## Mission 0 : Préparatifs
- [ ] Télécharger le fichier [`game_base.py`](game_base.py) qui servira de base pour les missions suivantes.
- [ ] Ouvrir le fichier dans un éditeur de texte.
- [ ] Exécuter le fichier.


## Mission 1 : S'approprier le héros-rond
- [ ] Contrôler la position du cercle (qui représente votre héros) avec la souris (suivre le curseur).

<details>
<summary>Indices</summary>

- `MOUSEMOTION` est l'événement produit lorsque la souris bouge.
- `mouse.get_pos()` est une fonction qui retourne la position de la souris sous forme d'un tuple (x, y).
</details>

## Mission 2 : Le bouclier (théorique) de l’espace
- [ ] Le joueur active son bouclier en restant appuyé sur la touche espace.
  - [ ] Faire un `print("shield enabled")` lorsque le bouclier est activé.
  - [ ] Faire un `print("shield disabled")` lorsque le bouclier est désactivé.

<details>
<summary>Indices</summary>

- `KEYDOWN` est l'événement produit lorsque l'on appuie sur une touche du clavier.
- `KEYUP` est l'événement produit lorsque l'on relâche une touche du clavier.
- `K_SPACE` est la touche espace.
- Vous pouvez créer une variable qui mémorise l'état d'activation du bouclier.
</details>

## Mission 3 : Un presque vrai bouclier métallique
- [ ] Afficher le héros en gris lorsque le bouclier-armure est activé.


## Mission 4 : Un méchant pas encore méchant
- [ ] Afficher un carré de 50x50 pixels (hello le méchant!) quelque part dans le quart nord-ouest de l’écran.

_Note :_
- Couleur du méchant libre.

<details>
<summary>Indice</summary>

-  `draw.rect(screen, color=(R, G, B), rect=(x, y, width, height))`
</details>

## Mission 5 : LA rencontre (inoffensive)
- [ ] Détecter la collision entre le héros et le méchant en utilisant la méthode [`colliderect`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect).
  - [ ] Faire un `print("battle")` (ou `print("bisous")`, comme vous préférez) lorsque le héros et le méchant sont en contact.

<details>
<summary>Indices</summary>

- Enregistrer la variable de retour des `draw` (pour obtenir un objet `Rect`).
- La méthode [`colliderect`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect) de cet objet permet de détecter la collision entre 2 objets de type `Rect`.
_Exemple: `player_rect.colliderect(ball_rect)` renvoi un booléen (`True` ou `False`)._
</details>

## Mission 6 : ~~Du sang~~ Du rouge sur les mains
- [ ] Changer la couleur du héros en rouge lorsqu'il est en collision.
- [ ] Créer une variable correspondant aux points de vie du héros.
  - [ ] Décrémenter la vie lorsque le héros est en collision.
  - [ ] Quitter le jeu (la boucle) quand le héros n’a plus de vie.

_Note :_
- Toute nuance de rouge est acceptée.
- Ignorer le bouclier pour l'instant.
- La caractéristique de base correspondant à la vitalité de votre héros (nombre de point de vie) est libre, toutefois une valeur supérieure à 50 est conseillée.
- C'est OK de perdre de la vie en continu tant que le héros touche notre ennemi (disons... toxique).
<details>
<summary>Indice</summary>

- Quitter le jeu revient à quitter la boucle principale.
</details>


## Mission 7 : Parce que la meilleure attaque c’est la défense ?
- [ ] Lorsque le bouclier est activé, notre héros ne doit pas perdre de vie (ni de sang) au contact de l'ennemi.

## Mission 8 : La puissance du blit [WIP]

_Préambule_ :

Vous qui suivez ces missions avec ferveur, il faut absolument qu'on vous avoue quelque chose : 

**Utiliser `draw` pour gérer des animations, ce n'est pas top, du tout...**

En effet, `draw` s'occupe a la fois de générer la forme, la remplir d'une couleur, la positionner et enfin de l'"afficher" sur l'écran (pris en compte par le `display.flip()` final).  
Pour découvrir pygame, c'était très pratique, toutefois, pour gérer plus finement et efficacement l'affichage, on va préférer utiliser des `Surface` et des objects `Rect` (que l'on va créer avant de rentrer dans la boucle pricipale)
et choisir de les afficher avec la méthode `blit` dans la boucle.
Ça peut paraître compliqué au premier abord, mais c'est en fait assez simple et très efficace (et ça sera indispensable pour des jeux plus complexes).

En fait on peut ~~comparer~~
- l'objet `Surface` à une peinture
- l'objet `Rect` à un cadre dans lequel on peut mettre une peinture.
- le blit ... à un copier-coller de la peinture dans le cadre. [à revoir]
[à compléter]

Assez discuté, passons à la pratique pour démystifier tout ça !

- [ ] Remplacer les appels à `draw` par la création de `Surface`, de `Rect` et d'appels à `blit`.
    - [ ] En dehors de la boucle, créer plusieurs `Surface` pour le héros (correspondant aux plusieurs couleurs) et une pour l'ennemi.
    - [ ] En dehors de la boucle, créer un `Rect` pour le héros et un autre pour l'ennemi.
    - [ ] Dans la boucle, utiliser `screen.blit(...)` pour afficher les objets.

<details>
<summary>Indices</summary>

Exemple d'utilisation:
```python
# en dehors de la boucle
ball_surface = pygame.Surface((width, height))
ball_surface.fill((R, G, B))
ball_rectangle = ball_surface.get_rect()  # possibilité de spécifier une position center=(x, y))
# dans la boucle
ball_rectangle.center = (x, y) # bouger le "cadre" (possibilité de spécifier top, bottom, left, right)
screen.blit(ball_surface, ball_rectangle) # afficher la "peinture" de la balle dans "cadre" situé à la position (x, y)
```
- Pensez à retirer les appels à fill et draw
- Pensez 
</details>

## Mission 9 : Un ennemi avec des yeux [WIP]
[ ]
indice: move_ip
 
## Mission 10 : Restaurer leurs images [WIP]
[ ]

## Prochaine mission ? [WIP]

