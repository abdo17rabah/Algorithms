# -*- coding: utf-8 -*-

###########################    Arbre Binaire    ###########################


class Noeud(object): 
  def __init__(self, element, ga=None, dr=None): 
    self.val = element 
    self.ga  = ga
    self.dr = dr

def hauteur(A):
    "fonction qui calcule la hauteur d'un arbre binaire A"
    if A ==None:
      return -1
    return 1+max(hauteur(A.ga),hauteur(A.dr))
 
def voir(A,dec=1):
  "un affichage planaire de l'arbre A modulo une rotation à 90°"
  if A == None:return ""
  return voir(A.dr,dec+5)+' '*dec+str(A.val)+'\n'+voir(A.ga,dec+5)
        
# Un exemple d'arbre binaire : 
B=Noeud(4,Noeud(1,None,Noeud(9)),Noeud(3,Noeud(2,Noeud(5),None),Noeud(7)))

print(voir(B)+"\n")


# 1. Écrire une fonction affichePrefixe(A) qui affiche les éléments d'un arbre binaire A
#    dans l'ordre préfixé, une fonction qui affiche les éléments
#    d'un arbre binaire dans l'ordre infixé et une fonction qui
#    affiche les éléments d'un arbre binaire dans l'ordre postfixé.
def prefixe(A) :
	if A == None :
		return None
	else :
		print(A.val)
		prefixe(A.ga)
		prefixe(A.dr)
print("#------ordre préfixé------#")
print(prefixe(B))

def infixe(A) :
	if A== None :
		return None
	else :
		infixe(A.ga)
		print(A.val)
		infixe(A.dr)

print("#------ordre infixe------#")
print(infixe(B))

def postfixe(A) :
	if A == None :
		return None
	else :
		postfixe(A.ga)
		postfixe(A.dr)
		print(A.val)
print("#------ordre postfixe------#")
print(postfixe(B))

# 2. Écrire une fonction interne(A) qui retourne le nombre de noeuds internes
#    (i.e. les noeuds qui ne sont pas des feuilles) d'un arbre binaire A.
def interne(A) :
	nb=0
	if A == None :
		return 0
	elif A.ga == None :
		return interne(A.dr)
	else :
		return 1+interne(A.ga)+interne(A.dr)
print("#------interne(B)------#")
print(" le nombre de noeuds internes est : ")
print(interne(B))
	
# 3. Écrire une fonction filiforme(A) qui détermine si un arbre binaire A est dégénéré
#    (c'est-à-dire, tel que tout noeud a au plus un fils).
def filforme(A) :
	if A==None :
		return True
	else :
		if A.ga != None and A.dr == None :
			return filforme(A.ga)
		elif A.dr != None and A.ga == None :
			return filforme(A.ga)
		elif A.dr == None and A.ga == None :
			return False	
		return False
print("#------filiforme(B)------#")
print(" B est dégénéré ? ")
print(filforme(B))
C=Noeud(4,None,Noeud(3,Noeud(2,Noeud(5),Noeud(7)),Noeud(7)))
print(filforme(C))	
	
# 4. Écrire une fonction combien(A,k) qui retourne le nombre de noeuds
#    de l'arbre binaire A qui sont à la profondeur k.
#    (cas possibles : i) A est vide ou k<0,
#                     ii) A est non vide et k=0,
#                     iii) A est non vide et k>0)
def combien(A,k):
	if A==None :
		return 0
	elif k==0 :
		return 1
	else :
		return combien(A.ga,k-1) + combien(A.dr,k-1)
print("#------nombre de noeuds de (B)------#")
print(combien(B,3))

# 5. La longueur de cheminement d'un arbre binaire est
#    la somme des profondeurs de tous les noeuds de cet arbre.
#    Écrire une fonction long_chemin(A,p=0) qui calcule la longueur de cheminement
#    d'un arbre binaire A. (p indique la profondeur du noeud racine de A).
def long_chemin(A,p) :
	if A==None :
		return 0
	elif p==0 :
		return 1
	else :
		p=1
		if A.ga != None and A.dr == None :	
			return p+long_chemin(A.ga,p)
		elif A.ga == None and A.dr != None :
			return p+long_chemin(A.dr,p)
		else :
			return p+long_chemin(A.ga,p)+long_chemin(A.dr,p)
print("#------la longueur de cheminement de (B)------#")
print(long_chemin(B,1))


# 6. Un arbre binaire est équilibré si en tout noeud de l'arbre
#    la différence des hauteurs de ses deux sous-arbres gauche et droit est d'au plus 1.
#    Écrire une fonction equilibre(A) qui retourne un booléen et un entier:
#    le booléen vaut vrai et l'entier indique la hauteur de l'arbre
#    si l'arbre est équilibré, le booléen vaut faux et l'entier indique
#    une valeur bidon (par exemple -2) sinon.

