# -*- coding:utf-8 -*-

# psyco est un module basé sur les techniques de "compilation à la volée"
# et permet ainsi d'accélérer l'exécution des programmes.
try:
    import psyco
    psyco.full() 
except:
    pass

from random import randrange
from time import time

def tirageAleatoire(taille,rang=30):
    """retourne un tableau de taille entiers dont les valeurs
    sont tirées aléatoirement dans l'intervalle [0,rang-1]"""
    res=[0]*taille
    for i in range(taille):
        res[i]=randrange(rang)
    return res

###########################   TRI RAPIDE   ###########################

def partition(tableau,g,d):
    "partition du tableau dans l'intervalle [g,d]"
    pivot=tableau[g]
    courg=g+1  
    courd=d 
    while True:
        while courg<d and tableau[courg]<=pivot:
            courg=courg+1
        while tableau[courd]>pivot:
            courd=courd-1
        if courg < courd:
            tableau[courg],tableau[courd]=tableau[courd],tableau[courg]
        else: 
            tableau[g],tableau[courd]=tableau[courd],tableau[g]
            return courd

def triRapide(tableau,g,d):
    "tri du tableau dans l'intervalle [g,d], donc tri de tableau[g:d+1]"
    if g<d:
        i=randrange(g,d+1)
        tableau[g],tableau[i]=tableau[i],tableau[g]
        m=partition(tableau,g,d)
        triRapide(tableau,g,m-1)
        triRapide(tableau,m+1,d)

print("Un exemple d'execution de triRapide:"); print
L=[5,3,4,7,4,1]; print("la liste initiale:", L)
print
triRapide(L,0,5); print("la meme liste, mais triee:", L)

##########################   TRI SELECTION   #########################

## 1) Ecrire la fonction TriSelection
compt1=0
def triSelection(tableau):
    nb = len(tableau)
    for en_cours in range(0,nb):
        global compt1    
        compt1 +=1  
        plus_petit = en_cours
        for j in range(en_cours+1,nb) :
            if tableau[j] < tableau[plus_petit] :
                plus_petit = j
        if tableau[plus_petit]< tableau[en_cours] :
            temp = tableau[en_cours]
            tableau[en_cours] = tableau[plus_petit]
            tableau[plus_petit] = temp
    return tableau

print("TRI SELECTION",triSelection(L))
print("Nombre de Comparaison TRI SELECTION",compt1)         
##########################   TRI FUSION   #########################

## 2) Ecrire la fonction fusion

#def fusion2(tableau, g, d
compt2=0
def fusion(tab1,tab2):
    """ retourne le tableau résultant de la fusion
    des deux tableaux triés tab1 et tab2 """
    res=[]
    index_gauche, index_droite = 0, 0
    while index_gauche < len(tab1) and index_droite < len(tab2): 
        global compt2
        compt2 +=1     
        if tab1[index_gauche] <= tab2[index_droite]:
            res.append(tab1[index_gauche])
            index_gauche += 1
        else:
            res.append(tab2[index_droite])
            index_droite += 1
    if tab1:
        res.extend(tab1[index_gauche:])
    if tab2:
        res.extend(tab2[index_droite:])
    return res

def triFusion(tableau,g,d):
    if g<d:
        m=(g+d)//2
        triFusion(tableau,g,m)
        triFusion(tableau,m+1,d)
        tableau[g:d+1]=fusion(tableau[g:m+1],tableau[m+1:d+1])
    return tableau

print("FUSION",fusion([1,3,4,7,14,21,29],[13,18,71,145,211]))
print("TRI FUSION",triFusion([1,3,4,75,13,18,71,14,21],0,7))
print("Nombre de Comparaison du TRI FUSION",compt2)
##########################   TEST   #########################                

## 3) Tester les temps d'exécution des différents tris
##        pour différentes tailles: 10, 100, 1000,
##        et, si on peut: 10 000, 100 000, 1 000 0000
        
def test(n):
    monTab=tirageAleatoire(n,n)
    print("*"*20); print("taille = "),; print(n)
    tonTab=monTab[:]
    print("######   TEST tri Rapide  #####")
    t1=time()
    triRapide(tonTab,0,len(tonTab)-1)
    t2=time()
    print("temps du tri rapide: "); print(t2-t1)

    print("######   TEST tri Fusion   #####")
    t3=time()
    triFusion(tonTab,0,len(tonTab)-1)
    t4=time()
    print("temps du tri Fusion: "); print(t4-t3)

    print("######   TEST tri Selection  #####")
    t5=time()
    triSelection(tonTab)
    t6=time()
    print("temps du tri Selection: "); print(t5-t6)

for el in [10,100,1000]:#,10000,100000,1000000]:
    test(el)
    print


## 4) Pour chacun des tris, introduire une variable compteur (globale)
##      pour compter le nombre de comparaisons entre paires d'éléments du tableau.
##
##    Pour chacun des tris, répondre à la question suivante:
##    Quand on multiplie la taille par 10, par combien est multiplié le temps? le nombre de comparaisons?
