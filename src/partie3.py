import matplotlib.pyplot as plt

from partie2 import *
import cv2
#----------------------------------------------------------------------------------------------------#
######################################  PARTIE 3  ##################################################
# --------------------------------------------------------------------------------------------------


def luminance(Img):
   s = 0                           # variable initilisée pour dont on va stocker la somme
   Img=Ouvrir(Img)                 # retourner la matrice de l'image
   for i in range(len(Img)):       # parcourir les lignes
      for j in range(len(Img[0])): # parcourir les colonnes
         s += Img[i][j]            #faire la somme des pixels
   return s / (len(Img)*len(Img[0])) # faire la division de la somme sur la dimension



def constrast(Img):
   s = 0
   N = len(Img)*len(Img[0])
   Moy = luminance(Img)      # le moyenne des pixels
   I = Ouvrir(Img)
   for i in range(len([Img])):
      for j in range(len(Img[0])):
         s += pow(I[i][j] - Moy, 2)  # methode de calculer la variance
   return (1 / N) * s

def profondeur(Img):
   L = Ouvrir(Img)
   maxi = 0                   # la valeur minimale d'un pixel c'est '0'.
   for i in range(len(Img)):
      for j in range(len(Img[0])):
         if L[i][j] > maxi: maxi = L[i][j]    # faire la comparaison .
   return maxi




def Ouvrir(Img):  # fonction permet de retourne la matrice représentant d'un image gris
   return cv2.imread(Img,0) # '0' indique que l'image doit être chargée en niveaux de gris.



