#!/usr/bin/env python
# coding: utf-8

# ![Mohammed al-Khwarizmi](img/al-khwarizmi.jpg)
# 
# 
# # Mohammed al-Khwarizmi
# ---
# 
# Le mot français « algorithme » provient du nom d'un savant arabe du $IX^{ème}$ siècle : **Mohammed al-Khwarizmi** (Khiva vers 788 — vers 850 Bagdad) qui fut l'un des inventeurs de l'algèbre et du système décimal.
# C'est également grâce à lui que se diffuseront les chiffres arabes en Occident.
# 
# Le premier ouvrage *al-Kitâb al-mukh- tasar fâ hisâb al-jabr w'al-muqâbala*, le Livre de l'explication du calcul de la remise en place et de la simplification, a donné son nom à l'algèbre.
# 
# Al-Khwarizmi y présente une exposition complète de la résolution des équations du premier et du second degré. L'inconnue, que nous notons `x`, s'appelle la *racine* et, comme il a éliminé tout nombre négatif, il distingue six cas et les traite sur des exemples qui se généralisent sans difficulté pour toute équation de même type. 
# 
# Il considère ainsi :
# - Carrés égaux aux racines, c'est-à-dire de la forme $ax^2 = bx$ ;
# - Carrés égaux à un nombre, soit $ax^2 = c$ ;
# - Racines égales à un nombre, soit $bx = c$ ;
# - Carrés et racines égaux à un nombre, soit $ax^2 + bx = c$ ;
# - Carrés et nombre égaux aux racines, soit $ax^2 + c = 6x$ ;
# - Racines et nombres égaux aux carrés, soit $bx + c = ax^2$;
# 
# où `a`,`b` et `c` désignent des nombres positifs.
# 
# Contrairement aux mathématicien grecs, al-Khwarizmi détaille des méthodes effectives de résolution d'équations.
# 
# Historiquement liée au calcul, la notion d'algorithme s'est progressivement étendue à la manipulation de différents objets, des textes et des images par exemple. 
# 
# # Les algorithmes
# 
# **Un algorithme est simplement une méthode qui sert à résoudre un problème en un nombre fini d'étapes** : chercher un mot dans le dictionnaire, classer des mots par ordre alphabétique, classer des nombres par ordre de grandeur, chercher le meilleur parcours possible sur une carte, trouver une racine carrée, construire des listes de nombres premiers, etc. 
# 
# On peut décrire un algorithme comme étant une suite d'actions à accomplir séquentiellement, dans un ordre fixé.
# 
# ## Définitions :  Algorithme ≠ Programme 
# 
# ### Algorithme
# 
# Un algorithme est la description abstraite des étapes *simples* conduisant à la résolution d'un problème. C'est la partie conceptuelle d'un programme.
# 
# ### Programme
# 
# Un programme est l'implémentation d'un algorithme dans un langage donné et sur un système particulier.
# 
# ### Exemple
# 
# Décrivez ci-dessous un algorithme pour trouver le maximum d'une *longue* liste de nombres entiers :  
# L = (17, 23218, 543, 7, 1984, 2000000, 21, ... , 3, 666, 69, 0, 42)  

# _Ecrire votre algorithme ici_

# ## Ingrédients de base des algorithmes en pseudo-code
# 
# ### Données
# 
# Elles peuvent être de 3 types:
# 
# 1. entrées
# 2. sorties
# 3. internes
# 
# ### Instructions
# 
# #### Affectations
# 
# Typiquement mettre une valeur ou un résultat dans une variable  
# $x \leftarrow 4$  
# $ \Delta \leftarrow b^2 - 4ac$
# 
# #### Instructions de contrôle
# 
# 1. branchements conditionnels ou test : *si .... alors .... sinon*
# 2. itérations ou boucles : *pour .. allant de .. à ..* ; *pour tous les éléments de ... répéter ...*
# 3. boucles conditionnelles : *tant que (test est vrai) répéter ...*
# 
# #### Exemple : Que fait cet algorithme ?

# **Algorithme**  
# entrée : N entier positif  
# sortie : ??  
# $i \leftarrow 0 $  
# **Tant que** $2^i \leq N $  
# $\quad$ $ i \leftarrow i + 1 $  
# **Sortir :** i

# La sortie de cette algorithme représente le nombre de bits nécessaires pour représenter N en binaire

# ### Que font les algorithmes suivants

