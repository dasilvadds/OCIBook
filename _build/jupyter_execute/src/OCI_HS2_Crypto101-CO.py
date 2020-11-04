#!/usr/bin/env python
# coding: utf-8

# # Cryptographie 101
# 
# ---
# 
# Depuis les simples substitutions de lettres à l'époque de *César*, l'art de dissimuler aux regards indiscrets le contenu de messages, notamment militaires, dépend aujourd'hui de l'arithmétique, de l'informatique et d'algorithmes puissants.
# 
# ## 1 - Codage de *César*
# 
# Le codage dit de *Jules César* est simple : faire un décalage de trois lettres sur toutes les lettres d'un message. De plus, les lettres du message en clair sont en minuscule et les lettres du message codé en majuscule. Dans l'algorithme de *César*, a devient D, b devient E, etc.
# 
# Ecrivez une fonction qui réalise le codage de *César* :
# 
# - Le message à coder sera passé en paramètre (pas de d'impératif de casse)
# - La fonction affichera le message en clair en minuscule et le message codé en majuscule
# - La fonction *retournera* le message codé
# 
# Ecrivez ensuite la fonction de décodage:
# 
# - Le message à décoder sera passé en paramètre (pas d'impératif de casse)
# - La fonction affichera le message codé en majuscule et le message décodé en minuscule
# - la fonction *retournera* le message décodé

# In[2]:


def codecesar(message):
    alph = "abcdefghijklmnopqrstuvwxyz"
    message = message.lower()
    #print message
    code = ""
    for c in message :
        if c in alph:
            idx = alph.index(c)
            newidx = (idx + 3) % 26
            code += alph[newidx]
        else :
            code += c
    code = code.upper()
    #print code
    return code


# In[3]:


def decodecesar(code):
    alph = "abcdefghijklmnopqrstuvwxyz"
    #print code
    code = code.lower()
    message = ""
    for c in code :
        if c in alph:
            idx = alph.index(c)
            newidx = (idx - 3) % 26
            message += alph[newidx]
        else :
            message += c
    #print message
    return message


# In[10]:


def _test_cesar():
    assert codecesar("Le message est : toto") == "OH PHVVDJH HVW : WRWR"
    assert decodecesar("OH PHVVDJH HVW : WRWR") == "le message est : toto"
    print("Code César OK")


# In[11]:


_test_cesar()


# ## 2 - Codage de *César* v. 2.0
# 
# La première version, très simple, a plusieurs défauts. 
# Déjà, si un ennemi acquiert une connaissance du procédé, il lui est très facile de décoder immédiatement tout message reçu. En outre, s'il se trouve devant un message codé et le même message en clair, il comprendra immédiatement les règles de cryptage. La méthode qui est venue après celle de *César* a tenu compte de ces défauts : au lieu de coder chaque lettre par un même décalage, on transforme chaque lettre en une autre selon une
# règle de correspondance telle que :
# 
# b|c|d|e|f|g|h|i|...|z|a
# ---|---
# C|H|A|R|L|E|S|B|...|Y|Z
# 
# On choisit une lettre de départ (le b, dans notre exemple) et un mot clé (CHARLES) et on ordonne les lettres par le codage décrit ci-dessus, les lettres n'appartenant pas au mot CHARLES étant classées par ordre croissant ensuite.
# 
# Ecrivez une fonction qui réalise le codage de *César* v. 2.0:
# 
# - Le message à coder sera passé en paramètre (pas de d'impératif de casse), ainsi que la clé et la lettre de départ
# - La fonction affichera le message en clair en minuscule et le message codé en majuscule
# - La fonction *retournera* le message codé
# 
# Ecrivez ensuite la fonction de décodage:
# 
# - Le message à décoder sera passé en paramètre (pas d'impératif de casse), ainsi que la clé et la lettre de départ
# - La fonction affichera le message codé en majuscule et le message décodé en minuscule
# - la fonction *retournera* le message décodé

# In[15]:


def codecesar2(message, cle, lettre):
    alph = "abcdefghijklmnopqrstuvwxyz"
    cle=cle.lower()
    lettre = lettre.lower()
    idxlettre = alph.index(lettre)
    base = alph[idxlettre:] + alph[:idxlettre]
    transform = ""
    for l in alph:
        if l not in cle:
            transform += l
    transform = cle + transform
    
    message = message.lower()
    #print message
    code = ""
    
    for c in message:
        if c in alph:
            idx = base.index(c)
            code += transform[idx]
        else : 
            code += c
    code = code.upper()        
    #print code
    return code
    


# In[14]:


def decodecesar2(code, cle, lettre):
    alph = "abcdefghijklmnopqrstuvwxyz"
    cle = cle.lower()
    lettre = lettre.lower()
    idxlettre = alph.index(lettre)
    base = alph[idxlettre:] + alph[:idxlettre]
    transform = ""
    for l in alph:
        if l not in cle:
            transform += l
    transform = cle + transform
   
    #print code.upper() 
    code = code.lower()
   
    message = ""
    
    for c in code:
        if c in alph:
            idx = transform.index(c)
            message += base[idx]
        else : 
            message += c
    
    #print message
    return message
    


