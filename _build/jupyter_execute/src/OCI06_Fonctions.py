#!/usr/bin/env python
# coding: utf-8

# # Fonctions
# ---
# 
# Une fonction permet de rassembler un ensemble d'instructions, de *code*, afin de pouvoir le réutiliser à loisir.
# En effet, il est important de noter que le code d'une fonction n'est pas exécuté au moment de sa définition, mais lorsque celle-ci est *appelée*.

# ## Définition et *appel* d'une fonction
# 
# Une fonction en *Python* est définie à l'aide du mot clé **`def`**, suivi du **nom** de la fonction, de parenthèses **( )**, et d'un double point **:**.
# Le **corps** de la fonction est constitué de toutes les instructions qui suivent avec un niveau suplémentaire d'indentation (s'obtient avec la touche `Tab`).
# 
# L'exemple suivant défini la fonction **fonction1** qui écrit *Hello World !* à chaque fois qu'elle est executée.

# In[1]:


def fonction1():
    print("Hello World !")


# Afin d'exécuter le *code* d'une fonction il faut l'*appeler*. Il suffit d'écrire le *nom* de la fonction suivie de parenthèses ().

# In[2]:


fonction1()


# Vous pouvez *appeler* la fonction autant de fois que vous souhaitez, chaque *appel* exécute à nouveau le *code* 

# In[3]:


fonction1()
fonction1()
fonction1()


# ### Exercice 1
# 
# Écrivez la fonction appelée `HHGTTG` qui vous affiche la réponse à [La grande question sur la vie, l'univers et le reste](https://fr.wikipedia.org/wiki/La_grande_question_sur_la_vie,_l'univers_et_le_reste)

# In[ ]:





# ## Signature
# 
# La signature inclut le nom de la fonction et le nombre de paramètres qu'elle requiert en les nommant.
# 
# La fonction suivante prend 2 paramètres, `x` et `y` et affiche leur somme:

# In[4]:


def masomme(x, y):
    print("La somme de {0} et {1} est : {2}".format(x, y, x+y))
    
masomme(40,2)
masomme(55,-13)


# Les paramètres lors de l'appel d'une fonction sont affectés dans l'ordre définit dans la signature de la fonction. *Python* permet que cet ordre soit changé à condition que les paramètres soient nommés de manière explicite lors de l'appel de la fonction. 

# In[5]:


masomme(y=-13, x=55)


# Que se passe-t-il si vous appelez la fonction `masomme` avec un seul paramètre ?

# In[ ]:





# ### Exercice 2
# 
# En utilisant le test crée à l'exercice 4.1 du [Notebook sur les tests](./OCI03_Booleans_IfBlock.ipynb), créez la fonction `testSqrt` qui prend une valeur en paramètre et affiche s'il s'agit d'un carré parfait ou non. 

# In[ ]:





# ## Valeurs par défaut
# 
# Les paramètres d'une fonctions peuvent avoir une valeur par défaut et deviennent dans ce cas des paramètres optionnels, par opposition aux paramètres sans valeur par défaut qui sont, eux, des paramètres obligatoires.
# 
# Les paramètres optionnels sont listés impérativement **après** les paramètres obligatoires dans la signature d'une fonction.
# 
# Si la valeur d'un paramètre optionnel n'est pas spécifié lors de l'appel de la fonction, la valeur par défaut est alors utilisée.

# In[6]:


def masomme2(x, y=5):
    print("La somme de {0} et {1} est : {2}".format(x, y, x+y))

masomme2(21,21)
masomme2(37)


# ### Exercice 3
# 
# * Créez la fonction `madiv` qui prend 2 paramètres, `a` et `b` et affiche le quotient de `a` par `b` ($\frac{a}{b}$) 
# * Assurez vous que le résultat affiché est toujours celui de la division décimale indépendamment du type des paramètres, i.e. `madiv(1,2)` doit afficher 0.5
# * Gérez le cas où `b = 0`

# In[ ]:





# ## *docstrings*
# 
# De manière optionnelle, mais **très fortement recommendée**, il est possible de définir un *docstring*. Un *docstring* est une description de la fonction en termes de but, de paramètres et de comportement.
# 
# Le *docstring* doit être positionné après la signature de la fonction et avant son *code*, il est en principe situé entre des triples double quote (""" *docstring* """) qui permettent de faire des commentaires multilignes lorsqu'ils sont utilisés ailleurs.

# In[7]:


def masomme3(x, y):
    """
    Affiche la somme des 2 paramètres x et y. 
    """
    print("La somme de {0} et {1} est : {2}".format(x, y, x+y))


# Le *docstring* constitue l'aide qui est affiché lorsque vous utilisez la fonction `help` ou le `?`.

# In[8]:


help(masomme3)


# In[9]:


get_ipython().run_line_magic('pinfo', 'masomme3')


# ### Exercice 4
# 
# Ajoutez un *docstring* à votre fonction `madiv` de l'exercice 3 qui explique comment vous vous assurez que le résultat affiché est toujours celui de la division décimale et comment vous gérez le cas `b = 0` 

