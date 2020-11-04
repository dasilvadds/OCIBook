#!/usr/bin/env python
# coding: utf-8

# # Booléens et tests
# ---

# ## Vrai ou Faux
# 
# En plus des différents types déjà vus, il existe un type un peu particulier appelé **Booléens** qui prend uniquement 2 valeurs, **vrai** ou **faux**.
# En *Python* un booléen est soit **`True`** soit **`False`**.
# Les booléens servent à donner le résultat d'une comparaison entre 2 objets.
# *Python* permet de comparer 2 objets de plusieurs manières :
# 
# * `A==B`: est-ce que `A` est égal à `B`?
# * `A!=B`: est-ce que `A` est différent de `B`?
# * `A>B`, `A>=B`, `A<B`, `A<=B`: est-ce que `A` est plus grand, plus grand ou égal, plus petit, plus petit ou égal à `B`?
# * `A is B`: est-ce que `A` est le même objet que `B` ? (pas uniquement sa valeur)
# * `A in B`: est-ce que `B` contient `A` ? (si `B` est un container comme une liste par exemple)

# In[ ]:


9**2 == 10+8*10-9


# In[ ]:


[1,2,3]==[1,2,3]


# In[ ]:


[1,2,3]==[1,3,2]


# In[ ]:


3.0 in ['Yay!', 'Python', 3.0]


# Ces tests peuvent être combinés entre eux en utilisant des opérateurs logiques.

# In[ ]:


A = 30

( A >10 ) or ( A%3==0 )


# ## Opérations et transformation 
# 
# Les opérateurs logique opèrent sur des booléens et renvoient des booléens en fonction de leurs tables.
# Il existe 2 opérations, **ET** et **OU** et 1 transformation appelée **contraire**.
# 
# Les tables sont les suivantes:
# 
# `and`|`True`|`False`
# ---|---|---
# **`True`**|`True`|`False`
# **`False`**|`False`|`False`
# 
# `or`|`True`|`False`
# ---|---|---
# **`True`**|`True`|`True`
# **`False`**|`True`|`False`
# 
# -|`not`
# ---|---
# **`True`**|`False`
# **`False`**|`True`
# 
# En *Python* ces opérateurs sont notés **`and`**, **`or`** et **`not`** et les résultats des tables peuvent être obtenus en appliquant les fonctions sur des booléens.

# In[ ]:


print(True and False)
print(False or True)
print(not False)


# ## Table de vérité
# 
# Une table de vérité est une table mathématique utilisée en logique pour représenter de manière sémantique des expressions logiques et calculer la valeur de leur fonction relativement à chaque combinaison de valeur assumée par leurs variables logiques. 
# 
# Les tables de vérité peuvent être utilisées en particulier pour dire si une proposition est vraie pour toutes les valeurs légitimement imputées.

# Considérons les 2 variables `A` et `B`, et pour simplifier la lecture nous associerons la valeur 0 à `False` et la valeur 1 à `True`.
# 
# Les tables de vérité pour les 3 opérateurs s'écrivent :
# 
# `A`|`B`|`not A`|`not B`|`A and B`|`A or B`
# ---|---|:---:|:---:|:---:|:---:
# 0|0|1|1|0|0
# 0|1|1|0|0|1
# 1|0|0|1|0|1
# 1|1|0|0|1|1

# ### Exercice
# 
# En utilisant `Python` pour faire les tests, remplissez la table de vérité suivante, et conservez **tous** les blocs de code `Python` que vous avez utilisé.
# 
# `A`|`B`|`not (A and B)`|`(not B) or (not A)`
# ---|---|:---:|:---:
# 0|0|?|?
# 0|1|?|?
# 1|0|1|?
# 1|1|?|?

# In[ ]:


A = True
B = False


# In[ ]:


not (A and B)


# ### Questions
# 
# Que remarquez-vous ?
# 
# Quelle relation pensez-vous qu'il y ait entre `not(A or B)` et `(not A) and (not B)` ?
# 
# Connaissez-vous les lois de [*De Morgan*](https://fr.wikipedia.org/wiki/Lois_de_De_Morgan)?

# *Vos réponses ici*

