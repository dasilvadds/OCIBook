#!/usr/bin/env python
# coding: utf-8

# # Introduction à Python & iPython notebook
# ---

# ## Introduction 

# Nous allons apprendre la langage de programmation *Python* ainsi que l'utilisation de différents modules de calculs numériques et de représentation graphique. *Python* est un langage de programmation facile à apprendre et très utilisé c'est pourquoi il a été choisi pour ce cours. Il y a de multiple façons de lancer des progammes *Python*, de la ligne de commandes aux interfaces graphiques.
# 
# [Python](http://www.python.org/) est un langage haut niveau, orienté objet est très versatile.
# 
# Charactéristiques générales de *Python*:
# 
# * **langage simple et clair:** Le code est facile à lire et intuitif, la syntaxe est minimaliste et facile à apprendre.
# * **langage expressif:** Mois de lignes de code, moins de bugs, plus facile à maintenir.
# 
# Détails techniques:
# 
# * **typage dynamique:** Pas besoin de définir le type des variables, des arguments des fonctions ou de ce qu'elles retournent.
# * **gestion automatique de la mémoire:** Pas besoin d'allouer ou de désallouer de la mémoire pour les variables et les structures de données. Pas de problèmes de fuite de mémoire.
# * **langage interprété:** Pas besoin de compiler le code. L'interpréteur *Python* lit et exécute le code à la volée.
# 
# Avantages:
# 
# * Le principal avantage est la facilité de programmation ce qui minimize le temps de développement, de débuggage et de maintien du code.
# * La conception du langage encourage plusieurs bonnes pratiques de programmation:
#  * Programmation orientée objets et modulaire.
#  * Réutilisation du code.
#  * Intégration de la documentation dans le code.
# * Une vaste collections de librairies et de modules additionnels.
# 
# Désavantages:
# 
# *Python* étant un langage interprété et à typage dynamique, l'exécution de code *Python* peut être plus longue que celle de code écrit dans des langage compilé forrtement typés tels que C++ ou Fortran. 
# 

# In[ ]:


print("Bonjour")


# ## Les bases en Python

# Ce cours se fera par le biais de *notebook ipython* comme celui-ci. 
# Un notebook est interactif - vous pouvez modifier et faire tourner du code dans des cellules et sauvegarder le résultat.
# Les cellules de code commencent par "In [*n*]:" où *n* indique l'ordre dans lequel les cellules ont été interprétées. Le résultat de l'interprétation du code est normalement affichée dans une cellule directement sous-jacente commençant par "Out [*n*]:". Pour exécuter le contenu d'une cellule, utilisez *shift-enter* ou sélectionnez *Run* dans le menu *Cell*.
# 
# Il est conseillé d'exécuter chaque cellule de code et de s'assurer d'avoir compris pourquoi un certain résultat est produit. Certaines cellules de code dépendent de définitions faites dans des cellules précédentes, vous obtiendrez les meilleurs résultats en exécutant les cellules de manière séquentielles. Au fur et à mesure que vous avancerez dans un notebook, vous trouverez des exercices marqués "Exercice", faites-les !
# 
# **Quelques instructions de base**
# 
# - Cliquez sur les bouton `Play` pour exécuter et passer à la cellule suivante. Le raccourci clavier est `shift-enter`
# - Pour ajouter une nouvelle cellule sélectionnez le menu `"Insert->Insert New Cell Below/Above"` ou cliquez sur le bouton '+'
# - Vous pouvez changer le mode code d'une cellule vers le mode texte en utilisant le menu déroulant.
# - Vous pouvez changer le contenu d'une cellule en double-cliquant dessus.
# - Pour sauvegarder votre notebook, sélectionnez le menu `"File->Save and Checkpoint"` ou pressez `Ctrl-s` ou `Command-s` sur un Mac
# - Pour annuler une opération, pressez `Ctrl-z` ou `Command-z` sur un Mac
# - Pour annuler la supression d'une cellule faite par le menu `Edit->Delete Cell`, sélectionnez le menu `Edit->Undo Delete Cell`
# - Le menu `Help->Keyboard Shortcuts` propose une liste de raccourcis clavier
# 
# Ce notebook est inspiré des notebooks suivants:
# 
# * [Lab1-IntroductionToPython](http://www.ectropy.info/post/python-introduction-labs) de Alexei Gilchrist
# * [A Crash Course in Python for Scientists](http://nbviewer.ipython.org/gist/rpmuller/5920182) de Rick Muller
# * [Lectures on Scientific Computing with Python](http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/tree/master) de J.R. Johansson.

