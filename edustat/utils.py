import pandas as pd
from .modeles import Eleve, Promotion
from .analyseurs import AnalyseurPromotion

# implémente charger_notes qui utilise Eleve.depuis_dic
def charger_notes(chemin_csv: str):

    df = pd.read_csv(chemin_csv, sep=";").fillna("")
    df = df.drop_duplicates()  # supprime les doublons stricts

    promotions = {}
    for ligne in df.to_dict("records"):
        eleve = Eleve.depuis_dict(ligne)
        nom_ecole = eleve.etablissement or "Inconnu"
        if nom_ecole not in promotions:
            promotions[nom_ecole] = Promotion(nom_ecole, nom_ecole, eleve.filiere)
        promotions[nom_ecole].ajouter(eleve)

    return promotions  # Retourne un dict {nom_etablissement: Promotion}