# #### Algorithme 1  
# entrée : a, b deux entiers naturels non nuls  
# sortie : ??  
# $x \leftarrow a$  
# $y \leftarrow b $  
# $z \leftarrow 0 $  
# __Tant que__ $y \geq 1 $  
# $\quad$ __Si__ y est pair  
# $\qquad$ $x \leftarrow 2x $  
# $\qquad$ $y \leftarrow y / 2$  
# $\quad$__Sinon__  
# $\qquad$ $z \leftarrow z + x $  
# $\qquad$ $y \leftarrow y-1 $  
# __Sortir :__ z

# Algorithme 1 : 
# 
# _Note :_ Les algorithmes existent depuis bien avant les ordinateurs! En particulier, l’algorithme ci-dessus nous vient de l’Egypte ancienne.

# #### Algorithme 2  
# entrée : n entier naturel  
# sortie : ??  
# $m \leftarrow n$  
# $i \leftarrow 1 $  
# **Tant que** $m \ge 0 $    
# $\quad$ $i \leftarrow 2i $  
# $\quad$ $m \leftarrow m - 1$  
# **Sortir :** i

# Algorithme 2 : 

# #### Algorithme 3  
# entrée : a, b deux entiers naturels non nuls  
# sortie : ??  
# $s \leftarrow 0$  
# **Si** $a \le b$  
# $\quad$ **Pour** i allant de $1 \text{ à } a$  
# $\qquad$ $s \leftarrow s + b $  
# **Sinon**  
# $\quad$ **Pour** i allant de $1 \text{ à } b$  
# $\qquad$ $s \leftarrow s + a $  
# **Sortir :** s

# Algorithme 3 : 

# ### Créations d'algorithme
# 
# Pour ces exercices, la syntax n'est pas primordiale, ce qui est important est de s'assurer que votre algorithme possède des entrées et des sorties, que les différentes étapes sont des opérations *simples* qui se suivent dans le bon ordre afin d'obtenir le résultat. Assurez-vous surtout que votre algorithme s'arrête bien !
# 
# #### Somme de multiples
# 
# Écrivez un algorithme qui calcule la somme des *n* premiers nombres entiers faisant partie de la liste de multiple de 5 et de 7.  
# Pour n = 5, cette somme vaut 5+7+10+14+15 = 51.

# **Somme de multiples** : votre algorithme ici

# #### Comptage de mot
# 
# Soit A une chaîne de caractères formée uniquement de mots et d’espaces (uniques) entre les mots, et soit n sa longueur (exemple: _A_ ="Le silence des agneaux" et donc _n_ = 22). Écrivez un algorithme dont les entrées sont _A_ et _n_, et dont la sortie est le nombre de mots de la chaîne (4 dans l’exemple).

# **Comptage de mot** : votre algorithme ici

# #### Les deux plus grands
# 
# Soit _L_ une liste de nombres entiers positifs de taille _n_ (exemple: _L_ = {3,43,17,22,16} et donc _n_ = 5). Ecrivez un algorithme dont l’entrée est _L_ et _n_, et dont la sortie sont les deux plus grands nombres de la liste (dans l’exemple: 43 et 22).

# **Les deux plus grands** : votre algorithme ici

# ### La méthode al-Khwarizmi
# 
# Voici ci-dessous l'algorithme de al-Khwarizmi pour résoudre toutes les équations du type  $x^2 + bx = c$, où `b` et `c` sont des nombres positifs.
# 
# >On prend la moitié des racines ; on la met au carré, que l'on additionne au nombre.
# Prenons alors la racine carrée de ce nombre et ôtons-lui la moitié des racines pour obtenir la solution.
# 
# **Rappel** : L'inconnue, que nous notons `x`, s'appelle la *racine*.
# 
# Réécrivez cet algorithme en pseudo-code ci dessous:

# **Algorithme d'al-Kwharizmi** : pseudo code à mettre ci-dessous

# ### Implémentation
# 
# Programmer consiste à transmettre à un ordinateur, à l'aide des instructions d'un langage, l'algorithme qu'il doit appliquer pour parvenir au résultat qu'on lui demande d'établir.
# 
# Écrivez en *Python* l'implémentation des algortihmes des exercices précédents.
# 
# Pour pouvoir réaliser cet exercice, il vous faut d'abord avoir vu [OCI04_Boucles](./OCI04_Boucles.ipynb)

# In[ ]:





# Ce Notebook est a été crée par David Da SILVA - 2020
# 
# Source: Tangente HS 37 & EPFL ICC - O. Lévêque
# 
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
