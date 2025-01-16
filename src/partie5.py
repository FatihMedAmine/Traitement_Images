from partie4 import *
from random import *

#----------------------------------------------------------------------------------------------------#
######################################  PARTIE 5  ##################################################
#--------------------------------------------------------------------------------------------------


M=[[[210, 100, 255],[100, 50, 255],[90, 90, 255],[90, 90, 255],[90, 90, 255],[90, 80, 255]],
[[190, 255,89],[ 201, 255,29],[200, 255,100],[100, 255,90],[20, 255,200], [100, 255,80]],
[[255,0, 0],[ 255,0, 0],[255,0, 0],[255,0, 0],[255,0, 0], [255,0, 0]]]

#print("M[0][1][1]:",M[0][1][1])
#print("M[1][0][1]:",M[1][0][1])
#print("M[2][1][0]:",M[2][1][0])


#print(" la quantité de mémoire nécessaire en octets(8 bits) pour stocker le tableau représentant une image RGB, justifier votre réponse?")
#print("Answer: 3*6*pixels=18*3 = octets=54 oct car on a la relation est=nbr_des_lignes*nbr_des_colonnes*3")

def initImageRGB():
        nbLignes   =   randrange(1,10)  #prendre le nombre des lignes par une maniére aleatoire
        nbColonnes =   randrange(1,10)  #prendre le nombre des colonnes par une maniére aleatoire
        imageRGB = np.zeros((nbLignes,nbColonnes,3),dtype=int)
        # Initialisation du tableau imageRGB avec des valeurs aléatoires
        for i in range(nbLignes):
            for j in range(nbColonnes):
                    imageRGB[i][j]= [randrange(256),randrange(256),randrange(256)]
        # Renvoi du tableau imageRGB initialisé
        return imageRGB


def symetrieV(Img):
    return Img[:, ::-1]



def symetrieH(Img):
    return Img[::-1,:]


def grayscale(Img):
    l,c=len(Img),len(Img[0])        # rendre le dimention du matrice de l'image IMG
    Gri=np.zeros((l,c))             # initialisée la matrice Gri par des zéros
    for i in range(len(Img)):       #  parcourir les lignes
        for j in range(len(Img[0])):# parcourir les colonnes
            max=min=Img[i][j][0]    #initalisée le max et le min
            for k in range(1,3):
                if max<Img[i][j][k]: #faire la comparaison
                    max=Img[i][j][k]
                if min>Img[i][j][k]:
                    min=Img[i][j][k]
            Gri[i][j]=(max+min)//2   #faire remplissage du matrice Gri
    return Gri

tst=initImageRGB()
AfficherImg(tst)
AfficherImg(grayscale(tst))



