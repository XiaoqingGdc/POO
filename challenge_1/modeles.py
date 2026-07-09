class Eleve:
    def __init__(self,id_eleve,prenom,nom,etablissement,filiere,maths,francais,anglais,histoire,svt,physique):
        self.id_eleve = id_eleve
        self.prenom = prenom
        self.nom = nom
        self.etablissement = etablissement
        self.filiere = filiere
        self.maths = maths
        self.francais = francais
        self.anglais = anglais
        self.histoire = histoire
        self.svt = svt
        self.physique = physique

    def notes(self):
        list_notes = [self.maths, self.francais, self.anglais]
        return list_notes
    
    def moyenne(self):
        note_valide = [note for note in self.notes() if note is not None ]
        if not note_valide:
            return f" Erreur de note"
        self.note_moyenne =  round(sum(note_valide) / len(note_valide), 2)
        return self.note_moyenne
    
    def est_admis(self,seuil = 10.0):
        note_moyenne = self.moyenne()
        if isinstance(note_moyenne,str):
            return False
        if 0<= note_moyenne <=20:
            return note_moyenne > seuil 
        return "note non valide"
    
    def mention(self):
        note_moyenne = self.moyenne()
        if not isinstance(note_moyenne, (int, float)):
            return None
        if 12.0 <=note_moyenne <=20 and self.est_admis():
            return "mention Assez bien"
        
    def bulletin(self):
        return f"{self.prenom} {self.nom},{self.moyenne()}/20, admission : {self.est_admis()}"


    def is_goodat_math(self):
        if self.maths is None or isinstance(self.moyenne(), str):
            return False
        return self.maths > self.moyenne()

