from partie3 import *

#----------------------------------------------------------------------------------------------------#
######################################  PARTIE 4  ##################################################
#---------------------------------------------------------------------------------------------------#


def inverser(img):
    return 255-Ouvrir(img)


def flipH(Img):
   return Ouvrir(Img)[:,::-1] # parcourir tous les lignes et les colonnes,et on va renverser l'ordre des colonnes


def poserV(img1,img2):
    return np.concatenate((Ouvrir(img1),Ouvrir(img2)), axis=0) #'0' pour la concatunation vertcale

def poserH(img1,img2):
    return np.concatenate((Ouvrir(img1), Ouvrir(img2)), axis=1) #'1' pour la concatunation Horizontale

