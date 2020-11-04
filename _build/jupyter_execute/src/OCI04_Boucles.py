#!/usr/bin/env python
# coding: utf-8

# # Boucles en *Python*
# ---
# 
# Il existe 2 types de boucle en *Python*: le boucles `for` et les boucles `while`. Elles s'écrivent de la manière suivante :
# 
#     for variable1 in list:
#         # variable1 prend chacune des valeurs de la liste
#         code
# 
# et
# 
#     while test_est_True:
#         # Le code est répété tant que le test retourne True
#         code

# La commande `continue` permet de sauter certaines itérations au sein d'une boucle.
# Essayez de deviner le comportement de la boucle suivante avant de l'exécuter et notez le ici :
# 
# *what's your guess ?*
# 
# 

# ## Boucle `for`
# 
# Une boucle `for` va parcourir tous les éléments d'une séquence (quelque soit son type : liste, tuple, dictionnaire, ensemble, chaîne de caractères) et exécuter des instructions à chaque fois.  
# Par exemple, `range(20)` crée la séquence des entiers de 0 à 19 (la borne de fin est exclue).
# 
# On peut *itérer* sur chacune de ces valeurs et effectuer des opérations:

# In[ ]:


for i in range(20):
    print("Le cube de {0:>2} est {1:>4}".format(i, i**3))


# ### Itération
# 
# Une boucle `for` peut *itérer* sur une chaîne de caractère :

# In[ ]:


for x in "banana":
    print(x)


# sur une liste :

# In[ ]:


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


# sur une liste mixte :

# In[ ]:


for i in [4, 6, "asdf", "jkl"]:
    print(i)


# **Remarque** : Les opérations ne sont pas forcément en lien avec le compteur de la boucle.

# In[ ]:


A = 21
print(A)

for i in range(5):
    print("Hello")
    A += 2
    
print(A)


# #### Exercices
# 
# Changer le `print()` de la boucle ci-dessus afin que les éléments s'impriment tous de manière centrée sur une ligne de 30 caractères remplies de "=".
# 
# i.e. : "==============5==============="
# 
# **Indice**: utiliser le [formating mini-language](https://docs.python.org/2/library/string.html#format-specification-mini-language)

# In[ ]:


for i in [4, 6, "asdf", "jkl"]:
    print(i)


# In[ ]:


for i in [4, 6, "asdf", "jkl"]:
    print("{0:=^30}".format(i))


# Écrivez un programme qui affiche une suite de 12 nombres dont chaque terme est égal au triple du terme précédent

# In[ ]:





# Modifiez ce programme afin que ce soit l'utilisateur qui choisisse le première valeur

# In[ ]:





# ### Énumération
# 
# Un besoin assez courant quand on manipule une liste ou tout autre objet itérable est de récupérer en même temps l'élément et son indice à chaque itération.  
# Pour cela, la méthode habituellement utilisée est simple : au lieu d'itérer sur notre liste, on va itérer sur une liste d'entiers partant de 0 et allant de 1 en 1 jusqu'au dernier indice valide de la liste, obtenue via la fonction `range()`.  
# Cette méthode n'est pas du tout efficace : en effet, manipuler ainsi l'indice est totalement contre-intuitif et va à l'encontre du principe des itérateurs en Python.
# 
# Un exemple de code utilisant cette mauvaise méthode :

# In[ ]:


mylist = [4, 6, "asdf", "jkl"]

for indice in range(0, len(mylist)):
    print("mylist[%d] = %r" % (indice, mylist[indice])) #une autre manière de formater des chaînes de caractère


# Pour réaliser ce genre d'itérations, on va utiliser la fonction **`enumerate(iter)`**  
# Elle permet en effet de récupérer une liste de tuples `(indice, valeur)` en fonction du contenu de la séquence et d'une manière très pratique.  
# On l'utilise comme ceci :

# In[ ]:


for indice, valeur in enumerate(mylist):
    print("mylist[{0}] = {1}".format(indice, valeur)) #c'est ce mode de formatage qu'il faut préférer


