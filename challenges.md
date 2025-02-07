# Pile ou Face
Écrire une fonction 
    qui ne prend pas de paramètres
    qui affiche aléatoirement “pile” ou “face” 
    qui ne renvoie rien

Tips
Voir la documentation de random.

```
>>> pile_ou_face()
pile
```

# Conseil Météo
Écrire une fonction 
    qui prend en paramètre :
    une température (entier)
    qui affiche “prend une écharpe” si  T < 10,
        affiche “prend ton mateau” si T < à 15, 
        affiche “prend de l’eau” si T >= 10
    qui ne renvoie rien

```
>>> meteo_advice(9)
prend ton écharpe
prend ton manteau
```

# Moyenne d’âges
Écrire une fonction 
    qui prend en paramètre une liste d’âges (entiers)
    qui calcule la moyenne des âges
    qui renvoie le résultat

Tips
La moyenne est calculée par la somme les éléments de la liste, divisée par le nombre d’éléments de la liste.

```
>>> age_average([15, 28, 42, 56])
35.25
```

# Décodeur
Écrire une fonction 
    qui prend en paramètre : une chaîne
    qui remplace tous les “x” par “o” et les “f” par “e”
    qui renvoie la chaîne décodée

Tips
Les majuscules ne sont pas prises en compte.

```
>>> decode(“Qufllf bfllf jxurnff sur Xfnxn III !”)
'Quelle belle journee sur Xenon III !'
```

# Générateur de pseudo
Écrire une fonction 
    qui prend en paramètre : la taille n (en syllabes) d’un pseudo
    qui renvoie un pseudo aléatoire de n syllabes
	
Tips
Définir une liste des syllabes possibles

```
>>> nickname(4)
'patibulon'
```

# Carré ascii
Écrire une fonction 
    qui prend en paramètre : la taille n d’un carré et le caractère qui dessine le carré
    qui affiche un carré de taille n
    qui ne renvoie rien

```
>>> print_square(4, "*")
****
****
****
****
```

# Distance ennemie
Écrire une fonction 
    qui prend une chaîne en paramètre, représentant un terrain (ex : “-x--o----x--”)
        où “o” définit un personnage
        et “x” définit un ennemie
    qui renvoie la distance entre “x” et “o” la plus courte

```
>>> distance("-x----o--x---")
2
```
