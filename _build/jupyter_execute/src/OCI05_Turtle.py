#!/usr/bin/env python
# coding: utf-8

# # Turtle : la tortue en `Python`
# ---
# 
# *Turtle* est un module graphique du langage de programmation Python. Il est inspiré de la programmation Logo et permet de déplacer une tortue sur l’écran.
# 
# La tortue désigne un robot virtuel capable de se déplacer dans un plan en laissant une trace ou non de son passage. Elle a été inventée dans les années 1960 au MIT par Seymour Papert qui a conçu un langage informatique [LOGO](https://fr.wikipedia.org/wiki/Logo_(langage)) destiné aux enfants. De nombreux langages informatiques ont repris cette idée de tortue et Python n’échappe pas à la règle.
# 
# Le but de cette partie est de découvrir quelques (mais pas toutes) fonctions permettant de contrôler la tortue. 
# Depuis la version 2.5 de Python, c’est le module **`turtle`** qui fournit les fonctionnalités de base permettant de commander une (ou plusieurs) tortues.

# In[1]:


# -*- coding: utf-8 -*-
import turtle


# Les méthodes associées aux tortues peuvent utilisées sans référence à une tortue particulière, elles s'appliquent à une tortue *anonyme* qui est automatiquement créée si nécessaire.
# 
# De la même manière, si aucune fenêtre d'affichage n'existe et qu'on agit sur une tortue, une fenêtre est automatiquement créée et affichée.
# 
# Ces automatismes peuvent paraître pratiques mais peuvent aussi être source de confusion. Il vaut mieux les expliciter.

# In[2]:


discworld = turtle.Screen()
ATuin = turtle.Turtle()


# La tortue peut prendre plusieurs formes, “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.  
# Par défaut elle est du type "classic", vérifiable avec la méthode `shape()`.

# In[3]:


ATuin.shape()


# La même méthode avec un paramètre valide (cf. liste ci-dessus) permet de changer la forme de la tortue

# In[4]:


ATuin.shape("turtle")


# ## Les fonctions de base
# 
# Les principales fonctions mises à votre disposition dans le module turtle sont les suivantes :
# 
# * `reset()` : Efface l’écran, recentre la tortue et remet les variables à zéro
# * `forward(distance)` : Avance d’une distance donnée en pixel
# * `backward(distance)` : Recule d’une distance donnée en pixel
# * `left(angle)` : Pivote vers la gauche d'un angle donné en degrés
# * `right(angle)` : Pivote vers la droite d'un angle donné en degrés
# * `up()` : Relève le crayon pour pouvoir avancer sans dessiner
# * `down()` : Abaisse le crayon pour recommencer à dessiner
# * `goto(x,y)` : Déplace la tortue à la position de coordonnées (x,y) **Attention à ne pas oublier d'utiliser la fonction `up()` avant d'utiliser `goto()` sinon le parcours effectué sera tracé**

# In[5]:


ATuin.left(45)
ATuin.forward(50)
ATuin.right(90)
ATuin.backward(50)
ATuin.up()
ATuin.goto(50,0)
ATuin.left(45)
ATuin.down()
ATuin.forward(50)
ATuin.up()
ATuin.goto(150,0)
ATuin.down()
ATuin.right(45)
ATuin.backward(50)
ATuin.left(90)
ATuin.forward(50)


# In[6]:


discworld.reset()


# In[7]:


turtle.shape("turtle")


# #### `Exercice 1`
# 
# Créez un programme qui dessine un carré dont la longueur des côtés est 121, ce carré étant dessiné depuis l’état(= position et orientation) courant de la tortue.
# 
# Dans quel état se trouve la tortue après avoir tracé un carré ?

# In[ ]:





# #### `Exercice 2`
# 
# À partir de l'exercice précédent, réalisez le dessin de la figure constitué de dix carrés de côté 50 avec un espace de 5 entre chacun d’eux
# 
# <img src="img/ligne10.png" width="300" height="300"/>

# In[ ]:





# #### `Exercice 3`
# 
# Toujours à partir des exercices précédents, réalisez le dessin de la figure, soit un carré constitué de cent carrés de côté 50 disposés en 10 lignes horizontales de 10, avec une espace de 5 entre eux.
# 
# <img src="img/cent_carres.png" width="300" height="300"/>

# #### `Exercice 4`
# 
# Réalisez maintenant le dessin de la figure constitué de cinquante carrés emboîtés ayant tous un sommet commun (en bas à gauche) et dont les longueurs des côtés varient de 10 en 10.
# 
# <img src="img/cinquante_carres.png" width="300" height="300"/>

# In[ ]:





# ## Couleurs
# 
# ### Mode de couleur
# 
# La définition d'une couleur se fait de manière classique à l'aide de sa décomposition dans les 3 couleurs primaires du modèle aditif : **rouge**, **vert** et **bleu** (*RGB* en anglais pour *red*, *green*, *blue*) où chaque couleur peut prendre une valeur entière entre 0 et 255 (soit 256 valeurs =$2^8$ = 1 octet). 
# 
# Alternativement, ces valeurs peuvent être normalisées entre 0 et 1 en divisant par 255. Par défaut `turtle` utilise cette notation normalisée mais il est possible d'utiliser la notation classique en le précisant à l'aide de la méthode `colormode()`.
# 
# * `colormode()` : renvoit le mode courant
# * `colormode(1)` : définit l'utilisation du mode normalisé
# * `colormode(255)` : définit l'utilisation du mode classique
# 
# ### Couleur du trait
# 
# La fonction `pencolor(couleur)` permet de modifier la couleur du tracé (noir par défaut). Si la fonction `pencolor()`est appelé sans paramètres, elle renvoit la couleur courante.
# 
# La `couleur` donnée en paramètre peut être :
# 
# * un tuple RGB `(r,g,b)` où chaque composante est entre 0 et `colormode()` 
# * 3 valeurs R, G et B où chaque composante est entre 0 et `colormode()` 
# * une chaîne de caractère représentant sa valeur en notation **Hexadécimale** 
# 
# Le tableau ci-dessous montre quelques exemples de couleurs.

# <table class="dtable">
# 		<tr>
# 			<th>Couleur</th>
# 			<th>Nom</th>
# 			<th>(R,G,B)</th>
# 			<th>Hex</th>
# 		</tr>
# 		<tr>
# 			<td style="background-color:#000000">&nbsp;</td>
# 			<td>Black</td>
# 			<td>(0,0,0)</td>
# 			<td>#000000</td>
# 		</tr>
# 		<tr>
# 			<td style="background-color:#FFFFFF">&nbsp;</td>
# 			<td>White</td>
# 			<td>(255,255,255)</td>
# 			<td>#FFFFFF</td>
# 		</tr>
# 		<tr>
# 			<td style="background-color:#FF0000">&nbsp;</td>
# 			<td>Red</td>
# 			<td>(255,0,0)</td>
# 			<td>#FF0000</td>
# 		</tr>
# 		<tr>
# 			<td style="background-color:#00FF00">&nbsp;</td>
# 			<td>Green</td>
# 			<td>(0,255,0)</td>
# 			<td>#00FF00</td>
# 		</tr>
# 		<tr>
# 			<td style="background-color:#0000FF">&nbsp;</td>
# 			<td>Blue</td>
# 			<td>(0,0,255)</td>
# 			<td>#0000FF</td>
# 		</tr>
# 		<tr>
# 			<td style="background-color:#FFFF00">&nbsp;</td>
# 			<td>Yellow</td>
# 			<td>(255,255,0)</td>
# 			<td>#FFFF00</td>
# 		</tr>
# 		<tr>
# 			<td style="background-color:#00FFFF">&nbsp;</td>
# 			<td>Cyan</td>
# 			<td>(0,255,255)</td>
# 			<td>#00FFFF</td>
# 		</tr>
# 		<tr>
# 			<td style="background-color:#FF00FF">&nbsp;</td>
# 			<td>Magenta</td>
# 			<td>(255,0,255)</td>
# 			<td>#FF00FF</td>
# 		</tr>
# 		<tr>
# 			<td style="background-color:#BEBEBE">&nbsp;</td>
# 			<td>Gray</td>
# 			<td>(190,190,190)</td>
# 			<td>#BEBEBE</td>
# 		</tr>
# 		<tr>
# 			<td style="background-color:#7F7F7F">&nbsp;</td>
# 			<td>Gray50</td>
# 			<td>(127,127,127)</td>
# 			<td>#7F7F7F</td>
# 		</tr>
# 		<tr>
# 			<td style="background-color:#B03060">&nbsp;</td>
# 			<td>Maroon</td>
# 			<td>(176,48,96)</td>
# 			<td>#B03060</td>
# 		</tr>
# 		<tr>
# 			<td style="background-color:#6B8E23">&nbsp;</td>
# 			<td>OliveDrab</td>
# 			<td>(107,142,35)</td>
# 			<td>#6B8E23</td>
# 		</tr>
# 		<tr>
# 			<td style="background-color:#FA8072">&nbsp;</td>
# 			<td>Salmon</td>
# 			<td>(250,128,114)</td>
# 			<td>#FA8072</td>
# 		</tr>
# 		<tr>
# 			<td style="background-color:#A020F0">&nbsp;</td>
# 			<td>Purple</td>
# 			<td>(160,32,240)</td>
# 			<td>#A020F0</td>
# 		</tr>
# 		<tr>
# 			<td style="background-color:#40E0D0">&nbsp;</td>
# 			<td>Turquoise</td>
# 			<td>(64,224,208)</td>
# 			<td>#40E0D0</td>
# 		</tr>
# 		<tr>
# 			<td style="background-color:#000080">&nbsp;</td>
# 			<td>Navy</td>
# 			<td>(0,0,128)</td>
# 			<td>#000080</td>
# 		</tr>
# 	</table>
# 