# Cette manière de faire se rapproche beaucoup plus de ce qui doit être fait en *Python* si l'on veut utiliser correctement le langage : on itère directement sur les valeurs à la sortie d'un générateur, au lieu d'utiliser un indice (manière plus courante dans les langages comme le C n'ayant pas d'itérateurs comme ceux de *Python*).

# #### Exercice
# 
# Affichez chaque lettre du mot suivant suivi de sa position dans le mot : *supercalifragilisticexpialidocious*

# In[ ]:





# ## Boucle `while`
# 
# ### Définition
# 
# La boucle `while` ne parcourt pas de séquence, mais vérifie une condition à chaque tour. Si cette condition est vérifiée, les instructions du corps de la boucle sont effectuées. Dans le cas contraire, la boucle s'arrête et les instructions ne sont pas executées.

# In[ ]:


i = 0
while i < 20:
    print("Le cube de {0:>2} est {1:>4}".format(i, i**3))
    i = i+1


# **Attention** : Une boucle `while` dont la condition est toujours vérifiée ne s'arrêtera jamais. On parle de boucle infinie. C'est une erreur classique qui peut avoir des erreurs dramatiques, programme ne s'arrête pas, saturation de la mémoire, crash...

# In[ ]:


#Si vous exécutez la boucle ci-dessous, il vous faudra appuyer sur le bouton Stop ( à droite de >| Run)
#avant de pouvoir continuer à travailler
i = 1
while i > 0:
    print("Le cube de {0:>2} est {1:>4}".format(i, i**3))
    i = i + 1


# ### Exercices
# 
# Utilisez une boucle `while` pour afficher tous les multiples de 21 inférieurs à 2538

# In[ ]:





# Écrivez un programme qui affiche chaque lettre du mot *supercalifragilisticexpialidocious* précédant la lettre *x*.

# In[ ]:





# ### Exercice
# 
# Écrivez un programme qui demande à l'utilisateur un nombre compris entre 21 et 42 jusqu'à ce que la réponse convienne en l'aiguillant (trop grand, trop petit...)

# In[ ]:





# ## `break` et `continue`
# 
# Parfois il est nécessaire de sortir d'une boucle avant la fin de son exécution. 
# Dans ces cas là, il faut utiliser le mot clé `break` qui fonctionne pour les 2 types de boucle `for` et `while`.
# 
# Par exemple, `while True:` crée une boucle infinie pusique le test est toujours vrai, mais l'instruction `break` permet d'en sortir :

# In[ ]:


i = 0
while True:
    i = i + 10
    if i > 95:
        break
print(i)


# La commande `continue` permet de sauter certaines itérations au sein d'une boucle.  
# Essayez de deviner le comportement de la boucle suivante avant de l'exécuter et notez le ici :

# *what's your guess ?*

# In[ ]:


for x in range(30):
    if x%3!=0:
        continue
    print(x)


# ## `for` vs. `while`
# 
# ### Questions
# 
# 1. Quelles sonts les différences que vous notez entre les 2 types de boucle
# 2. Selon vous y a-t-il un boucle plus rapide que l'autre ? Pourquoi ?
# 

# __Vos réponses ici__

# ### Testons
# 
# Le module `time` founit la fonction `time()` qui renvoit le temps courant depuis [`Epoch`](https://en.wikipedia.org/wiki/Epoch_%28reference_date%29#Computing).  
# En utilisant cette fonction, calculer la temps mis pour calculer les carrés des chiffres de $0 \text{ à } 10^7$ avec une boucle `for` et une boucle `while`.
# 
# **Conseil :** éviter de faire un `print` pour chaque ligne de calcul...
# 
# Au fait, quel est le `Epoch` de *Python* ?

# In[ ]:


import time

start = time.time()
#code de la boucle à évaluer
stop = time.time()

print(stop-start)


# Ce Notebook est a été crée par David Da SILVA - 2020
# 
# Source: [openclassrooms.com](https://openclassrooms.com/courses/pratiques-avancees-et-meconnues-en-python)
# 
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
