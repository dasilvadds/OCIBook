#!/usr/bin/env python
# coding: utf-8

# ## 10 - Dictionnaire en *Python*
# ---
# 
# Vincent Le Goff - [OpenClassRoom](https://openclassrooms.com/courses/apprenez-a-programmer-en-python/les-dictionnaires-2)
# 
# Les dictionnaires sont des objets pouvant en contenir d'autres, à l'instar des listes. Cependant, au lieu d'héberger des informations dans un ordre précis, ils associent chaque objet contenu à une clé (la plupart du temps, une chaîne de caractères). Par exemple, un dictionnaire peut contenir un carnet d'adresses et on accède à chaque contact en précisant son nom.
# 
# ### 10.1 - Création et édition de dictionnaire
# 
# Un dictionnaire est un type de données extrêmement puissant et pratique. Il se rapproche des listes sur certains points mais, sur beaucoup d'autres, il en diffère totalement.
# Les objets de ce type sont des objets conteneurs, dans lesquels on trouve d'autres objets. Pour accéder à ces objets contenus, il faut connaître leur position dans la liste. Cette position se traduit par des entiers, appelés indices, compris entre 0 (inclus) et la taille de la liste (non incluse).
# Le dictionnaire est aussi un objet conteneur. Il n'a quant à lui aucune structure ordonnée, à la différence des listes. De plus, pour accéder aux objets contenus dans le dictionnaire, on n'utilise pas nécessairement des indices mais des clés qui peuvent être de bien des types distincts.
# 
# Voici la première méthode d'instanciation d'un dictionnaire :

# In[ ]:


mon_dictionnaire = dict()
type(mon_dictionnaire)


# In[ ]:


mon_dictionnaire


# Les parenthèses délimitent les tuples, les crochets délimitent les listes et les accolades `{}` délimitent les dictionnaires. Par conséquent, la seconde méthode d'instanciation d'un dictionnaire est évidemment :

# In[ ]:


mon_dictionnaire = {}
mon_dictionnaire


# Voici comment ajouter des clés et valeurs dans notre dictionnaire vide :

# In[ ]:


mon_dictionnaire = {}
mon_dictionnaire["pseudo"] = "Prolixe"
mon_dictionnaire["mot de passe"] = "*"
mon_dictionnaire


# La clé à laquelle nous souhaitons accéder est indiquée entre crochets. 
# Si la clé n'existe pas, elle est ajoutée au dictionnaire avec la valeur spécifiée après le signe `=`.
# Sinon, l'ancienne valeur à l'emplacement indiqué est remplacée par la nouvelle :

# In[ ]:


mon_dictionnaire = {}
mon_dictionnaire["pseudo"] = "Prolixe"
mon_dictionnaire["mot de passe"] = "*"
mon_dictionnaire["pseudo"] = "6pri1"
mon_dictionnaire


# C'est assez similaire à la création de variables : si la variable n'existe pas, elle est créée, sinon elle est remplacée par la nouvelle valeur.
# 
# Pour accéder à la valeur d'une clé précise, c'est très simple :

# In[ ]:


mon_dictionnaire["mot de passe"]


# Si la clé n'existe pas dans le dictionnaire, une exception de type KeyError sera levée.

# In[ ]:


mon_dictionnaire["toto"]


# On peut aussi créer des dictionnaires déjà remplis.
# On précise entre accolades la clé, le signe deux points **`:`** et la valeur correspondante. On sépare les différents couples clé : valeur par une virgule. C'est d'ailleurs comme cela que Python vous affiche un dictionnaire quand vous le lui demandez.

# In[ ]:


placard = {"chemise":8, "pantalon":6, "tee-shirt":7}
placard


# Généralisons un peu tout cela : nous avons des dictionnaires, qui peuvent contenir d'autres objets. On place ces objets et on y accède grâce à des clés. Un dictionnaire ne peut naturellement pas contenir deux clés identiques (comme on l'a vu, la seconde valeur écrase la première). En revanche, rien n'empêche d'avoir deux valeurs identiques dans le dictionnaire.
# 
# Nous avons utilisé ici, pour nos clés et nos valeurs, des chaînes de caractères. Ce n'est absolument pas obligatoire. Comme avec les listes, vous pouvez utiliser des entiers comme clés :

# In[ ]:


mon_dictionnaire = {}
mon_dictionnaire[0] = "a"
mon_dictionnaire[1] = "e"
mon_dictionnaire[2] = "i"
mon_dictionnaire[3] = "o"
mon_dictionnaire[4] = "u"
mon_dictionnaire[5] = "y"
mon_dictionnaire


# On a l'impression de recréer le fonctionnement d'une liste mais ce n'est pas le cas : rappelez-vous qu'un dictionnaire n'a pas de structure ordonnée. Si vous supprimez par exemple l'indice 2, le dictionnaire, contrairement aux listes, ne va pas décaler toutes les clés d'indice supérieur à l'indice supprimé. Il n'a pas été conçu pour.
# 
# **On peut utiliser quasiment tous les types comme clés et on peut utiliser absolument tous les types comme valeurs.**

