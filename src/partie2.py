from partie1 import *
import numpy as np


   # ----------------------------------------------------------------------------------------------------#
   ######################################  PARTIE 2  ##################################################
   # --------------------------------------------------------------------------------------------------

def image_noire(h,l):
    return np.zeros((h,l))       #retourner la matrice qui contient des zeros.


def image_blanche(h, l):
    return np.ones((h,l))         #retourner la matrice qui contient des uns.

def creerImgBlancNoir(h, l):
      Im = image_noire(h,l)       #initialiser  la matrice image par des zéros.
      for i in range(h):          #parcourir les lignes.
         for j in range(l):       # parcourir les colonnes.
            Im[i][j] = (i + j) % 2
      return Im

def negatif(Img):
    return 1 - Img # si la valeur du pixel = 1 ---> new valeur = (1 - 1)=0
                   # si la valeur du pixel = 0 ---> new valeur = (1 - 0)=1


