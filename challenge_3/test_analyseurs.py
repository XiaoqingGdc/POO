"""
test_analyseurs.py 
Teste la hiérarchie d'analyseurs : AnalyseurPromotion et ses trois classes filles.

Les instances Eleve sont créées manuellement depuis notes_brutes.csv

"""

from modeles    import Eleve, Promotion
from analyseurs import (AnalyseurPromotion, AnalyseurGenerale,
                                AnalyseurTechno, AnalyseurPro)

# ── Construction manuelle des trois promotions ───────────────────────────────
# Lycée Victor Hugo — 6 élèves par filière, recopiés depuis notes_brutes.csv

# Filière Générale
promo_gen = Promotion("Générale T1", "Lycée Victor Hugo", "Générale")
for eleve in [
    Eleve("E001","Lucas",  "Martin", "Lycée Victor Hugo","Générale",
          maths=14.5, francais=13.0, anglais=16.0, histoire=12.5, svt=15.0, physique=14.0),
    Eleve("E002","Camille","Dubois", "Lycée Victor Hugo","Générale",
          maths=17.0, francais=16.5, anglais=15.0, histoire=14.0, svt=18.0, physique=17.5),
    Eleve("E003","Nathan", "Leroy",  "Lycée Victor Hugo","Générale",
          maths=9.0,  francais=11.0, anglais=10.5, histoire=8.0,  svt=9.5,  physique=8.5),
    Eleve("E004","Inès",   "Moreau", "Lycée Victor Hugo","Générale",
          maths=12.0, francais=14.0, anglais=13.5, histoire=11.0, svt=12.5, physique=13.0),
    Eleve("E005","Tom",    "Bernard","Lycée Victor Hugo","Générale",
          maths=7.5,  francais=9.0,  anglais=8.0,  histoire=6.5,  svt=None, physique=7.0),
    Eleve("E006","Jade",   "Petit",  "Lycée Victor Hugo","Générale",
          maths=15.5, francais=15.0, anglais=17.0, histoire=16.0, svt=15.5, physique=16.0),
]:
    promo_gen.ajouter(eleve)

# Filière Technologique
promo_tech = Promotion("Technologique T1", "Lycée Victor Hugo", "Technologique")
for eleve in [
    Eleve("E007","Axel",  "Robert",   "Lycée Victor Hugo","Technologique",
          maths=11.0, francais=10.0, anglais=12.0, histoire=9.5,  svt=11.5, physique=12.5),
    Eleve("E008","Léa",   "Simon",    "Lycée Victor Hugo","Technologique",
          maths=13.5, francais=12.0, anglais=11.0, histoire=13.0, svt=14.0, physique=13.0),
    Eleve("E009","Hugo",  "Laurent",  "Lycée Victor Hugo","Technologique",
          maths=8.0,  francais=9.5,  anglais=10.0, histoire=8.5,  svt=7.5,  physique=9.0),
    Eleve("E010","Emma",  "Michel",   "Lycée Victor Hugo","Technologique",
          maths=15.0, francais=13.5, anglais=14.0, histoire=12.0, svt=15.5, physique=14.5),
    Eleve("E011","Rayan", "Garcia",   "Lycée Victor Hugo","Technologique",
          maths=6.5,  francais=8.0,  anglais=7.5,  histoire=7.0,  svt=6.0,  physique=7.0),
    Eleve("E012","Zoé",   "Lefebvre", "Lycée Victor Hugo","Technologique",
          maths=12.5, francais=11.5, anglais=13.0, histoire=11.0, svt=12.0, physique=12.5),
]:
    promo_tech.ajouter(eleve)

# Filière Professionnelle
promo_pro = Promotion("Professionnelle T1", "Lycée Victor Hugo", "Professionnelle")
for eleve in [
    Eleve("E013","Théo",  "Dupont",  "Lycée Victor Hugo","Professionnelle",
          maths=10.0, francais=11.5, anglais=9.0,  histoire=10.5, svt=None, physique=10.0),
    Eleve("E014","Manon", "Bonnet",  "Lycée Victor Hugo","Professionnelle",
          maths=8.5,  francais=10.0, anglais=9.5,  histoire=9.0,  svt=8.0,  physique=9.0),
    Eleve("E015","Louis", "Mercier", "Lycée Victor Hugo","Professionnelle",
          maths=13.0, francais=12.0, anglais=11.5, histoire=12.5, svt=13.0, physique=12.0),
    Eleve("E016","Chloé", "Morin",   "Lycée Victor Hugo","Professionnelle",
          maths=7.0,  francais=8.5,  anglais=8.0,  histoire=7.5,  svt=7.0,  physique=8.0),
    Eleve("E017","Enzo",  "Fournier","Lycée Victor Hugo","Professionnelle",
          maths=11.0, francais=10.5, anglais=12.0, histoire=10.0, svt=11.5, physique=11.0),
    Eleve("E018","Sarah", "Girard",  "Lycée Victor Hugo","Professionnelle",
          maths=9.5,  francais=11.0, anglais=10.0, histoire=10.5, svt=9.0,  physique=10.0),
]:
    promo_pro.ajouter(eleve)