# ## Bloc de test
# 
# Une particularité de *Python* est l'utilisation des indentation afin de rassembler des informations au sein d'un bloc.
# Les indentations dans *Python* remplace les accolades **{ }** dans d'autres langages tels que **C++**.
# 
# Afin de définir un bloc de code en *Python* comme pour les tests, les fonctions ou les boucles, il faut utiliser le double point **:** suivi d'un niveau d'indentation.
# 
# Voyons par exemple la structure d'un bloc conditionnel de type *SI...ALORS...SINON* qui se traduit en *Python* par les commandes `if` et `else`.
# 
#     if A==B:
#       # les instructions de ce bloc sont exécutées
#       # si A est égal à B
#     else:
#       # sinon ce sont les instructions de ce bloc
#       # qui seront exécutées
# 
# Un bloc conditionnel de manière général possède la structure légèrement plus complexe suivante:
# 
#     if A==B:
#       # les instructions de ce bloc sont exécutées
#       # si A est égal à B
#     elif A==C:
#       # celles de ce bloc sont exécutées
#       # si A est égal C  
#       # ET si le premier test est faux (renvoi False)
#     elif test2:
#       # celles de ce bloc sont exécutées
#       # si test2 est vrai (renvoi True)  
#       # ET si les deux premiers tests sont faux (renvoi False)
#     
#     .
#     .
#     .
#     
#     else:
#         # finalement ces instructions sont exécutées si 
#         # aucun des tests précédents n'est vérifié
# 
# Il peut y avoir autant de `elif` que vous voulez mais il ne peut y avoir qu'un seul `else` ( c'est un Highlander! ) 
# 
# Tous les `elif` ainsi que le `else` peuvent être omis.
# 
# Modifiez les valeurs de `A` dans le code suivant et observez ce qui se passe.

# In[ ]:


A = 15

if A > 9:
    print("A est plus grand que 9")
elif A > 4:
    print("A est compris entre 5 et 9")
else:
    print("A est plus petit que 5")
    


# ### Exercice
# 
# Créez un test afin de déterminer si un nombre est un carré (i.e 1, 4, 9, 16, ...), et créez un bloc conditionnel qui affiche soit "carré" soit "pas un carré" en fonction du résultat du test.
# 
# *Indice* : `int(d)` retourne la partie entière du nombre décimal `d`.
# 
# Testez votre bloc pour différentes valeurs.

# In[ ]:





# ## Interraction avec l'utilisateur
# 
# Afin de rendre vos script un peu plus interractifs, il est possible de demander à python d'utiliser une entrée clavier pour l'utiliser ensuite dans votre script.
# 
# La commande à utiliser est `input()`. Elle provoque l'ouverture d'un champ dans lequel l'utilisateur doit rentrer une donnée au clavier et attend l'appui de la touche `Entrée`.
# 
# ### Exemple

# In[ ]:


A = 20
toto = input()
print("Vous avez saisie : {0} et A vaut {1} ".format(toto,A))


# La fonction `input()` peut contenir un paramètre qui sera affiché devant la fenêtre de saisie

# In[ ]:


import sys
reload(sys)
sys.setdefaultencoding("utf-8")


# In[ ]:


yr = input("Quel est votre année de naissance ?")
print("Je devine que vous avez environ {0} ans ! \nJe suis fort hein !?!".format(2020-int(yr)))


# ### Exercices
# 
# * Écrivez un programme qui demande un nombre à l'utilisateur, puis calcule et affiche le carré de ce nombre

# In[ ]:





# * Écrivez un programme qui demande un nombre à l'utilisateur et l'informe ensuite si ce nombre est pair ou impair 

# In[ ]:





# * Écrivez un programme qui demande l'âge d'une personne et affiche ensuite sa catégorie :
#     1. "Poussin" de 6 à 7 ans
#     2. "Pupille" de 8 à 9 ans
#     3. "Minime" de 10 à 11 ans
#     4. "Cadet" après 12 ans
#     5. "Junior" après 16 ans
#     6. "Senior" après 18 ans

# In[ ]:





# Ce Notebook est a été crée par David Da SILVA - 2020
# 
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
