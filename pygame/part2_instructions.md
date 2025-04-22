# Partie 2 - Rencontre de l'Autre

## Mission 0 : Préparatifs
- [ ] Télécharger le fichier [`game_base.py`](game_base.py) qui servira de base pour les missions suivantes.
- [ ] Ouvrir le fichier dans un éditeur de texte.
- [ ] Exécuter le fichier.


## Mission 1 : S'approprier le héros-rond
- [ ] Contrôler la position du cercle (qui représente votre héros) avec la souris (suivre le curseur).

<details>
<summary>Indices</summary>

- `pygame.MOUSEMOTION` est le `type` d'événement produit lorsque la souris bouge.
- `pygame.mouse.get_pos()` est une méthode qui retourne la position de la souris sous forme d'un tuple (x, y).
</details>

## Mission 2 A : Le bouclier (théorique) de l’espace
- [ ] Le joueur active son bouclier en restant appuyé sur la touche espace.
  - [ ] Faire un `print("paré")` lorsque le bouclier est activé.
  - [ ] Faire un `print("vulnérable")` lorsque le bouclier est désactivé.

<details>
<summary>Indices</summary>

- `pygame.KEYDOWN` et `pygame.KEYUP` sont respectivement les `type` d'événements produits lorsque l'on appuie et relâche une touche du clavier.
- `pygame.K_SPACE` est un évenement `key` correspondant à la touche espace (voir l'exemple de la touche échap dans le code).
- Vous pouvez créer une variable qui mémorise l'état d'activation du bouclier.
</details>

## Mission 2 B : Un presque vrai bouclier métallique
- [ ] Afficher le héros en gris lorsque le bouclier-armure est activé.
- [ ] Retirer les `print` précédemment ajoutés.

## Mission 3 : Un méchant pas encore méchant
- [ ] Afficher un carré de 50x50 pixels (hello le méchant!) quelque part dans le quart nord-ouest de l’écran.

_Note :_
- Couleur du méchant libre.

<details>
<summary>Indice</summary>

-  `pygame.draw.rect(screen, color="black", rect=(x, y, width, height))`
</details>

## Mission 4 : LA rencontre (inoffensive)
- [ ] Détecter la collision entre le héros et le méchant en utilisant la méthode [`colliderect`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect).
  - [ ] Faire un `print("battle")` (ou `print("bisous")`, comme vous préférez) lorsque le héros et le méchant sont en contact.

_Note :_
- Enregistrer la variable de retour du `draw` pour obtenir un objet `Rect`.
- La méthode `colliderect` de cet objet (`Rect`) permet de détecter la collision avec un autre objet de type `Rect`.

<details>
<summary>Indices</summary>
 
- Exemple :
  ```
      racket_rect = pygame.draw.rect(screen, color="white", rect=(100, 70, 50, 50))
      ball_rect = pygame.draw.circle(screen, color="yellow", center=(150, 20), radius=25)
      if racket_rect.colliderect(ball_rect):
          # Faire rebondir la balle
  ```
  `racket_rect.colliderect(ball_rect)` renvoi un booléen (`True` ou `False`) en fonction du résultat de la détection de la collision.

</details>

## Mission 5 : ~~Du sang~~ Du rouge sur les mains
- [ ] Changer la couleur du héros en rouge lorsqu'il est en collision.
- [ ] Créer une variable correspondant aux points de vie du héros.
  - [ ] Perdre de la vie lorsque le héros est en collision.
  - [ ] Quitter le jeu quand le héros n’a plus de vie.

_Note :_
- Toute nuance de rouge est acceptée.
- Ignorer le bouclier pour l'instant.
- Le nombre de point de vie max de votre héros est libre, toutefois une valeur supérieure à 50 est conseillée.
- C'est OK de perdre de la vie en continu tant que le héros touche notre ennemi (disons... toxique).
<details>
<summary>Indice</summary>

- Quitter le jeu revient à quitter la boucle principale.
</details>

## Mission 6 : Parce que la meilleure attaque est la défense ?
- [ ] Lorsque le bouclier est activé, notre héros ne doit pas perdre de vie (ni de sang) au contact de l'ennemi.

## Mission spéciale 7 A : La puissance du blit

_Préambule_ :

Vous qui suivez ces missions avec ferveur, il faut absolument qu'on vous avoue quelque chose : 

**Utiliser `draw` pour gérer des animations, ce n'est pas top...**

En effet, `draw` s'occupe à la fois de générer la forme, la remplir d'une couleur, la positionner et enfin de l'"afficher" sur l'écran (pris en compte par le `display.flip()` final).  
Pour découvrir PyGame, c'était très pratique, toutefois, pour gérer plus finement et efficacement l'affichage, on va préférer utiliser des
objets spécialement conçus pour gérer chacune de ses fonctions.

Pour cette mission, on va s’intéresser à 2 notions de base de PyGame:
- les objets `Surface` pour gérer les **images** (ou formes),
- la méthode `blit` pour **recopier** ces images sur une surface comme l’écran.

En fait, on peut imager la `Surface` comme une peinture (le tableau, pas le tube) et l’action de `blit` comme copier-coller la peinture sur un mur (à une position donnée).

<details>
<summary>Pourquoi, utiliser ce type d’objets ?</summary>
  
Parce que ça permet entre-autre de :
- ne pas générer les images à chaque itération de la boucle,
- changer la couleur de la surface sans recréer la forme,
- changer la position de l’image sans toucher à l’image elle-même,
- copier une même image plusieurs fois sur la même surface (imaginer un fond avec plusieurs même nuages),
- copier une image sur n’importe quelle autre image, même autre que l’écran (comme coller une image de chapeau sur la surface dédiée au héros).
</details>

Assez discuté, passons à la pratique pour démystifier tout ça !

- Remplacer les appels à `draw` par la création de `Surface` et d'appels à `blit`.
    - [ ] En dehors de la boucle, créer plusieurs `Surface` pour le héros (correspondant a ses différentes couleurs) et une pour l'ennemi.
    - [ ] Dans la boucle, utiliser `screen.blit(...)` pour afficher les surfaces.

_Note :_
- Comme on ne vous a pas encore dévoilé tous les secrets des objets `Rect` utilisés pour la collision, cette partie ne sera 
malheureusement plus fonctionnelle. Mais ne l’effacez surtout pas ! Elle remarchera dans la deuxième partie de cette mission.  
Pour tester la partie A de cette mission, vous pouvez soit mettre en commentaire les lignes concernant la collision, soit les garder au chaud dans un fichier à part. 
- Notre héros-rond va être remplacé par un héros-carré le temps de cette mission spéciale (ce qui pourrait être considéré comme une régression). 
Je tiens toutefois à dévoiler que ce petit humain aura un vrai visage dès la mission 9 :).

