class Professor:
    def __init__(self, nom, tipus):
        self.nom = nom
        self.tipus = tipus 

    def getNom(self):
        return self.nom

    def printar(self):
        return f"Professor: {self.nom}, Tipus: {self.tipus}"


class Alumne:
    def __init__(self, nom, curs, professor_responsable):
        self.nom = nom
        self.curs = curs
        self.professor_responsable = professor_responsable

    def getNom(self):
        return self.nom

    def printar(self):
        return f"Alumne: {self.nom}, Curs: {self.curs}, Professor Responsable: {self.professor_responsable}"


class Escola:
    def __init__(self, nom, localitat, responsable):
        self.nom = nom
        self.localitat = localitat
        self.responsable = responsable
        self.professors = []
        self.alumnes = [] 

    def afegir_professor(self, professor):
        for p in self.professors:
            if (p.getNom()==professor.getNom()):
                return print("Error! No es pot afegir un porfessor a dues escoles")
        self.professors.append(professor)

    def eliminar_professor(self, nom_professor):
        for p in self.professors:
            if (p.getNom()==nom_professor):
                self.professors.remove(p)

    def afegir_alumne(self, alumne):
        for a in self.alumnes:
            if (a.getNom()==alumne.getNom()):
                return print("Error! No es pot afegir un alumne a dues escoles")
        self.alumnes.append(alumne)

    def eliminar_alumne(self, nom_alumne):
        for a in self.alumnes:
            if (a.getNom()==nom_alumne):
                self.alumnes.remove(a)
    
    def getLlistaProfessors(self):
        return self.professors
    def getLlistaAlumnes(self):
        return self.alumnes
