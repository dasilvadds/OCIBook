#!/usr/bin/env python
# coding: utf-8

# # Les listes en *Python*
# ---

# ## Définition et instanciation
# 
# La liste en *Python* (`List`) est le type de données le plus flexible.  
# C'est une séquence d'éléments, qui peut être modifiée (suppression/ajout) et découpée (`Slice`).  
# 
# Les listes en *Python* sont définies en utilisant des crochets [ ] et en plaçant des éléments à l'intérieur qui sont séparés par des virgules.  
# Les éléments de la liste sont indexés (`index`) de gauche à droite, le premier index vaut 0.
# 
# **Attention** : Les *listes* définies à l'aide de parenthèses sont appelées des `tuples` et leur contenu n'est pas modifiable.

# In[ ]:


weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]


# ## Accéder aux éléments d'une liste
# 
# Pour accéder à un élément en particulier de la liste on peut utiliser son index (le numéro de sa place dans la liste) noté entre [ ].  
# **Attention :** en *Python* les index commence à 0. Le premier élément de la liste s'obtient donc avec la notation `maliste[0]`.

# In[ ]:


print( weekdays[3] )


# ### Index négatifs
# 
# Vous pouvez également parcourir les éléments de la liste en commençant par la fin en utilisant des index négatifs.
# Le dernier élément se trouve à l'index -1, l'avant dernier à l'index -2, etc.

# In[ ]:


weekend = [ weekdays[-2], weekdays[-1] ]
print(weekend)


# ### Sous-liste | `slicing`
# Pour extraire une *tranche* de la liste on utilise le symbole __:__ qui séparent l'index de début et l'index de fin.  
# **Attention :** l'élément à l'index de fin est exclu de la liste ( i.e. [*index_début ; index_fin*[ )

# In[ ]:


weekdays[0:5]


# #### Exercice
# 
# Créez une sous-liste allant de la fraise au kiwi

# In[ ]:


fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]


# In[ ]:


sublist = fruitlist[2:5]
print(sublist)


# #### Remarques
# Si l'index de début est omis, la *tranche* commencera au début de la liste. Si c'est l'index de fin qui est absent, la *tranche* finira à la fin de la liste.  
# Une *tranche* peut également être définie avec des index négatifs.
# 
# #### Exercice
# 
# Créez la même sous-liste que précédement allant de la fraise au kiwi, mais cet fois avec des index négatifs

# In[ ]:





# ### Listes imbriquées
# 
# Les listes ne sont pas forcément constituées d'éléments de même type. Vous pouvez faire tous les mélanges que vous voulez y compris mettre imbriquer des listes dans des listes ou des tuples dans des tuple et vice versa.

# In[ ]:


mixedlist = [ 1.0, 100, "Elephant", ("mouse", "rat"), weekend ]
mixedlist


# Pour accéder aux éléments imbriqués on utilise autant de niveaux de [ ] qu'il y a de niveaux d'imbriquation.
# Par exemple pour accéder au premier élément de la liste `weekend` imbriquée dans `mixedlist` on utilisera la notation suivante :

# In[ ]:


mixedlist[-1][0]


# ## Modification de liste
# 
# Les listes ont de nombreuses méthodes utiles qui sont prédéfinies comme par exemple pour ajouter ou supprimer des éléments.
# Des explications concises sont accessibles via la commande `help(list)`. 
# Ignorez les méthodes qui commencent par un underscore ( \_ ) ; ces méthodes sont utilisées pour définir des opérations internes comme l'initialisation d'une liste, les surcharges d'opérateurs, etc.

# ### Modification d'un élément
# 
# Il est possible de modifier un élément d'une liste en y accédant par son `index`.

# In[ ]:


fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruitlist[3] = "kumquat"
print(fruitlist)


# #### Exercice
# Modifiez *Wednesday* dans la liste `weekdays` en *Mercredi*.

# In[ ]:





# Modifiez le deuxième élément de la liste `weekend` imbriquée dans `mixedlist` pour **Samedi**

# In[ ]:


mixedlist = [ 1.0, 100, "Elephant", ("mouse", "rat"), weekend ]


# In[ ]:


mixedlist[4][1] = "Samedi"
print(mixedlist)


# ### Ajout d'un élément
# 
# #### En fin de liste
# La méthode **`append(x)`** ajoute l'élément *x* en fin de liste.

# In[ ]:


fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruitlist.append("kumquat")
print(fruitlist)


# #### À un endroit spécifique
# 
# La méthode **`insert(idx, x)`** insère l'élément *x* à l'`index` *idx*.

# In[ ]:


fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruitlist.insert(2,"kumquat")
print(fruitlist)


# #### Concaténation de listes
# 
# Il y a plusieurs façons de concaténer 2 listes ou plus. La méthode la plus simple est sûrement l'utilisation de l'opérateur `+`.

# In[ ]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# On peut également utiliser la méthode **`extend(iter)`** et qui va rajouter les éléments d'une liste (ou une autre structure itérable) à une autre liste.

# In[ ]:


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# #### Exercices
# 
# 1. Ajoutez le papmplemousse (en anglais) à la fin de `fruitlist`.
# 2. Insérez le citron (toujours en anglais) entre l'orange et le kiwi.
# 3. Supprimez le **melon** de la liste.
# 4. Imprimez l'avant-dernier élément de la liste en utilisant un index négatif.
# 5. Créez une nouvelle liste `fruitday` qui est la concaténation de `weekdays` et `fruitlist`.

