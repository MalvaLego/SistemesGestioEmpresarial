#Funció contandoMinas
def contandoMinas(mines):
    files = len(mines)
    columnes = len(mines[0])
    
    #Còpia per al resultat
    resul = []
    for a in range(files):
        resul.append([0] * columnes)
    
    #Recorrem cada casella per si és una mina, la deixem com a -1.
    for i in range(files):
        for j in range(columnes):
            if mines[i][j]== -1:
                resul[i][j]= -1  
            else:
                #Comptem les mines adjacents
                cont= 0
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if (0<=i + x<files) and (0<=j + y<columnes) and (x != 0 or y != 0):
                            if mines[i+x][j+y] == -1:
                                cont += 1
                resul[i][j]= cont
    return resul

#Entrada del buscamines
mines = [[0, 0, -1, 0],[0, -1, -1, 0]]

resul = contandoMinas(mines)

#Resultat
for fila in resul:
    print(fila)
