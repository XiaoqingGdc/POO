class AnalyseurPromotion:
    SEUIL_ADMISSION = 10.0
    def __init__(self, promotion):
        self.promotion = promotion
        self._stats = {}
    def analyser(self):
        self._stats = {
        "nb_eleves": len(self.promotion),
        "moyenne": self.promotion.moyenne_generale(),
        "taux_admission": self.promotion.taux_admission(self.SEUIL_ADMISSION),
        }
        return self
    
    def rapport(self):
        print(f"\n Eleves : {self._stats.get('nb_eleves', 'N/A')}")
        print(f" Moyenne : {self._stats.get('moyenne', 'N/A')}/20")
        print(f" Admission : {self._stats.get('taux_admission', 'N/A')}%")

    def top_n(self, n=3):
        return self.promotion.classement()[:n]
    
class AnalyseurGenerale(AnalyseurPromotion):
    SEUIL_ADMISSION = 10.0
    def analyser(self):
        super().analyser()
        maths = [e.maths for e in self.promotion if e.maths is not None]
        sciences = [e.svt for e in self.promotion if e.svt is not None]
        lettres = [e.francais for e in self.promotion if e.francais is not None]

        def moy(lst):
            return round(sum(lst) / len(lst), 2) if lst else None
        self._stats["moy_maths"] = moy(maths)
        self._stats["moy_sciences"] = moy(sciences)
        self._stats["moy_lettres"] = moy(lettres)
        return self
    
    def rapport(self):
        print(f"\n [Filiere Generale]")
        super().rapport()
        print(f" Moy. maths : {self._stats.get('moy_maths', 'N/A')}/20")
        print(f" Moy. sciences : {self._stats.get('moy_sciences', 'N/A')}/20")
        print(f" Moy. lettres : {self._stats.get('moy_lettres', 'N/A')}/20")
class AnalyseurTechno(AnalyseurPromotion):
    SEUIL_ADMISSION = 10.0
    def __init__(self, promotion, matiere_dominante="maths"):
        super().__init__(promotion)
        self.matiere_dominante = matiere_dominante
    def analyser(self):
        super().analyser()
        notes = [
        getattr(e, self.matiere_dominante)
        for e in self.promotion
        if getattr(e, self.matiere_dominante, None) is not None
        ]
        self._stats["moy_matiere_dominante"] = (
        round(sum(notes) / len(notes), 2) if notes else None
        )
        return self
    def rapport(self):
        mat = self.matiere_dominante.capitalize()
        print(f"\n [Filiere Technologique — matiere dominante : {mat}]")
        super().rapport()
        print(f" Moy. {mat:<12} : "
        f"{self._stats.get('moy_matiere_dominante', 'N/A')}/20")
    
    
class AnalyseurPro(AnalyseurPromotion):
    SEUIL_ADMISSION = 8.0
    def analyser(self):
        super().analyser()
        self._stats["taux_admission"] = self.promotion.taux_admission(
        self.SEUIL_ADMISSION
        )
        return self
    def rapport(self):
        print(f"\n [Filiere Professionnelle — seuil : {self.SEUIL_ADMISSION}/20]")
        super().rapport()