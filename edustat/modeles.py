class Eleve:
    def __init__(self,id_eleve,prenom,nom,etablissement,filiere,maths=None, francais=None, anglais=None,
histoire=None, svt=None, physique=None,):

        self.id_eleve = id_eleve
        self.prenom = prenom
        self.nom = nom
        self.etablissement = etablissement
        self.filiaire = filiere

        self.maths = maths
        self.francais = francais
        self.histoire = histoire
        self.svt = svt
        self.physique = physique
        self.anglais = anglais 

    def __repr__(self):
        return f"Eleve(id_eleve = {self.id_eleve}, nom = {self.nom},filiaire = {self.filiaire})"
    
    def __str__(self):
        moyenne = self.moyenne()
        return f"({self.prenom} {self.nom} | {self.filiaire}| {moyenne}/20)"
    
    def __eq__(self,other):
        if not isinstance(other,Eleve):
            return False
        return self.id_eleve == other.id_eleve
    
    def __lt__(self,other): #comparaison sur moyenne() (None vaut 0)
        m1 = self.moyenne()
        moyenne1 = m1 if m1 is not None else 0
        m2 = other.moyenne()
        moyenne2= m2 if m2 is not None else 0
        return moyenne1 < moyenne2

    def notes(self):
        liste_notes=[self.maths,self.francais,self.anglais,self.histoire,self.svt,self.physique]
        notes = [float(note) for note in liste_notes if note is not None]
        return notes
    
    def moyenne(self):
        if len(self.notes())==0:
            return None
        else:
            total = sum(self.notes())
            nb = len(self.notes())
            moyenne = round(total/nb,2)
            return moyenne
    
    def est_admis(self,seuil=10.0):
        self.seuil = seuil
        moyenne = self.moyenne() or 0
        return moyenne >= seuil
    
    def bulletin(self):
        print(f"Eleve : {self.id_eleve}, {self.prenom} {self.nom}")
        print(f"Bulletin : {self.notes()}")
        print(f"Note moyenne : {self.moyenne()}")
        print(f"Est admis : {self.est_admis()}")
        moyenne = self.moyenne() or 0
        if moyenne >= 12.0:
            print("mention Assez bien")

    def goodat_maths(self):
        list_goodatmaths = []
        if self.maths is not None:
            moyenne = self.moyenne()
            if moyenne is not None and float(self.maths)>moyenne:
                list_goodatmaths.append(self)
        return list_goodatmaths

class Promotion:
    def __init__(self,nom,etablissement,filiere):
        self.nom = nom
        self.etablissement = etablissement
        self.filiere = filiere
        self.eleves =[]
    
    def __repr__(self):
        return f"etablissemnt = {self.etablissement}, filiere = {self.filiere}"

    def __str__(self):
        return f"{self.etablissement} | {self.filiere}"
    
    def __len__(self):
        return len(self.eleves)
    
    def __iter__(self):
        return iter(self.eleves)
    
    def __contains__(self,eleve):
        return eleve in self.eleves
    
    def ajouter(self,eleve):
        return self.eleves.append(eleve)
    
    def moyenne_generale(self):
        notes_total =[]
        for eleve in self.eleves: 
            if eleve.moyenne() is not None:
                notes_total.append(eleve.moyenne()) 
        nb_eleve_anote = len(notes_total)
        if nb_eleve_anote ==0:
            return None
        else:
            moyenne_generale= round(sum(notes_total)/nb_eleve_anote,2)
            return float(moyenne_generale)

    def taux_admission(self,seuil = 10.0):
        eleve_admise  = []
        for eleve in self.eleves:
            if eleve.est_admis(seuil):
                eleve_admise.append(eleve)
        nb_eleve_admise = len(eleve_admise)
        nb_eleve_total = len(self.eleves)
        if nb_eleve_total == 0:
            return None
        taux_admission = round(nb_eleve_admise/nb_eleve_total*100,2)
        return taux_admission

    def classement(self):
        return sorted(self.eleves,reverse = True)

    def rapport(self):
        taux = self.taux_admission()
        taux_affiche = taux if taux is not None else 0

        print (
        f"Nom d'établissement : {self.etablissement}\n"
        f"Nom de filiaire : {self.filiere}\n"
        f"Nombre d'élèves dans la Promotion :{len(self.eleves)}\n"
        f"Moyenne général est {self.moyenne_generale()}\n"
        f"Taux d'admission est {taux_affiche} %"
        )

    def eleve_par_id(self,identifiant):
        for eleve in self.eleves:
            if eleve.id_eleve == identifiant:
                return eleve
        return None
