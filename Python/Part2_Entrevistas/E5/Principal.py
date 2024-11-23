from models import Escola,Professor,Alumne

e1 = Escola("Escola de Python", "València", "Joan Ferrer")
e2 = Escola("Escola de Java", "Barcelona", "Laura Puig")

p1 = Professor("Anna López", "Ciències")
p2 = Professor("Carles Pérez", "Lletres")

a1 = Alumne("Maria García", "3r ESO", "Anna López")
a2 = Alumne("Josep Martí", "4t ESO", "Carles Pérez")

e1.afegir_professor(p1)
e2.afegir_professor(p2)

e1.afegir_alumne(a1)
e2.afegir_alumne(a2)

#Imprimir les dades de cada escola
print("Escola 1:")
for p in e1.getLlistaProfessors():
    print(p.printar())
for a in e1.getLlistaAlumnes():
    print(a.printar())

print("\nEscola 2:")
for p in e2.getLlistaProfessors():
    print(p.printar())
for a in e2.getLlistaAlumnes():
    print(a.printar())


#Error al afegir un professor a dues escoles
print()
e1.afegir_professor(p1)

#Error al afegir un alumne a dues escoles
e2.afegir_alumne(a2)

#Eliminar un objecte de cada escola
print()
e1.eliminar_professor("Anna López")
e2.eliminar_alumne("Josep Martí")        

#Imprimir les dades de cada escola després d'eliminar un professor i un alumne
print("Escola 1:")
for p in e1.getLlistaProfessors():
    print(p.printar())
for a in e1.getLlistaAlumnes():
    print(a.printar())

print("\nEscola 2:")
for p in e2.getLlistaProfessors():
    print(p.printar())
for a in e2.getLlistaAlumnes():
    print(a.printar())