# In[12]:


def _test_cesar2():
    assert codecesar2("le message est : toto", "CHarles", "B") == "GR IRPPZER RPQ : QKQK"
    assert decodecesar2("GR IRPPZER RPQ : QKQK", "chaRLes", "b") == "le message est : toto"
    print("Code César v.2 OK")


# In[16]:


_test_cesar2()


# ## 3 - La substitution poly-alphabétique
# 
# Un algorithme de substitution poly-alphabétique est le suivant : on décale les lettres d'un mot en fonction de la place des lettres, et non en fonction des lettres elles-mêmes. On se munit d'une clé, par exemple CHARLES, et on opère des codages à la *Jules César* avec les 
# $(k + 7)^{ème}$ lettres du texte en utilisant la $k^{ème}$ lettre de la clé. 
# Voici un exemple d'application:
# 
# C|H|A|R|L|E|S|C|H|A|R
# -|-|-|-|-|-|-|-|-|-|-
# s|o|u|v|e|n|t|p|o|u|r
# U|V|U|M|P|R|L|R|V|U|I
# 
# En effet,«s+2=U»,«o+7=V»,«u+0=U»,«u+17=M»...
# 
# Ecrivez une fonction qui réalise le codage par substitution poly-alphabétique:
# 
# - Le message à coder sera passé en paramètre (pas de d'impératif de casse), ainsi que la clé
# - La fonction affichera le message en clair en minuscule et le message codé en majuscule
# - La fonction *retournera* le message codé
# 
# Ecrivez ensuite la fonction de décodage:
# 
# - Le message à décoder sera passé en paramètre (pas d'impératif de casse), ainsi que la clé
# - La fonction affichera le message codé en majuscule et le message décodé en minuscule
# - la fonction *retournera* le message décodé

# In[17]:


def codepoly(message, cle):
    alph = "abcdefghijklmnopqrstuvwxyz"
    cle=cle.lower()
    polycle = cle * (len(message)/len(cle) + 1)
    
    message = message.lower()
    #print message
    code = ""
    
    for i,c in enumerate(message):
        if c in alph:
            idxc = alph.index(c)
            idxpoly = alph.index(polycle[i])
            code += alph[(idxc+idxpoly)%26]
        else : 
            code += c
    
    code = code.upper()        
    #print code
    return code            


# In[18]:


def decodepoly(code, cle):
    alph = "abcdefghijklmnopqrstuvwxyz"
    cle=cle.lower()
    polycle = cle * (len(code)/len(cle) + 1)
    
    code = code.lower()
    #print code.upper()
    message = ""
    
    for i,c in enumerate(code):
        if c in alph:
            idxc = alph.index(c)
            idxpoly = alph.index(polycle[i])
            message += alph[(idxc-idxpoly)%26]
        else : 
            message += c
      
    #print message
    return message          


# In[19]:


def _test_poly():
    assert codepoly("le message est : toto", "charles") == "NL DPWKCNE PWL : KZXG"
    assert decodepoly("NL DPWKCNE PWL : KZXG", "charles") == "le message est : toto"
    print("Code Poly-alphabétique OK")


# In[20]:


_test_poly()


# ## 4 - Module crypto
# 
# Maintenant que nous avons des fonctions de codage et de décodage pour 3 méthodes différentes, nous allons transformer ce notebook en module python qui pourra être importé dans d'autre programme et qui pourra également être executé en tant que programme comme vu dans le notebook 8.
# 
# Lorsque ce module est exécuté en tant que programme, il devra demander à l'utilisateur s'il veut coder ou décoder un message, quelle méthode de cryptage doit être utilisé et les différents paramètres associés à cette méthode.  
# Enfin le message à crypter / décrypter sera demandé et le résultat affiché à l'écran.
# 
# Ecrivez ci-dessous le code nécéssaire à cette réalisation. 

# In[ ]:


if __name__ == "__main__":
    crypto = {"code":{1:codecesar, 2:codecesar2, 3:codepoly},"decode":{1:decodecesar, 2:decodecesar2, 3:decodepoly}}
    action = raw_input("Que voulez vous faire ? \n Pour crypter un message tapez : code\n Pour décrypter un message tapez : decode\n")
    methode =int(raw_input("Quelle méthode voulez-vous utiliser ? \n 1. César \n 2. César V.2 \n 3. Substitution poly-alphabétique\n"))
    if methode == 1 : # codage de César, seul le message est nécessaire
        mesg = raw_input("Quel est le message ? \n")
        args = (mesg,)
    elif methode == 2 : # codage de César V.2, il faut le message, la clé et la lettre
        mesg = raw_input("Quel est le message ? \n")
        cle = raw_input("Quel est la clé ? \n")
        lettre = raw_input("Quel est la lettre ? \n")
        args = (mesg, cle, lettre)
    else : # codage poly-alphabétique, il faut le message et la clé
        mesg = raw_input("Quel est le message ? \n")
        cle = raw_input("Quel est la clé ? \n")
        args = (mesg, cle)
        
    result = crypto[action][methode](*args)
    print("Voici le résulat de l'action demandée : \n {0}".format(result))

