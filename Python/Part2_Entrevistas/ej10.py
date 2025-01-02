import cv2 
from pyzbar.pyzbar import decode 
import os
from PIL import Image
   
def DirectoryReader(dir):
    # Obtenim tots els fitxers del directori
    for fitxer in os.listdir(dir):
        if fitxer.endswith('.png'):
            # El nom de l'alumne es correspon amb el nom del fitxer (sense .png)
            nom = fitxer.replace('.png', '')
            
            # Obrim la imatge
            image = Image.open(os.path.join(dir, fitxer))
            
            # Llegim l'ID des del codi de barres de la imatge passant l'objecte d'imatge
            codi_id = BarcodeReader(image)
            
            if codi_id:
                print("Nom de l'alumne: "+nom+", ID: "+codi_id)
            else:
                print("No s'ha pogut llegir el codi de barres de "+nom)

def BarcodeReader(image):
    # Decodifiquem els codis de barres
    codis = decode(image)
    
    # Si trobem algun codi de barres, retornem el primer (hi hauria de ser només un)
    if codis:
        return codis[0].data.decode('utf-8')
    else:
        return
  
DirectoryReader(".")
