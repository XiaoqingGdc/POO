class AnalyseurPromotion: # classe mère

    SEUIL_ADMISSION = 10.0 # attribut de CLASSE( partagé )

    def __init__(self, promotion):
        self.promotion = promotion
        self._stats = {}

    def analyser (self):
        self._stats = {
            "nb_eleves" : len(self.promotion),
            "moyennes" : self.promotion.moyenne_generale(),
            "taux_admission" : self.promotion.taux_admission(self.SEUIL_ADMISSION)
            }
        return self 
    
    def rapport(self):
        print(
            f"Établissement : {self.promotion.etablissement}\n"
            f"Filière : {self.promotion.filiere}\n"
            f"Nombre d'élèves : {self._stats.get('nb_eleves')}\n"
            f"Moyenne générale : {self._stats.get('moyennes')}\n"
            f"Taux d'Admission : {self._stats.get('taux_admission')}%\n"
        )

    def top_n(self,n=3):
        return self.promotion.classement()[:n]


class AnalyseurGenerale(AnalyseurPromotion):
    def analyser(self):
        super().analyser()

        notes_maths = [eleve.maths for eleve in self.promotion if eleve.maths is not None]
        moy_maths = round(sum(notes_maths)/len(notes_maths), 2) if notes_maths else None

        notes_sciences = [
            note for eleve in self.promotion
            for note in [eleve.svt, eleve.physique]
            if note is not None
        ]
        moy_sciences = round(sum(notes_sciences)/len(notes_sciences),2) if notes_sciences else None

        note_lettres = [
            note for eleve in self.promotion
            for note in [eleve.francais, eleve.histoire]
            if note is not None
        ]
        moy_lettres = round(sum(note_lettres)/len(note_lettres),2) if note_lettres else None                       
      
        self._stats ["moyenne_maths" ]= moy_maths
        self._stats ["moyenne_science"] = moy_sciences
        self._stats ["moyenne_lettres"]= moy_lettres
        return self 


    def rapport(self):
        super().rapport()
        print(
        f"Moyenne Maths : {self._stats.get('moyenne_maths')}\n"
        f"Moyenne Sciences : {self._stats.get('moyenne_science')}\n"
        f"Moyenne Lettres : {self._stats.get('moyenne_lettres')}\n"
    )



class AnalyseurTechno (AnalyseurPromotion): #classe fille
    def __init__(self, promotion, matiere_dominante="maths"):
        super().__init__(promotion)
        self.matiere_dominante = matiere_dominante

    def analyser(self):
        super().analyser()

        notes = [
            getattr(eleve,self.matiere_dominante)
            for eleve in self.promotion
            if getattr(eleve,self.matiere_dominante) is not None
            ]

        moyenne_matiere_dominante = round(sum(notes)/len(notes),2) if notes else None

        self._stats['matiere_dominante'] = self.matiere_dominante
        self._stats['moyenne_matiere_dominante'] = moyenne_matiere_dominante

        return self

    def rapport(self):
        super().rapport()
        print(
            f'La matière dominante est : {self._stats.get("matiere_dominante")}\n'
            f'La moyenne de la matière dominante est : {self._stats.get("moyenne_matiere_dominante")}\n'
        )



class AnalyseurPro (AnalyseurPromotion): #classe fille
    SEUIL_ADMISSION = 8.0

    def analyser(self):
        super().analyser()

        eleve_admis =[]
        for eleve in self.promotion:
            note_moyenne = eleve.moyenne() or 0
            if note_moyenne >= self.SEUIL_ADMISSION:
                eleve_admis.append(eleve)
        nb_eleve_tt = len(self.promotion)
        if nb_eleve_tt ==0:
            taux_admission = None
        else:    
            taux_admission = round(len(eleve_admis)/nb_eleve_tt*100,2)

        self._stats["taux_admission"]=taux_admission
        return self
    

    def rapport(self):
        super().rapport()
        print(
            f"Taux d'admission est {self._stats.get('taux_admission')}% quand la seuil d'admission est {self.SEUIL_ADMISSION}"
        )
