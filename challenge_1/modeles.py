class Eleve:
    def __init__(self, id_eleve, prenom, nom, filiere,
    maths=None, francais=None, anglais=None,
    histoire=None, svt=None, physique=None):

        self.id_eleve = id_eleve
        self.prenom = prenom
        self.nom = nom
        self.filiere = filiere
        self.maths = maths
        self.francais = francais
        self.anglais = anglais
        self.histoire = histoire
        self.svt = svt
        self.physique = physique

    def notes(self):
        toutes = [self.maths, self.francais, self.anglais, self.histoire, self.svt, self.physique]
        resultat = []
        for n in toutes:
            if n is not None:
                resultat.append(n)
        return resultat
 

    def moyenne(self):
        n = self.notes()
        if not n:
            return None
        return round(sum(n) / len(n), 2)
        
    def est_admis(self, seuil=10.0):
        moyenne = self.moyenne()
        if moyenne is not None and moyenne >= seuil:
            return True
        else:
            return False
        
    def bulletin(self):
        moyenne = self.moyenne()
        statut = " Admis" if self.est_admis() else " Non admis"

        print(f"{self.prenom} {self.nom} ({self.filiere})")
        print(f" Moyenne : {moyenne if moyenne is not None else 'N/A'}/20 | {statut}")

print(Eleve)
    