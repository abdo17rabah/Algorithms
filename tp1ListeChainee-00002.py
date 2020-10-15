 # -*- coding: utf-8 -*-

# On utilise une classe pour définir le type pointeur sur noeud.
class Noeud(object):
    def __init__(self,val,suiv=None):
        """initialisateur de classe
        permet l'allocation de la mémoire requise pour stocker le noeud
        et l'initialisation de ses attributs val et suiv"""
        self.val=val
        self.suiv=suiv

# Quelques exemples de listes avec représentation simplement chaînée.
# a) la liste vide :
listeVide=None

# b) une liste réduite à l'élément 5 :
listeSingleton=Noeud(5)
# listeSingleton=Noeud(5) => appel de la fonction __init__  de Noeud
# avec comme paramètres : self=listeSingleton, val=5 et suiv=None
#
# Cette simple instruction correspond en pseudo-code à la séquence :
#     listeSingleton : pointeur sur noeud     # déclaration de type
#     Nouveau(listeSingleton)                 # allocation de la mémoire
#     listeSingleton->val=5                   # initialisation du champ val
#     listeSingleton->suiv=None               # initialisation du champ suiv


# c) la liste 2,5,8,10:
maliste=Noeud(2,Noeud(5,Noeud(8,Noeud(10))))


# Exo 1. A partir de la liste maliste=Noeud(2,Noeud(5,Noeud(8,Noeud(10))))
# écrivez l'instruction nécessaire pour afficher le 1er élément de maliste (l'élément 2)
#print (maliste.val)
# puis l'instruction nécessaire pour afficher le 3ème élément (ici 8).
#print (maliste.suiv.suiv.val)
#type (maliste)

# Exo 2. En utilisant les procédures données ci-dessous (essayez d'abord de bien les comprendre),
# écrivez les instructions nécessaires pour :
# a) afficher tous les éléments de maliste;
#p=maliste
#while p!=None:
#	print(p.val)
#        p=p.suiv
    

# b) ajouter l'élément 7 en début de maliste et afficher à nouveau maliste;
#listeSingleton1=Noeud(7)
#listeSingleton1.suiv=maliste
#while listeSingleton1 != None :
#	print (listeSingleton1.val)
#	listeSingleton1=listeSingleton1.suiv

# c) ajouter l'élément 3 en fin de maliste et afficher à nouveau maliste;
#listeSingleton2=Noeud(3)
#temp=maliste
#while temp.suiv!= None :
#	temp=temp.suiv
#temp.suiv=listeSingleton2

#p=maliste
#while p!=None:
#	print(p.val),
#	p=p.suiv

# d) déterminer si l'élément 8 est ou non dans maliste.
#temp=maliste
#pos =0
#while temp!= None :
#	if temp.val == 8 :
#		print ("l'element 8 existe à la position: ",pos)
#	pos+=1	
#	temp=temp.suiv
	


def affiche(debut):
	while debut!=None:
		print(debut.val),
		debut=debut.suiv
	print

def insere_debut(debut,x):
	return Noeud(x,debut)

def insere_fin_it(debut,x):
	if debut==None:
		return Noeud(x)
	cour=debut
	while cour.suiv!=None:
		cour=cour.suiv
		cour.suiv=Noeud(x)
	return debut
    
def recherche_rec(debut,x):
	if debut==None:
		return False
	if debut.val==x:
		return True
	return recherche_rec(debut.suiv,x)


# Exo 3. Donnez une version récursive de la procédure insere_fin(debut,x)
# qui prend en entrée deux arguments (debut qui est une référence
# sur le premier noeud d'une liste et x un élément)
# et qui insère x à la fin de la liste.
def insere_fin_rec(debut,x):
	temp=Noeud(None)
	if debut==None:
		return Noeud(x)
	else:
		temp.val=debut.val
		temp.suiv=insere_fin_rec(debut.suiv,x)
		return temp


#print("---rec--")
#maliste=insere_fin_rec(maliste,97)
#affiche(maliste)
# Exo 4. Donnez une version itérative de la procédure recherche(debut,x)
# qui prend en entrée deux arguments (debut une référence
# sur le premier noeud d'une liste et x un élément) et
# qui détermine si x est ou non dans la liste.
def recherche_iter(debut,x):
	
	if debut==None:
		return False
		
	temp=debut
	while temp!=None:
		if temp.val == x :
			
			return True
		else :	
        		temp=temp.suiv

	return False

#r=recherche_iter(maliste,97)
#print(r)



# Exo 5. Écrivez une procédure inverse(debut)
# qui prend en entrée debut une référence sur le premier noeud d'une liste
# et qui retourne une référence sur le premier noeud de la liste inversée.
def inverser(debut):
	temp=Noeud(debut.val,None)
	p=debut.suiv
	q=temp
	while p!=None:
		temp=Noeud(p.val,q)
		q=temp
		p=p.suiv	
	return temp	
	
#temp1=inverser(maliste)
#affiche(temp1)
# Exo 6. Une liste L1 est une sous-liste d'une liste L2 si L1 est obtenue à partir de L2 en supprimant zéro, un ou plusieurs éléments de la liste L2.
# Exemple: la liste 3,5,10 est une sous-liste de la liste 2,3,5,5,7,10.
# Écrivez une procédure sousListe(L1,L2)
# qui prend en entrée deux listes L1 et L2 et qui retourne True si L1 est une sous-liste de L2.
# On supposera que L1 et L2 sont des listes d'entiers triés dans l'ordre croissant (au sens large).
def sousListe(L1,L2):
	p=L1
	q=L2
	bol=False
	if L2==None and L1 != None:
		return False
	if L1==None and L2 != None:
		return False
	while p!=None and q!=None:
		if p.val<q.val :
			p=p.suiv
		elif p.val>q.val :
			q=q.suiv
		else :
			p=p.suiv
			q=q.suiv
			return True
	return False

maliste1=Noeud(9,Noeud(11,Noeud(4,Noeud(6))))
s=sousListe(maliste,maliste1)
print(s)
# Exos un peu plus difficiles (avec *):

# Exo 7. Écrivez une procédure insere_apres(L,x,y)
# qui insère un élément y après la première occurrence de l'élément x dans une liste L
# (ne fait rien en l'absence de x) et retourne la liste ainsi modifiée.
def insere_apres(L,x,y):
	p=L
	if L==None:
		return L
	while p!=None :
		if p.val==x :
			q=Noeud(y,p.suiv)
			p.suiv=q
		p=p.suiv
	return L
s=insere_apres(maliste,2,100)
affiche(s)
# Exo 8. Écrivez une procédure insere_avant(L,x,y)
# qui insère un élément y avant la première occurrence de l'élément x dans une liste L
# (ne fait rien en l'absence de x) et retourne la liste ainsi modifiée.
def insere_avant(L,x,y):
	p=L
	temp=p
	if p.val == x:
		q=Noeud(y,L)
		L=q
		return L
	p=p.suiv
	while p!=None :
		if p.val!=x :
			temp=p
			p=p.suiv
		elif p.val==x :
			q=Noeud(y,p)
			temp.suiv=q
		p=p.suiv
	return L
			
s=insere_avant(maliste,2,100)
affiche(s)
## Test

#debut=None
#for i in range(3):
#   debut=insere_fin_it(debut,i)
#affiche(debut)
