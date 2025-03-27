# Partie 1 - Exploration

## Mission 0 : Atterrissage
- [ ] Télécharger le fichier [`draw_base.py`](draw_base.py) qui servira de base pour les missions suivantes.
- [ ] Ouvrir le fichier dans un éditeur de texte.
- [ ] Exécuter le fichier.

## Mission 1 : Ciel en peinture
- [ ] Changer la couleur du fond, pour faire afficher une couleur représentant un "ciel nocturne" (tout ciel sera accepté).

<details>
<summary>Indices</summary>

- Pour remplir une surface d'une couleur, on utilise sa méthode `fill()`.  
- Elle prend en paramètre un tuple de 3 valeurs numériques (R, G, B), pour **(Red, Green, Blue)**, correspondant aux composantes de la couleur souhaitée. Ressource utile: [rgbcolorpicker.com](https://rgbcolorpicker.com/).

Exemples:
- `(0, 0, 0)` correspond au noir. 
- `(255, 255, 255)` au blanc. 
- `(255, 0, 0)` au rouge.
- `(128, 0, 128)` au violet.
</details>

<details>
<summary>Rendu suggéré</summary>
  
![mission_1](https://github.com/user-attachments/assets/63f15022-2491-43c7-9f38-8783a6c51fd8)
</details>


## Mission 2 : Géomètre
- [ ] Centrer le cercle.
- [ ] Augmenter la taille du cercle (x2 plus grand).

<details>
<summary>Indices</summary>

`draw.circle` a 2 paramètres qui nous intéressent :
- `center`: permet de définir la position du centre du cercle. Il correspond un tuple (x, y) définissant ses coordonnées.
- `radius`: permet de définir le rayon du cercle en pixel.
</details>

<details>
<summary>Rendu suggéré</summary>

![mission_2](https://github.com/user-attachments/assets/8f839361-8570-429e-828c-d5b4239b2fe5)
</details>


## Mission 3 : Y'a de l'ambiance
- [ ] Changer la couleur du cercle une frame sur deux (couleurs au choix).

<details>
<summary>Indices</summary>

- Une frame sur deux, c'est une itération de la boucle principale sur deux.
- Vous pouvez créer une variable qui vous aidera pour la condition du choix de la couleur.
- Pensez à mettre également dans la boucle la ligne de code qui met à jour l'affichage écran (`display.flip()`).
</details>

<details>
<summary>Rendu suggéré</summary>

![mission_3](https://github.com/user-attachments/assets/f7f42040-8fb5-4ff1-a61a-598d1c21a2c7)
</details>

## Mission 4 : Artificier
- [ ] Créer une animation qui agrandit le cercle (jusqu'à 200px de rayon).

_Note :_
- Lorsque le rayon du cercle atteint 200px, il repart à 10px, pour une animation infinie.
- L’effet de clignotement ajouté précédemment peut être retiré.

<details>
<summary>Indices</summary>

- Faire une animation, c'est augmenter un tout petit peu la taille du cercle à chaque itération de la boucle principale.
- Pensez à mettre dans la boucle la ligne de code qui remplit l'arrière-plan (`screen.fill(...)`).
- Vérifier à chaque itération que le cercle n'a pas atteint sa taille maximale.
</details>

<details>
<summary>Rendu suggéré</summary>

![mission_4](https://github.com/user-attachments/assets/32cf06e4-c4c0-4413-ae34-5ba87d12d844)
</details>

## Mission 5 : Maitre du feu
- [ ] Contrôler l’animation avec le bouton de la souris.

_Note :_
- Continuer l'animation tant que le bouton est enfoncé, sinon mettre en pause. 

<details>
<summary>Indices</summary>

- `pygame.MOUSEBUTTONDOWN` est le type d'événement produit lorsque le bouton de la souris est **enfoncé**.
- `pygame.MOUSEBUTTONUP` est le type d'événement produit lorsque le bouton de la souris est **relâché**.
</details>

<details>
<summary>Rendu suggéré</summary>

![mission_5](https://github.com/user-attachments/assets/ee7eba6f-e6e4-4b14-ac83-32a772769b06)
</details>

## [Bonus] Mission 6 : Maître artificier
- [ ] À chaque clic de la souris, faire apparaître un nouveau cercle centré sur la position de la souris (au moment du clic).

_Note :_
- Les cercles ont tous la même taille.
- L’effet de pause/reprise au clic ajouté précedemment peut être retiré.

<details>
<summary>Indices</summary>
  
- `pygame.mouse.get_pos()` retourne la position de la souris (x, y).
- l’utilisation d’une liste pour stocker la position des cercles est probablement bienvenue.
</details>

<details>
<summary>Rendu suggéré</summary>

![mission_6](https://github.com/user-attachments/assets/9fdcfd0c-6bc7-42fc-923f-14db30e77cd1)
</details>

## [Bonus] Mission 7 : Grand maître artificier
- [ ] Chaque nouveau cercle commence avec une taille de 10px et grandissent à présent indépendamment les uns des autres.
- [ ] Chaque cercle se voit attribuer une couleur aléatoire.
- [ ] Définir une classe `Circle` pour gérer les attributs de chaque cercle.

<details>
<summary>Indices</summary>

- Obtenir une couleur aléatoire revient à générer aléatoirement les 3 composantes RGB qui la constituent.
- Les attributs uniques à chaque cercle sont : sa taille, sa position et sa couleur. Quels attributs ont une valeur "par défaut" et lesquels sont obligatoire à l'instanciation ?
- Ajouter une méthode `grow` à la classe `Circle` permet de simplifier la gestion des tailles.  
</details>

<details>
<summary>Rendu suggéré</summary>

![mission_7](https://github.com/user-attachments/assets/a40de833-50bc-45fc-acee-d866a821b119)
</details>
