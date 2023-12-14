# Partie 1 - Exploration

## Mission 0 : Atterrissage
- [ ] Télécharger le fichier [`draw_base.py`](draw_base.py) qui servira de base pour les missions suivantes.
- [ ] Ouvrir le fichier dans un éditeur de texte.
- [ ] Exécuter le fichier.

## Mission 1 : Peintre en herbe
- [ ] Changer la couleur du fond, pour faire mettre une couleur "herbe".

<details>
<summary>Indices</summary>

Pour remplir une surface d'une couleur, on utilise sa méthode `fill()`.  
Elle prend en paramètre un tuple de 3 valeurs numériques (R, G, B), pour **(Red, Green, Blue)**, correspondant aux composantes de la couleur souhaitée.

Exemples:
- `(0, 0, 0)` correspond au noir. 
- `(255, 255, 255)` au blanc. 
- `(255, 0, 0)` au rouge.
- `(128, 0, 128)` au violet.
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

## Mission 3 : Y'a de l'ambiance
- [ ] Changer la couleur du cercle une frame sur deux (couleur au choix).

<details>
<summary>Indices</summary>

- Une frame sur deux, c'est une itération de la boucle principale sur deux.
- Vous pouvez créer un variable qui vous aidera pour la condition du choix de la couleur.
</details>


## Mission 4 : Artificier
- [ ] Créer une animation qui agrandit le cercle (jusqu'à 200px de rayon).

_Note :_
- Lorsque le rayon du cercle atteint 200px, il repart à 0px, pour une animation infinie.
<details>
<summary>Indices</summary>

- Faire une animation, c'est augmenter un tout petit peu la taille du cercle à chaque itération de la boucle principale.
- Pensez à mettre également dans la boucle la ligne de code qui met à jour l'affichage écran (`display.flip()`).
- Vérifier à chaque itération que le cercle n'a pas atteint sa taille maximale.
</details>

## Mission 5 : Maitre du feu
- [ ] Contrôler l’animation avec le bouton de la souris.

_Note :_
- Continuer l'animation tant que le bouton est enfoncé, sinon mettre en pause. 

<details>
<summary>Indices</summary>

- `MOUSEBUTTONDOWN` est l'événement produit lorsque le bouton de la souris est enfoncé.
- `MOUSEBUTTONUP` est l'événement produit lorsque le bouton de la souris est relâché.
- Pensez à mettre dans la boucle la ligne de code qui remplit l'arrière-plan (`screen.fill(...)`).
</details>

## Prochaine mission ? 
Bravo 👍 ! Vous avez terminé la première exploration de l'outil `pygame` ! (et vous avez obtenu le grade **Scout** 🔥, si jamais ça pouvait vous faire de l'effet)


Pour continuer vos expériences vidéo ludique avec un héro 🦸‍, un bouclier 🛡 et des méchants 😈... Allez voir la [Partie 2](part2_instructions.md) !