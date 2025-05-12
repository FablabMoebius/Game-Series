# Partie 3 - Le Pong

![pong_illustration](https://github.com/FablabMoebius/Game-Series/assets/14202917/892fb9f3-782e-4e7e-85c3-26d88e74e5a7)

## Mission 0 : Matériel
- [ ] Télécharger le fichier [`pong_base.py`](pong_base.py) qui servira de base pour les missions suivantes.

## Mission 1 : Faire preuve d’imagination
- [ ] À quoi ressemble le jeu Pong ?
- [ ] De quoi se compose t-il ?
- [ ] Quelles sont les règles basiques du jeu ?

_Note :_
- Il n’y a pas de mauvaise réponse à cette question. Vous pouvez créer une variante qui vous plait et qui vous sera unique.

<details>
<summary>Indices</summary>

- [page Wikipédia](https://fr.wikipedia.org/wiki/Pong)
- [vidéo Youtube](https://youtu.be/uStS-2nmnig?si=4EL7QbFCgEnADm-r&t=4)
</details>

## Mission 2 : La Base

_Préambule :_
Lorsque l’on commence à coder un jeu vidéo, on est parfois tenté par aborder tout de suite l’aspect des visuels en recherchant
ou en créant des sprites (images).
Heureusement, ici, nous n’avons pas besoin de nous occuper de cela ni de l’ambiance musicale ^^’ Alors allons droit au but !

- [ ] Créer 2 raquettes (2 surfaces rectangulaires), placées de part et d’autre de l’écran.
- [ ] Créer une balle (1 petite surface carrée, pour respecter le style rétro), placée vers le centre de l’écran.
- [ ] Afficher ces 3 surfaces sur l’écran.

_Note :_
- Les couleurs des raquettes, de la balle et du fond sont libres.
- Les dimensions des raquettes et de la balle sont libres.

<details>
<summary>Indice</summary>

Rappel avec l’exemple de la balle:
```python
# en dehors de la boucle
ball_surface = pygame.Surface((width, height))
ball_surface.fill(color="white")
ball_rectangle = ball_surface.get_rect(center=(x, y))
# dans la boucle
screen.blit(ball_surface, ball_rectangle)
```
</details>

## Mission 3 : Le contrôle de la raquette
- [ ] Déplacer la raquette de gauche, sur l’axe vertical, avec la souris.

_Note :_
- Utiliser le "cadre" (objet `Rect`) de la raquette pour la déplacer.

<details>
<summary>Indices</summary>

- Pour rappel, `pygame.mouse.get_pos()` retourne un tuple (x, y) avec les coordonnées de la position de la souris.
- Exemple pour attribuer une nouvelle position à un objet rectangle : `ball_rectangle.center = (x, y)`.
</details>

## Mission 4 : Une balle mobile
- [ ] Déplacer la balle en continu, dans une direction, disons sud-ouest.

_Note :_
- La quantité de pixels de déplacement est libre.
<details>
<summary>Indices</summary>

- Aller dans une direction, c’est faire un déplacement sur l’axe x et sur l’axe y. Par exemple, la direction (1, 1) : si on l’additionne à la position d’une entité, c’est-à-dire x+1 et y+1, elle va aller vers le sud-est.
- Pour déplacer la position de la balle relativement à sa position actuelle, utilisez `ball_rectangle.move_ip(x, y)`
</details>

## Mission 5 : Une IA imbattable
- [ ] Faire bouger la raquette de droite, sur l’axe vertical, pour qu’elle suive automatiquement la balle.

<details>
<summary>Indice</summary>

- Suivre la balle, c’est avoir la même position en y que la balle.
</details>

## Mission 6 : Le contact avec le bord de la fenêtre
- Détecter une collision avec le bord haut ou le bord bas de la fenêtre.
- [ ] Faire un print("rebond vertical"), lorsque la balle touche le bord haut ou le bas de la fenêtre.

_Note :_
- Si cela peut vous être utile, les objets `Rect` ont des attributs qui permettent de récupérer les coordonnées de leurs bords, tels que `top` et `bottom`.

<details>
<summary>Indice</summary>

- Si vous comparez la position de la balle avec un bord tel que `ball_rectangle.top == 0`, 
préférez utiliser `ball_rectangle.top <= 0`, car si la balle se déplace à plus d’un pixel par frame, elle peut passer de l’autre côté du bord sans que la condition soit vraie.
</details>

## Mission 7 : Le contact avec les raquettes

- Détecter une collision avec les raquettes.
- [ ] Lorsque que la balle touche une raquette, faire un print("rebond horizontal").

_Note :_
- Utilisez la méthode `colliderect` de l'object `Rect`.

## Mission 8 : Le rebond
- [ ] Créer une fonction qui prend en paramètre une direction et un axe de rebond et qui retourne la nouvelle direction (suite au rebond).
- [ ] Utiliser cette fonction pour gérer les rebonds de la balle sur les raquettes.
- [ ] Utiliser cette fonction pour gérer les rebonds de la balle sur les bords haut et bas de la fenêtre.

<details>
<summary>Indices</summary>

- Quand on lance une balle en avant, que se passe-t-il au rebond sur le sol ? Elle va garder sa trajectoire en avant, mais repart en l'air (au lieu de continuer de tomber à travers le sol).  
  On peut dire qu'au rebond sur le sol, sa valeur en y est inversée, mais son x reste le même.
- Un exemple de fonction :
```python
def bounce(direction, axis):  # direction est un tuple (x, y), axis est une chaine de caractère "x" ou "y"
    if axis == "x":
        return ...  # à compléter
    elif axis == "y":
        return ...  # à compléter
```
</details>

## Missions Bonus
Bravo **Padawan**, vous avez un Pong tout à fait jouable et respectable ! 
Bien sûr, on peut l'améliorer. Comment ? Je vous laisse y réfléchir quelques secondes...
<details>
<summary>Quelques idées d'amélioration (liste non exhaustive)</summary>

- compter et afficher un score,
- augmenter la vitesse de la balle,
- proposer un mode 2 joueurs,
- ajouter les effets sonores,
- ajouter des effets/éléments graphiques,
- ajouter des pièges sur la carte,
- ajouter des bonus sur la carte,
- pouvoir mettre en pause,
- enregistrer le meilleur score.
</details>

À vous de jouer !

Sachez qu'il y a encore plein de notions à explorer dans PyGame, comme l'utilisation des objets Sprites et des groupes de Sprites (et la collision multiple). 
Hé oui, l'aventure continue ! 🤩