<details>
<summary>Indices</summary>

- Exemple d'utilisation avec une balle:
```python
# Initialisation de la surface en dehors de la boucle
ball_surface = pygame.Surface((width, height))
ball_surface.fill(color="yellow")
# Dans la boucle
while going:
  # Traitements divers
  screen.blit(ball_surface, (x, y)) # Copie la "peinture" de la ball à la position (x, y) de l’écran
  pygame.display.flip()
```
- L’appel à `blit` ne remplace pas l’appel à `pygame.display.flip()` qui s’occupe de mettre à jour la fenêtre graphique.
</details>

## Mission spéciale 7 B : Donner un cadre aux personnages

_Préambule_ :

Parce que notre ~~puissance~~ curiosité n’a pas de limite, on va s’intéresser à une autre notion de base de PyGame : les objets `Rect`.
Ils vont nous permettre de gérer la **position** des images.

En fait, on peut imager un objet `Rect` comme un cadre pour un tableau.  
Ainsi:
- On peut le déplacer le cadre indépendamment de la peinture qu’on compte y mettre.
- On peut avoir plusieurs images compatibles avec un même cadre (comme plusieurs armes possibles dans l’emplacement de la main droite).

Pour gérer la collision entre deux entités, on va vérifier si leurs cadres se touchent (indépendamment de l’image de ces entités à l’instant t).