# Enfin la couleur passée en paramètre peut aussi être une chaîne de caractère contenant le *nom* de la couleur tel que définit dans la librairie Tcl/tk. Cette librairie définie 511 noms de couleurs représentées ci-dessous.
# 
# Vous pouvez trouver la correspondance entre les *noms* des couleurs et leurs valeurs RGB [ici](https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm).
# 
# <img src="img/python_colors.png"/>
# 
# Par exemple, pour dessiner un triangle rouge :

# In[8]:


discworld.reset() # pour nettoyer la fenêtre
ATuin.pencolor("red")
for _ in range(3):
    ATuin.forward(100)
    ATuin.left(120)


# ### Remplissage
# 
# Il est possible de remplir un polygone avec une couleur. Il faut définir la couleur de remplissage, puis le début et la fin du polygone.
# 
# La couleur de remplissage est définie par la méthode `fillcolor(couleur)` qui s'utilsie de la même manière que `pencolor()`.
# 
# Le début du polygone est marqué par la commande `begin_fill()` et la fin par `end_fill()`. Il n'est pas nécessaire que la tortue se retrouve au départ du polygone pour le terminer, par défaut il se finit par un segment *virtuel* entre le point de départ et la position de la tortue lors de l'appel de `end_fill()`.
# 
# Par exemple, pour dessiner une [Triforce](https://fr.wikipedia.org/wiki/Triforce_(The_Legend_of_Zelda)), il suffit de parcourir les 3 côtés d'un triangle par moitié et de remplir au fur et à mesure.

# In[9]:


discworld.reset()
ATuin.fillcolor("gold2")
ATuin.pencolor("gold2")
ATuin.begin_fill()
ATuin.left(60)
ATuin.forward(50)
ATuin.right(120)
ATuin.forward(50)
ATuin.end_fill()
ATuin.begin_fill()
ATuin.forward(50)
ATuin.right(120)
ATuin.forward(50)
ATuin.end_fill()
ATuin.begin_fill()
ATuin.forward(50)
ATuin.right(120)
ATuin.forward(50)
ATuin.end_fill()


# **A noter : **
# 
# * La commande `begin_fill()` peut être remplacée par `fill(True)` ou `fill(1)`.
# * La commande `end_fill()` peut être remplacée par `fill(False)` ou `fill(0)`.
# * La commande `color(couleur)` définit en même temps la couleur de trait **et** celle de remplissage. Elle s'utilise de la même manière que `fillcolor` et `pencolor`.
# 
# 
# #### `Exercice 5`
# 
# Dessinez le drapeau Français et le drapeau Suisse.

# In[ ]:





# ## Divers
# 
# ### Vitesse de la tortue
# 
# On peut modifier la vitesse de déplacement de la tortue à l'aide de la commande `speed(vitesse)`. La `vitesse` donnée en paramètre peut être un entier entre 0 et 10 ou une chaîne de caractère parmis :
# 
# * "fastest" = 0
# * "fast" = 10
# * "normal" = 6
# * "slow" = 3
# * "slowest" = 1
# 
# **Notes : **
# 
# * Les valeurs supérieures à 10 ou inférieures à 0.5 sont considérées comme égales à 0
# * La vitesse 0 *supprime* les animations, les mouvements sont quasiment instantanés
# 
# ### En vrac
# 
# Quelques commandes utiles :
# 
# * `width(largeur)` : définit l'épaisseur du trait à une `largeur` donnée en pixels
# * `clear()` : permet d'effacer l'écran sans la bouger la tortue ni remettre les variables à zéro
# * `write(texte)` : permet d'écrire une chaîne de caractère `texte` à la position de la tortue
# 
# ### Documentation complète
# 
# Vous pourrez trouver la documentation complète du module `turtle` sur le [site officiel](https://docs.python.org/3/library/turtle.html).
# 
# ## Challenges
# 
# Essayer de reproduire les dessins ci-dessous
# 
# <img src="img/TurtleChallenges.png" height="300"/>
# 
# *Indice : dans la dernière image les lignes sont séparées de $2^{\circ}$*

# Ce Notebook est a été crée par David Da SILVA - 2020
# 
# Source: [openclassrooms.com](https://openclassrooms.com/courses/pratiques-avancees-et-meconnues-en-python)
# 
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