# ### Arithmetique

# Vous pouvez utiliser python comme une calculatrice, les priorités de calcul sont respectées.
# Par exemple, $9 \times (2+3) -40 +2^2$ s'écrit :

# In[ ]:


9 * (2 + 3) - 40 + 2


# Dans un notebook, le résultat d'une cellule est celui de la dernière commande.

# In[ ]:


12
12 * 12
12 * 12 * 12
12 * 12 * 12 * 12
print("Toto")


# Pour afficher les résultats intermédiaires, utiliser la fonction `print`

# In[ ]:


print(3 * 7)


# #### Exercice
# 
# Modifiez le code ci-dessous afin d'afficher tous les résultats intermédiaires

# In[ ]:


12
12*12
12*12*12
12*12*12*12


# Les nombres complexes sont définis de manières native en python. Un nombre imaginaire est suivi de la lettre "j":

# In[ ]:


2j


# En général un nombre complexe et l'addition d'un réel et d'un nombre imaginaire, par exemple:

# In[ ]:


2 + 1j + 4 + 2j


# et

# In[ ]:


(2 + 1j) * (4 + 2j)


# #### Exercice
# 
# Étant donné le nombre imaginaire pur $i=\sqrt{-1}$, calculez $i^i$ :

# In[ ]:





# ### Variables

# Les variables sont définies à l'aide du symbole égal ( **=** ) et la valeur peut être n'importe quel objet Python (nous reviendrons plus en détails sur la notion d'objet un peu plus tard). 
# Le type d'objet affecté à une variable peut changer durant l'exécution d'un programme, il n'est pas définitif - c'est le typage dynamique.
# Le nom d'une variable doit commencer avec une lettre ou une underscore ( **\_** ) et peut contenir des caractères alphanumériques et des underscores.
# **Prenez l'habitude de donner des noms significatifs à vos variables.**

# In[ ]:


A = 10
B_2 = 5
A_plus_B_2 = A + B_2
print(A**B_2)

A = "Five "
print(A * B_2)


# Certains noms sont réservé pour le langage et ne peuvent pas être utilisés pour des variables:
# 
#     and, as, assert, break, class, continue, def, del, elif, else, except,
#     exec, finally, for, from, global, if, import, in, is, lambda, not, or,
#     pass, print, raise, return, try, while, with, yield

# Une fonctionalité très pratique de *iPython* est la complétion automatique. Dans la cellule suivante, tapez `A_` puis la touche TAB ( ->| ).

# In[ ]:





# #### Exercice
# 
# Affectez les valeurs suivantes aux variables correspondantes:
# - `7` dans la variable `my_int`
# - `2.21` dans la variable `my_float`
# - `True` dans la variable `my_bool`

# In[ ]:





# Effectuez les opérations suivantes:
# - `my_int` divisé par `my_float` 
# - `my_float` à la puissance `my_int`
# - `my_bool` plus `my_int`

# In[ ]:





# Que se passe-t-il pour la troisième opération si on affecte `False` à `my_bool` ?
# Que peut-on en déduire au sujet des variables booléennes en *Python* ?
# 
# Ecrivez votre réponse dans une nouvelle cellule ci-dessous.