Et comme le monde est bien fait, la fonction `blit` peut prendre en paramètre un objet `Rect` (au lieu d’une coordonnée), pour copier-coller la `Surface` à la position du cadre.

- Utiliser des objets `Rect` pour gérer l’emplacement des entités.
  - [ ] En dehors de la boucle, créer **un** objet `Rect` pour notre héros et un autre pour le méchant.
  - [ ] Utiliser la méthode `center` de cet objet pour re-positionner le héros.
  - [ ] La collision doit être à nouveau fonctionnelle.

<details>
<summary>Indice</summary>

Exemple d'utilisation avec une balle :
```python
# Initialisations en dehors de la boucle
ball_surface = pygame.Surface((width, height))
ball_surface.fill(color="yellow")
ball_rectangle = ball_surface.get_rect()  #  Génère un cadre de la taille de la surface.
# Dans la boucle
while going:
  # Traitement divers
  ball_rectangle.center = (x, y)  # Bouge le "cadre" (possibilité de spécifier top, bottom, left, right, au lieu de center)
  screen.blit(ball_surface, ball_rectange)  # Affiche la "peinture" de la balle au niveau du "cadre" (situé à la position x, y)
  pygame.display.flip()
```
</details>

## Mission 8 : Un méchant avec des pieds
- [ ] Déplacer le méchant de manière autonome, en ligne droite vers l’est.

_Note :_
- Vitesse de déplacement : 1px par frame.
- Utiliser la méthode `move_ip` (pour "move in place") de l'objet `Rect` du méchant pour le déplacer relativement à sa position.
- Pas grave si le méchant fini par sortir de l’écran ^^.

## Mission 9 : Restaurer leurs images

- [ ] Mettre un visage sur le héros et sur le méchant.
- [ ] Afficher son image avec le bouclier lorsque le bouclier est activé, afficher l'image du héro blessé lorsqu'il saigne.

_Note :_
- Vous trouverez ce qu’il vous faut dans le répertoire [`part2_assets`](part2_assets) du projet. Téléchargez ce répertoire à la racine de votre projet python.

<details>
<summary>Indices</summary>

- Pour charger une image, utilisez la méthode `pygame.image.load("path/to/image.png")`. Elle retourne une `Surface` contenant l'image.
- Vous pouvez initialiser plusieurs surfaces qui seront affichées au niveau d'un même et unique `Rect` en fonction de la situation.
</details>

## Misson BONUS 9 B: De l'herbe à ~~chat~~ crabe

- [ ] Créer une surface pour le background, pour lequel pour aurez chargé l'image d'herbes disponible dans les assets et afficher-la avec un `blit` sur l'écran.

## Mission BONUS 10 : Un ennemi avec des yeux
- [ ] Le méchant se déplace vers le joueur.

_Note :_
- Vitesse de déplacement : 1px par axe (x, y). 


<details>
<summary>Indices</summary>

Pour vous simplifier la tâche, vous pouvez utiliser la fonction `get_relative_move` donnée ci-dessous, qui prend en paramètre les positions de 2 entités (A et B) et qui retourne la direction pour que B se déplace vers A.

Par exemple:

Si rect_a est en x=50 et y=100,  
et rect_b est en x=20 et y=150,
il faut que B avance sur l'axe x (va vers l'est) et remonte sur l'axe y (va au nord) si il veut espérer rejoindre A.  
C'est justement ce que nous donne `get_relative_move(rect_a, rect_b)` qui va renvoyer le tuple x=1, y=-1.  
  
```python
def get_relative_move(a_pos, b_pos):
    x_diff = a_pos[0] - b_pos[0]
    move_x = (x_diff > 0) - (x_diff < 0)
    y_diff = a_pos[1] - b_pos[1]
    move_y = (y_diff > 0) - (y_diff < 0)
    return move_x, move_y
```

Vous pouvez directement l'apppeler en paramètre de `move_ip`, comme suit : `b_rect.move_ip(get_relative_move(a_rect, b_rect))`.
</details>