print("Promotions construites :")
print(f"  {promo_gen}   — {len(promo_gen)} élèves")
print(f"  {promo_tech}  — {len(promo_tech)} élèves")
print(f"  {promo_pro}   — {len(promo_pro)} élèves")

# ── 1. Classe mère seule ─────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("1. ANALYSEUR DE BASE — AnalyseurPromotion")
print("=" * 60)

a_base = AnalyseurPromotion(promo_gen)
a_base.analyser()
print()
a_base.rapport()

print(f"\n  top_n(3) :")
for rang, e in enumerate(a_base.top_n(3), 1):
    print(f"    {rang}. {e}")

# ── 2. Classes filles ────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("2. CLASSES FILLES — stats spécifiques à chaque filière")
print("=" * 60)

a_gen  = AnalyseurGenerale(promo_gen)
a_tech = AnalyseurTechno(promo_tech, matiere_dominante="physique")
a_pro  = AnalyseurPro(promo_pro)

for a in [a_gen, a_tech, a_pro]:
    a.analyser()
    a.rapport()

# ── 3. Boucle polymorphe — zéro if/elif ──────────────────────────────────────
print("\n" + "=" * 60)
print("3. BOUCLE POLYMORPHE — même appel, comportements différents")
print("=" * 60)

analyseurs = [a_gen, a_tech, a_pro]

print("\n  Itération sur la liste d'analyseurs — aucun if/elif :\n")
for a in analyseurs:
    a.analyser().rapport()

# ── 4. isinstance() — vérification de l'héritage ─────────────────────────────
print("\n" + "=" * 60)
print("4. HERITAGE — isinstance() vs type()")
print("=" * 60)

print(f"\n  isinstance(a_gen, AnalyseurGenerale)   : {isinstance(a_gen, AnalyseurGenerale)}")
print(f"  isinstance(a_gen, AnalyseurPromotion)  : {isinstance(a_gen, AnalyseurPromotion)}")
print(f"  isinstance(a_tech, AnalyseurGenerale)  : {isinstance(a_tech, AnalyseurGenerale)}")
print(f"  type(a_gen) == AnalyseurGenerale       : {type(a_gen) == AnalyseurGenerale}")
print(f"  type(a_gen) == AnalyseurPromotion      : {type(a_gen) == AnalyseurPromotion}")

# ── 5. Seuil d'admission Pro vs classe mère ───────────────────────────────────
print("\n" + "=" * 60)
print("5. SEUIL D'ADMISSION — AnalyseurPro (8.0) vs classe mère (10.0)")
print("=" * 60)

a_base_pro  = AnalyseurPromotion(promo_pro)
a_pro_fille = AnalyseurPro(promo_pro)
a_base_pro.analyser()
a_pro_fille.analyser()

taux_mere  = a_base_pro._stats["taux_admission"]
taux_fille = a_pro_fille._stats["taux_admission"]

print(f"\n  Mêmes données — filière Professionnelle ({len(promo_pro)} élèves)")
print(f"  Taux avec seuil 10.0 (classe mère)  : {taux_mere}%")
print(f"  Taux avec seuil  8.0 (AnalyseurPro) : {taux_fille}%")
print(f"  Différence visible                   : {taux_mere != taux_fille}")

# ── 6. super() — les stats de base sont toujours présentes ───────────────────
print("\n" + "=" * 60)
print("6. SUPER() — stats de base héritées + stats spécifiques")
print("=" * 60)

a_gen.analyser()
print(f"\n  Clés dans AnalyseurGenerale._stats :")
for cle, val in a_gen._stats.items():
    print(f"    {cle:<22} : {val}")

# ── 7. SEUIL_ADMISSION — attribut de classe par filière ──────────────────────
print("\n" + "=" * 60)
print("7. ATTRIBUT DE CLASSE — SEUIL_ADMISSION")
print("=" * 60)

print(f"\n  AnalyseurPromotion.SEUIL_ADMISSION : {AnalyseurPromotion.SEUIL_ADMISSION}")
print(f"  AnalyseurGenerale.SEUIL_ADMISSION  : {AnalyseurGenerale.SEUIL_ADMISSION}")
print(f"  AnalyseurTechno.SEUIL_ADMISSION    : {AnalyseurTechno.SEUIL_ADMISSION}")
print(f"  AnalyseurPro.SEUIL_ADMISSION       : {AnalyseurPro.SEUIL_ADMISSION}")