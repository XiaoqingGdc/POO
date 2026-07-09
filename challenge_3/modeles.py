class Eleve:
    def __init__(self, id_eleve, prenom, nom, etablissement, filiere,
                 maths=None, francais=None, anglais=None,
                 histoire=None, svt=None, physique=None):

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

    def __repr__(self): 
        return (f"Eleve(id={self.id_eleve!r}, "
                f"nom={self.nom!r}, "
                f"filiere={self.filiere!r})")
    
    def __str__(self):  
        moy = self.moyenne()
        moy_str = f"{moy}/20" if moy is not None else "N/A"
        return f"{self.prenom} {self.nom} | {self.filiere} | moy. {moy_str}"

    def __eq__(self, other): 
        if not isinstance(other, Eleve):
            return NotImplemented
        return self.id_eleve == other.id_eleve
    
    def __lt__(self, other):   
        if not isinstance(other, Eleve):
            return NotImplemented
        moyenne_self = self.moyenne() or 0
        moyenne_other = other.moyenne() or 0
        return moyenne_self < moyenne_other

    def notes(self):
        toutes = [self.maths, self.francais, self.anglais, self.histoire, self.svt, self.physique]
        return [n for n in toutes if n is not None]

    def moyenne(self):
        n = self.notes()
        if not n:
            return None
        return round(sum(n) / len(n), 2)
        
    def est_admis(self, seuil=10.0):
        moyenne = self.moyenne()
        return moyenne is not None and moyenne >= seuil
        
    def bulletin(self):
        moyenne = self.moyenne()
        statut = "Admis" if self.est_admis() else "Non admis"
        print(f"{self.prenom} {self.nom} ({self.filiere})")
        print(f"Moyenne : {moyenne if moyenne is not None else 'N/A'}/20 | {statut}")


class Promotion:
    def __init__(self, nom, etablissement, filiere):
        self.nom = nom
        self.etablissement = etablissement
        self.filiere = filiere
        self._eleves = [] 
        
    def __repr__(self):
        return (f"Promotion(nom={self.nom!r}, "
                f"etablissement={self.etablissement!r}, "
                f"filiere={self.filiere!r}) -> {len(self)} élève(s)")

    def __str__(self):  
        return f"{self.nom} | {self.etablissement} | {self.filiere}"

    def __len__(self): 
        return len(self._eleves)

    def __iter__(self):
        return iter(self._eleves)

    def __contains__(self, eleve):
        return eleve in self._eleves

    def ajouter(self, eleve):
        if isinstance(eleve, Eleve):
            if eleve not in self._eleves:
                self._eleves.append(eleve)

    def afficher_eleves(self):
        for eleve in self._eleves:
            print(eleve)

    def moyenne_generale(self):
        moyennes = [eleve.moyenne() for eleve in self._eleves if eleve.moyenne() is not None]
        if not moyennes:
            return None
        return round(sum(moyennes) / len(moyennes), 2)

    def taux_admission(self, seuil=10.0):
        eleves_evalues = [e for e in self._eleves if e.moyenne() is not None]
        if not eleves_evalues:
            return 0.0

        admis = sum(1 for e in eleves_evalues if e.est_admis(seuil))
        return round((admis / len(eleves_evalues)) * 100, 1)

    def classement(self):
        # Utilise automatiquement la méthode __lt__ définie dans Eleve pour trier
        return sorted([e for e in self._eleves if e.moyenne() is not None], reverse=True)

    def eleve_par_id(self, identifiant):
        for eleve in self._eleves:
            if eleve.id_eleve == identifiant:
                return eleve
        return None

    def rapport(self):
        print(f"***** RAPPORT DE LA PROMOTION : {self.nom} *****")
        print(f"Établissement : {self.etablissement} | Filière : {self.filiere}")
        print(f"Nombre d'élèves : {len(self)}")
        print(f"Moyenne générale : {self.moyenne_generale() or 'N/A'}/20")
        print(f"Taux de réussite : {self.taux_admission()}%")
        print("*" * 50)