# In[ ]:





# ### Suppression
# 
# #### Supprimer un élément spécifique
# 
# La méthode **`remove(elmt)`** supprime l'élément *elmt*.  

# In[ ]:


fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruitlist.remove("orange")
print(fruitlist)


# #### Supprimer selon une position
# 
# La méthode **`pop(idx)`** supprime l'élément se trouvant à la position *idx* et le retourne (`return`).  
# Si *idx* n'est pas précisé, `pop()` supprime et retourne le dernier élément de la liste.

# In[ ]:


fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruit = fruitlist.pop(3)
print(fruit)
print(fruitlist)

lastfruit = fruitlist.pop()
print(lastfruit)
print(fruitlist)


# #### Effacement
# 
# Le mot clé `del` peut aussi être utilisé pour effacer un élément dont l'`index` est connu.

# In[ ]:


fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
del fruitlist[2]
print(fruitlist)


# **Attention** : le mot clé `del` efface aussi le contenu d'une variable.

# In[ ]:


fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
del fruitlist
print(fruitlist)


# Pour vider le contenu d'une liste, il faut utiliser la méthode **`clear()`**.

# In[ ]:


fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruitlist.clear()
print(fruitlist)


# In[ ]:





# #### Exercice
# 
# Créez une nouvelle liste `monovowelfruit` dans laquelle vous déplacerez les fruits de `fruitlist` dont le nom ne possède pas 2 voyelles différentes. Ces fruits ayant été déplacés, ils ne seront plus dans `fruitlist`.

# In[ ]:


fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]



print(fruitlist)


# ### Copier une liste
# 
# L'affectation d'une liste existante à une nouvelle variable (`fruitcopy = fruitlist`) ne créé pas une copie de la liste, mais créé une référence. Toutes modifications de la liste initiale affectera la référence.

# In[ ]:


fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruitcopy = fruitlist

fruitlist[3] = "peach"

print(fruitcopy)


# Pour créer une copie on peut utiliser la méthode **`copy()`** qui va générer une copie de la liste.

# In[ ]:


fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruitcopy = fruitlist.copy()

fruitlist[3] = "peach"

print(fruitcopy)


# On peut également utiliser le *constructeur* de listes : **`list(elmt)`**, qui créer une liste à partir de `elmt`.

# In[ ]:


fruitlist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruitcopy = list(fruitlist)

fruitlist[2] = "peach"

print(fruitcopy)


# ## Méthodes de liste
# 
# Complétez les descriptions des méthodes suivantes.  
# Pour celles que vous ne connaissez pas, utilisez la fonction `help` afin de truover une description, puis essayez de les utiliser dans des exemples.
# 
# |Méthode|Description|
# |----|----|
# |append()| |
# |clear()| |
# |copy()| |
# |count()| |
# |extend()| |
# |index()| |
# |insert()| |
# |pop()| |
# |remove()| |
# |reverse()| |
# |sort()| |
# 

# In[ ]:





# **Besoin d'aide ?** : par [ici](https://www.tutorialspoint.com/python3/python_lists.htm)

# ## Fonctions supplémentaires
# 
# ### `len()`
# 
# Il existe des fonctions prédifinies qui peuvent opérer sur les liste telles que la fonction **`len`** qui permet d'obtenir la taille d'une liste.

# In[ ]:


len(fruitlist)


# ####  Exercice
# 
# Imprimez le dernier élément de la liste `weekdays` en utilisant la fonction `len` (pas d'index négatif).

# In[ ]:





# Pourquoi la commande `weekdays[len(weekdays)]` ne fonctionne-t-elle pas ?

# __votre réponse ici__

# ### `range()`
# 
# Une commande très utile pour générer des séquences de nombres : **`range`**.
# Cette fonction peut prendre 1, 2 ou 3 paramètres.
# 
# Avec 1 paramètre elle permet de générer la liste des entiers inférieurs au paramètre.

# In[ ]:


list(range(10))


# Avec 2 paramètres vous spécifiez la valeur de début et celle de fin (non inclue).

# In[ ]:


list(range(2,10))


# Avec 3 paramètres vous spécifiez la valeur de début, de fin et le pas.

# In[ ]:


list(range(2,10,2))


# Cette commande est particulièremet utile pour les *boucles* que nous aborderons par la suite.

# #### Exercices
# 
# Utilisez la fonction `range()` pour générer la liste de tous les multiples de 7 inférieurs 4103. 

# In[ ]:





# En utilisant des listes imbriquées, créez une structure pour représenter la matrice 3x3 suivante : $A=\begin{pmatrix}1&4&7\\2&5&8\\3&6&9\end{pmatrix}$. 
# Vos imbrications de listes devront permettre à la commande `A[l][c]` d'accéder à l'élément se trouvant à la ligne `l` et la colonne `c` ; e.g. `A[1][2]=8` et `A[2][0]=3` (Attention les index commencent à 0).

# In[ ]:


A = [[1,4,7],[2,5,8],[3,6,9]]
print(A)
print(A[1][2])
print(A[2][0])


# In[ ]:





# Ce Notebook est a été crée par David Da SILVA - 2020
# 
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