# ### 10.2 - Supprimer des clés d'un dictionnaire
# 
# Comme pour les listes, vous avez deux possibilités mais elles reviennent sensiblement au même :
# 
# * le mot-clé `del`
# * la méthode de dictionnaire `pop`
# 
# Ils fonctionnent pratiquement dde la même manière que pour les listes, i.e. la méthode `pop` renvoie la valeur de la clé supprimée :

# In[ ]:


placard = {"chemise":3, "pantalon":6, "tee shirt":7}
del placard["chemise"]


# In[ ]:


placard = {"chemise":3, "pantalon":6, "tee shirt":7}
placard.pop("chemise")


# ### 10.3 - Les méthodes de parcours
# 
# Comme vous pouvez le penser, le parcours d'un dictionnaire ne s'effectue pas tout à fait comme celui d'une liste. La différence n'est pas si énorme que cela mais, la plupart du temps, on passe par des méthodes de dictionnaire.
# 
# #### Parcours des clés
# 
# On peut parcourir un dictionnaire comme on l'a fait pour les listes :

# In[ ]:


fruits = {"pommes":21, "melons":3, "poires":31}

for x in fruits:
    print(x)


# Comme vous le voyez, si on parcour un dictionnaire *simplement*, on parcourt en réalité la liste des clés contenues dans le dictionnaire.
# 
# **Attention : Les dictionnaires n'ont pas de structure ordonnée, par conséquent les clés ne s'affichent pas dans l'ordre dans lequel on les a entrées**.

# La méthode `keys` (*clés* en anglais) renvoie la liste des clés contenues dans le dictionnaire et permet de parcourir le dictionnaire de la même manière (la lecture de l'instruction est juste plus explicite).

# In[ ]:


for x in fruits.keys():
    print x


# #### Exercice
# En utilisant la méthode `sort` qui trie les `list`, réalisez un parcours ordonné des clés de votre dictionnaire.

# In[ ]:





# #### Parcours des valeurs
# 
# On peut aussi parcourir les valeurs contenues dans un dictionnaire. Pour ce faire, on utilise la méthode `values` ( *valeurs* en anglais).

# In[ ]:


fruits = {"pommes":21, "melons":3, "poires":31}

for valeur in fruits.values():
    print(valeur)


# Cette méthode est peu utilisée pour un parcours car il est plus pratique de parcourir la liste des clés, cela suffit pour avoir les valeurs correspondantes. Mais on peut aussi, bien entendu, l'utiliser dans une condition :

# In[ ]:


if 21 in fruits.values():
    print("Un des fruits se trouve en quantité 21.")


# #### Parcours des clés et valeurs simultanément
# 
# Pour avoir en même temps les indices et les objets d'une liste, on utilise la fonction `enumerate`.
# Pour faire de même avec les dictionnaires, on utilise la méthode `items`. 
# Elle renvoie une liste, contenant les couples `clé : valeur`, sous la forme d'un tuple. 
# Voici comment l'utiliser :

# In[ ]:


fruits = {"pommes":21, "melons":3, "poires":31}
for cle, valeur in fruits.items(): 
    print("La clé {} contient la valeur {}.".format(cle, valeur))


# ### En résumé
# 
# * Un dictionnaire est un objet conteneur associant des clés à des valeurs.
# * Pour créer un dictionnaire, on utilise la syntaxe `dictionnaire = {cle1:valeur1, cle2:valeur2, cleN:valeurN}`.
# * On peut ajouter ou remplacer un élément dans un dictionnaire : `dictionnaire[cle] = valeur`.
# * On peut supprimer une clé (et sa valeur correspondante) d'un dictionnaire en utilisant, au choix, le mot-clé `del` ou la méthode `pop`.
# * On peut parcourir un dictionnaire grâce aux méthodes `keys` (parcourt les clés), `values` (parcourt les valeurs) ou `items` (parcourt les couples clé-valeur).

# #### Exercice
# 
# Vous possédez un stock de fruits qui est répertorié dans le dictionnaire `fruits` ci-dessus.
# 
# Créez un dictionnaire `prix` qui contiendra les prix unitaires des fruits que vous avez en stock avec les valeurs suivantes :
# 
# * pommes : 0.75
# * melons : 3.5
# * poires : 1
# 
# Écrivez une fonction qui parcourt vos 2 dictionnaires et affiche pour chaque fruit, son nom, son prix et sa quantité en stock sous la forme suivante:
# > Pommes
# 
# >Prix : 0.75 CHF
# 
# >Stock : 21

# In[ ]:





# Écrivez une fonction qui calcule et affiche le chiffre d'affaire potentiel dans le cas ou vous vendriez tous vos fruits.

# In[ ]:




