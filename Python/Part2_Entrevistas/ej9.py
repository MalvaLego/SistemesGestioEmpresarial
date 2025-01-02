import csv
import barcode
from barcode.writer import ImageWriter
import sys

#Llegir fitxer CSV
with open('alumnes.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        #Es separen el nom i el id
        nom = row[0]
        id = row[1]

        #Completar l'id amb 12 dígits
        id = id.zfill(12)

        #Codi de barres EAN-13
        codi_classe = barcode.get_barcode_class('ean13')
        codi_barres = codi_classe(id, writer=ImageWriter())

        #Es guarda el codi de barres com a fitxer PNG
        codi_barres.save(nom+".png") 

        print(f"Generant codi de barres per {nom} amb ID {id}.")
