# -*- coding:utf-8 -*-

######################    Arbre Binaire de Recherche (ABR)   ######################

class Noeud(object): 
  def __init__(self, element, ga=None, dr=None): 
    self.val = element 
    self.ga  = ga
    self.dr = dr

unABR=Noeud(10,Noeud(5,None,Noeud(7)),Noeud(13,Noeud(12,Noeud(11),None),Noeud(17)))

def voir(A,dec=1):
    "un affichage planaire de l'arbre binaire A modulo une rotation à 90°"
    if A == None:return ""
    return voir(A.dr,dec+5)+' '*dec+str(A.val)+'\n'+voir(A.ga,dec+5)

#print(voir(unABR)+"\n")

# 1. Écrivez une procédure minimum(A) qui retourne un pointeur sur le noeud de valeur minimale d'un ABR A
#    (et retourne None si l'ABR est vide).
def minimum(A):
	if A==None :
		return None
	if A.ga==None :
		return A
	else :
		return minimum(A.ga)

x=minimum(unABR)		
print(x.val)

# 2. Écrivez une procédure itérative present(A,x) qui, étant donné un ABR A et un élément x,
#    détermine si l'élément x est présent ou non dans l'ABR A (la procédure retourne un booléen).
def present(A,x):
	if A==None:
		#print("élément non trouvé")
		return False
	elif x==A.val :
		return True
	elif x<A.val :
		return present(A.ga,x)
	else :
		return present(A.dr,x)
print(present(unABR,99))

# 3. Écrivez une procédure insere(A,x) qui renvoie l'ABR A où on a ajouté l'élément x.
#    La procédure ne modifie rien si x est déjà dans A.
def insere(A,x) :
	if present(A,x)==True :
		return A
	if A==None :
		return Noeud(x,None,None)
	if x<A.val :
		A.ga=insere(A.ga,x)
	elif x>A.val :
		A.dr=insere(A.dr,x)
	return A
Abr=insere(unABR,8)
#print(voir(Abr)+"\n")

# 4. Écrivez une procédure affiche(A) qui affiche tous les éléments d'un ABR A
#    dans l'ordre croissant.
def afficher(A) :
	if A!= None :
		afficher(A.ga)
		print(A.val)
		afficher(A.dr)

#afficher(unABR)

# # 5*. Écrivez une procédure afficheIntervalle(A,debut,fin)
#    qui, pour deux valeurs debut et fin supposées telles que début <= fin,
#    affiche tous les éléments x de l'ABR A qui appartiennent à l'intervalle [debut, fin].
#    Évitez les parcours de sous-arbres inutiles.	
#    Considérez les 4 cas suivants:
#    1) A = None : rien à afficher;
#    2) fin < A.val : appel récursif sur le sous-arbre gauche;
#    3) A.val < debut : appel récursif sur le sous-arbre droit;
#    4) debut <= A.val <= fin :
#     appel récursif sur le sous-arbre gauche et l'intervalle [debut,A.val], écrire A.val
#     puis appel récursif sur le sous-arbre droit et l'intervalle [A.val,fin]
def afficheIntervalle(A,debut,fin):
	if A==None :
		return -1
	elif fin < A.val :
		afficheIntervalle(A.ga,debut,fin)
	elif A.val < debut :
		afficheIntervalle(A.dr,debut,fin)
	else :
		afficheIntervalle(A.ga,debut,fin)
		print(A.val)
		afficheIntervalle(A.dr,debut,fin)
print(afficheIntervalle(unABR,10,17))
# 6**. Écrivez une procédure rechercheKeme(A,k)
#    qui recherche le k-ème plus petit élément de l'ABR A, pour k>=1.
#
#    Le principe est d'effectuer un parcours infixé où
#    l'on décrémente k lors de la visite de chaque noeud.
#
#    Cette procédure retourne un couple: un élément et un entier.
#
#    Dans le cas où ce k-ème plus petit élément de A existe (k <= taille de l'ABR A),
#    l'élément correspond au k-ème plus petit élément de l'ABR A
#    et l'entier vaut 0.
#
#    Dans le cas où ce k-ème plus petit élément n'existe pas,
#    on donne à l'élément une valeur 'bidon', -1 par exemple,
#    et l'entier vaut k moins le nombre d'éléments de l'ABR A.


# 7. Écrivez une procédure coupeSelon(A,x) qui, pour un ABR A et un élément x
#    (présent ou non dans A),retourne deux ABR:
#    un ABR contenant les éléments de A strictement inférieurs à x
#    et un ABR contenant les éléments de A strictement supérieurs à x.
#    Quels noeuds de A sont visités par la procédure coupeSelon(A,x)?

# 8. Écrivez une procédure insereAlaRacine(A,x) qui retourne l'ABR A
#    où on ajoute l'élément x comme racine.
#    Vous utiliserez pour cela la procédure coupeSelon.

# 9. Écrivez une procédure récursive fusion(A,B) qui retourne l'ABR
#    qui est la fusion des ABR A et B.
#    Vous utiliserez pour cela la procédure coupeSelon.



