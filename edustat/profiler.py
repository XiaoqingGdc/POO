import pandas as pd

class DataProfiler:
    def __init__(self, df, nom="Sans nom"):
        if not isinstance(df, pd.DataFrame):
            raise TypeError
        self._df = df.copy()
        self.nom = nom
        self._df = df.copy() 
    
    def __repr__(self):
        return (f"DataProfiler(nom={self.nom}\n"
                f"Nbr lignes = {len(self._df)}\n"
                f"Nbr colonnes = {self._df.shape[1]})")
                
    def __len__(self):
        return len(self._df)
    
    def __str__(self):
        return f"[{self.nom}] {self._df.shape[0]} lignes x {self._df.shape[1]} colonnes"
    
    @classmethod
    def depuis_csv(cls, chemin, nom=None, separateur=";"):
        df = pd.read_csv(chemin, sep=separateur, skip_blank_lines=True)
        df = df.dropna(how='all')
        if 'id' in df.columns:
            df = df.dropna(subset=['id'])
        nom = nom or chemin.split("/")[-1].replace(".csv", "")
        return cls(df, nom)

    def types_colonnes(self):
        resultat ={}
        for valeur, description in self._df.dtypes.items():
            resultat[valeur] = str(description)
        return resultat
    
    def valeurs_manquantes(self):
        nb_valu_m = self._df.isna().sum()
        serie_manquants= nb_valu_m[nb_valu_m > 0]
        return pd.DataFrame(serie_manquants, columns=["manquantes"])
    
    def doublons(self):
        nb_dupli = self._df.duplicated().sum()
        return int(nb_dupli)
    
    def stats_numeriques(self):
        return self._df.describe(include="number").loc[['mean', 'min', 'max']].T

    def profiler(self):
        self._stats = {
        "nom": self.nom,
        "nb_lignes": self._df.shape[0],
        "nb_colonnes": self._df.shape[1],
        "types_colonnes": self.types_colonnes(),
        "nb_doublons": self.doublons(),
        "valeurs_manquantes": self.valeurs_manquantes(),
        }
        return self

    def rapport(self):
        print(
        f"nom : {self._stats.get('nom')}\n"
        f"nb_lignes_total : {self._stats.get('nb_lignes')}\n"
        f"nb_colonne_total : {self._stats.get('nb_colonnes')}\n"
        f"nb_doublons : {self._stats.get('nb_doublons')}\n"
        f"nb_manquant : {self._stats.get('valeurs_manquantes')}\n"
        f"type : {self._stats.get('types_colonnes')}"
        )
        return self

    def exporter(self, chemin: str):
        if not self._stats:
            self.profiler()
        lignes = [{"indicateur": k, "valeur": str(v)} for k, v in self._stats.items()]
        pd.DataFrame(lignes).to_csv(chemin, sep=";", index=False, encoding="utf-8")
        print(f"Profil exporté → {chemin}")
        return self

class ProfileurNotes(DataProfiler):
    MATIERES = ["maths", "francais", "anglais", "histoire", "svt", "physique"]

    def __init__(self, df, nom="ProfilNotes"):
        super().__init__(df, nom)
        for matiere in self.MATIERES:
            if matiere in self._df.columns:
                self._df[matiere] = pd.to_numeric(self._df[matiere], errors='coerce')

    def moyenne_par_matiere(self):
        matieres_presentes = [m for m in self.MATIERES if m in self._df.columns]
        if not matieres_presentes:
            return None
        moyennes = self._df[matieres_presentes].mean().round(2)
        return moyennes.sort_values(ascending=False)
    
    def moyennes_par_matiere(self):
        return self.moyenne_par_matiere()

    def moyenne_par_filiere(self):
        matieres_presentes = [m for m in self.MATIERES if m in self._df.columns]
        if "filiere" not in self._df.columns or not matieres_presentes:
            return None
        df_tmp = self._df.copy()
        df_tmp["moyenne_eleve"] = df_tmp[matieres_presentes].mean(axis=1)
        return df_tmp.groupby("filiere")["moyenne_eleve"].mean().round(2)

    def moyennes_par_etablissement(self):
        matieres_presentes = [m for m in self.MATIERES if m in self._df.columns]
        if "etablissement" not in self._df.columns or not matieres_presentes:
            return pd.Series(dtype=float)
        df_tmp = self._df.copy()
        df_tmp["moyenne_eleve"] = df_tmp[matieres_presentes].mean(axis=1)
        return df_tmp.groupby("etablissement")["moyenne_eleve"].mean().round(2)   
     

    def taux_admission_global(self, seuil):
        matieres_presentes = [m for m in self.MATIERES if m in self._df.columns]
        if not matieres_presentes:
            return 0.0
        moyennes_eleves = self._df[matieres_presentes].mean(axis=1)
        taux = (moyennes_eleves >= seuil).mean() * 100
        return round(taux, 2)


    def profiler(self):
        super().profiler()
        self._stats["moyenne_par_matiere"] = self.moyenne_par_matiere()
        self._stats["moyenne_par_filiere"] = self.moyenne_par_filiere()
        self._stats["moyenne_par_etablissement"] = self.moyennes_par_etablissement()
        return self

    def rapport(self):
        if not self._stats:
            self.profiler()
        super().rapport()
        print(f"Moyennes par matière :\n{self._stats.get('moyenne_par_matiere')}")
        print(f"Moyennes par filière :\n{self._stats.get('moyenne_par_filiere')}")
        print(f"Moyennes par établissement :\n{self._stats.get('moyenne_par_etablissement')}")
        return self

      