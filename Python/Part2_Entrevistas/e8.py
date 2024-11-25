import os
import shutil

llista=["png","mp4","doc","py","txt"]

carpeta_actual = os.getcwd()

for dir in llista:
    carpeta = dir
    ruta = os.path.join(carpeta_actual, carpeta)
    if not os.path.exists(ruta):
        os.mkdir(ruta)

    for fitxer in os.listdir(carpeta_actual):
        if fitxer.endswith("."+dir):
            ruta_fitxer = os.path.join(carpeta_actual, fitxer)
            try:
                shutil.move(ruta_fitxer, ruta)
                print("Fitxer "+fitxer+" mogut a "+ruta)
            except Exception as e:
                print("Error al moure el fitxer "+fitxer+": "+e)
