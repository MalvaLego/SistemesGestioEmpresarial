import os
import shutil

llista=["png","mp4","doc","py","txt"]

carpetaActual = os.getcwd()

for dir in llista:
    carpeta = dir
    ruta = os.path.join(carpetaActual, carpeta)
    if not os.path.exists(ruta):
        os.mkdir(ruta)

    for fitxer in os.listdir(carpetaActual):
        if fitxer.endswith("."+dir):
            rutaFitxer = os.path.join(carpetaActual, fitxer)
            try:
                shutil.move(rutaFitxer, ruta)
                print("Fitxer "+fitxer+" mogut a "+ruta)
            except Exception as e:
                print("Error al moure el fitxer "+fitxer+": "+e)