# In[ ]:





# ### Exercice 5
# 
# La suite de Fibonacci est une suite de nombre entier définie de la manière suivante:
# * $F(0) = 0$
# * $F(1) = 1$
# * $\forall n > 1, \; F(n) = F(n-1) + F(n-2)$
# 
# Les premiers éléments sont : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169].
# 
# Créez une fonction qui prend en paramètre un entier n et retourne les n+1 premiers éléments de la suite de Fibonacci.

# In[ ]:





# ## Retours
# 
# En principe les fonctions ne servent pas qu'à afficher des résultats, mais plutôt à en fournir afin d'être utilisé dans la suite du déroulement d'un programme.
# 
# Afin de fournir des résultats, les fonctions peuvent renvoyer quelque chose, on parle du ou des *retours* d'une fonction, qui peuvent être assignés à des variables ou passés en paramètre à d'autres fonctions, etc.
# 
# Ces *retours* se font à l'aide du mot clé `return` qui précède les éléments *retournés* par la fonction. 

# In[10]:


def masomme4(x, y):
    """
    Renvoie la somme des 2 paramètres x et y. 
    """
    z = x+y
    return z


# In[11]:


masomme4(11,31) #Notez la présence du Out[] après l'exécution


# In[12]:


a = masomme4(9,12)
print(a)
print(a*2)


# **Attention : ** l'exécution de la commande `return` achève l'exécution du corps de la fonction.

# In[13]:


def masomme5(x, y):
    """
    Renvoie la somme des 2 paramètres x et y. 
    """
    z=x+y
    return z
    print("La somme de {0} et {1} est : {2}".format(x, y, x+y))


# In[14]:


masomme5(31,11)


# ### Exercice 6
# 
# Créez la fonction `square` qui renvoie le carré de la valeur passée en paramètre. N'oubliez pas le *docstring* !

# In[ ]:





# Une fonction peut renvoyer plusieurs éléments en même temps, il suffit qu'ils soient séparés par des virgules **( , )** après le mot clé `return`.

# In[15]:


def masomme6(x, y):
    """
    Renvoie les 2 paramètres x et y ainsi que leur somme. 
    """
    z=x+y
    return x,y,z


# In[16]:


masomme6(21,21)


# Le retour d'une telle fonction peut être assigné à une variable...

# In[17]:


a = masomme6(52, -10)
print(a)


# ...ou plusieurs, à conditions qu'il y ait autant de variables que de valeurs retournées.

# In[18]:


a,b,c = masomme6(19,23)
print(c)


# ### Exercice 7
# 
# * Créez une fonction `powersix` qui prend une valeur en paramètre et retourne ses 6 premières puissances, e.g. `powersix(x)` retourne $x, x^2, x^3, x^4, x^5 et \; x^6$. N'oubliez pas le *docstring* !
# * Si le retour de la fonction `powersix` est assigné à une unique variable, quelle est son type ?
# * Modifiez votre fonction pour qu'elle retourne une **liste** des 6 premières puissances

# In[ ]:





# ## Portée des variables
# 
# Une variable qui est définie à l'intérieur d'une fonction n'existe que là.
# L'*endroit* où une variable existe est appelé sa **_portée_**.
# De cette manière les fonctions sont des portions de *code* indépendantes ce qui les rend plus facile à débugger.

# In[19]:


def Afunc():
    A = 42
    print(A)

A = 10
print(A)
Afunc()
A = 100
print(A)
Afunc()


# ### Travail personnel
# 
# En réalité, la portée des variables en *Python* est un peu plus compliquée que cela. Cherchez sur internet des informations à ce sujet et complétez cette section pour la prochaine leçon.

# ## Fonction *lambda*
# 
# *Python* permet une syntaxe intéressante qui vous laisse définir des mini-fonctions d’une ligne à la volée. Empruntées à [*Lisp*](https://en.wikipedia.org/wiki/Lisp_%28programming_language%29), ces fonctions dites lambda peuvent être employées partout où une fonction est nécéssaire.
# 

# In[20]:


f1 = lambda x: x**2 

# est équivalent à

def f2(x):
    return x**2


# In[21]:


f1(3), f2(3)


# Vous pouvez utiliser une fonction *lambda* sans l’assigner à une variable. Ce n’est pas forcément très utile, mais cela démontre qu’une fonction *lambda* est simplement une fonction en ligne.

# In[22]:


(lambda x: x**2)(3)


# ### Exercice 8
# 
# La fonction `map` prend une fonction et une liste en paramètre et retourne la liste des résultats de l'application de la fonction aux éléments de la liste (cf `help(map)`).
# 
# En utilisant cette fonction `map` combinée à une fonction *lambda*, afficher en une seule ligne de code la liste des tous les cubes de 2 à 42.

# In[23]:


help(map)


# Ce Notebook est a été crée par David Da SILVA - 2020
# 
# Source: [openclassrooms.com](https://openclassrooms.com/courses/pratiques-avancees-et-meconnues-en-python)
# 
# <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
