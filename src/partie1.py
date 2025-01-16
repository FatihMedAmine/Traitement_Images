import matplotlib.pyplot as plt

#----------------------------------------------------------------------------------------------------#
######################################  PARTIE 1  ##################################################
#--------------------------------------------------------------------------------------------------


def AfficherImg(img):
   plt.axis("off")  # pour masquer les axes
   plt.imshow(img, interpolation="nearest")  # image naturelle
   #plt.imshow(img,cmap='gray')
   plt.show()




#________________________________________________________________________________________________________


def ouvrirImage(chemin):
   img = plt.imread(chemin) # Lire l'image à partir sa chemin.
   return img


#________________________________________________________________________________________________________

def saveImage(img):
   plt.imsave("image1.png", img)