# ### Strings (chaîne de caractères)

# En *Python* les chaînes de caractères (*string*) sont défini en utilisant des paires de guillemets simple (') ou double ("). Cela permet d'inclure des apostrophes ou des citations dans des chaînes de caractères.

# In[ ]:


print("Albert O'Connor")
print('Je lui ai dit "Salut!"')


# Certains opérateurs mathématiques ont été surchargés pour fonctionner avec des chaînes de caractères. Par exemple l'opérateur '**+**' concatène les strings et '**\***' les répète.

# In[ ]:


"Good" + " " + "Morning!"


# In[ ]:


"=" * 30


# #### Commentaires
# 
# *Python* ignore tout ce qui se trouve sur une ligne précédée du symbole #, ce qui permet de rajouter des commentaires à votre code ou d'en désactiver temporairement une partie.
# Si ce symbole est contenu dans une string, il est considéré comme un caractère normal et les caractères suivant ne sont pas ignorés.
# Prenez l'habitude de **toujours commenter votre code**, même si vous ne l'écrivez que pour vous. Quelques mots d'explications rendront votre code beaucoup plus lisible et vous feront gagner du temps lorsque vous y reviendrez plus tard.

# In[ ]:


# this is a comment and won't get evaluated
# a = 10
a = 15

a


# #### Exercice
# 
# Corrigez l'erreur dans l'affectation suivante et ajoutez un commentaire qui explique la modification faite et pourquoi.

# In[ ]:


welcome_message = "Buenos dias! "'


# ### Modules

# La plupart des fonctionnalités de *Python* sont fourni par des *modules* qui peuvent être importés afin de fournir des constantes, des fonctions, des classe, etc.
# *Python* contient de base une grande quantité de ces modules sous la dénomination de la **Python Standard Library**.
# Cette librairie fournit des outils pour manipuler des fichiers, des dossiers, lire des données, explorer du XML, etc.
# Par exemple le module *math* contient de nombreuses fonctions et constantes mathématique qui peuvent être utilisées une fois le module *importé*.

# In[ ]:


import math


# Nous pouvons maintenant utiliser la constante $\pi$

# In[ ]:


print(math.pi)


# Pour utiliser un élément d'un module, celui-ci doit être précédé du nom du module qui le défini.
# Afin d'éviter d'avoir à écrire le nom du module trop souvent, il est possible d'importer certains éléments du module dans l'espace de nom (*namespace*) local.

# In[ ]:


from math import pi, cos

cos(pi)


# Il est également possible d'importer tous les éléments d'un module en utilisant la commande suivante

# In[ ]:


from math import *

sin(pi / 2.0)


# L'avantage de cette approche est qu'elle permet d'utiliser toutes les fonctions et constantes du module *math* sans avoir à taper le préfixe "math".
# Le problème est que maintenant le namespace local contient tout un tas d'éléments qui ne sont pas forcément souhaités et surtout qui risquent d'entrer en conflit avec d'autres éléments définis auparavant.
# C'est pourquoi il est fortement conseillé d'utiliser plutôt une des deux premières méthodes.

# #### Exercice
# 
# Affectez à la variable `x` la valeur $\dfrac{3e}{\pi}$.
# Calculer l'expression suivante : $y=\sqrt{\log(7x^2+21x-cos(\dfrac{\pi}{4})}$

# In[ ]:





# #### Un peu d'aide ?

# Il existe plusieurs manières d'obtenir de l'aide ou de savoir ce qui est disponible sans pour autant avoir besoin de documentation extérieure ou de Google.
# La fonction intrinsèque *dir* affiche tous les éléments d'un module ou d'une classe et permet d'avoir un aperçu de ce qui est disponible.

# In[ ]:


print(dir(math))


# La fonction *help* est elle aussi très utile:

# In[ ]:


help(math)


# Ce Notebook est a été crée par David Da SILVA - 2020
# 
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
