"""
test_modeles.py 
Teste les méthodes spéciales d'Eleve et la classe Promotion.
Données : 6 élèves de la filière Générale, Lycée Victor Hugo (notes_brutes.csv).
"""

from modeles import Eleve, Promotion

# ── Construction des instances ──────────────────────────────────────────────
# 6 élèves recopiés depuis notes_brutes.csv — même établissement, même filière

e1 = Eleve("E001", "Lucas",   "Martin", "Lycée Victor Hugo", "Générale",
           maths=14.5, francais=13.0, anglais=16.0,
           histoire=12.5, svt=15.0, physique=14.0)

e2 = Eleve("E002", "Camille", "Dubois", "Lycée Victor Hugo", "Générale",
           maths=17.0, francais=16.5, anglais=15.0,
           histoire=14.0, svt=18.0, physique=17.5)

e3 = Eleve("E003", "Nathan",  "Leroy",  "Lycée Victor Hugo", "Générale",
           maths=9.0, francais=11.0, anglais=10.5,
           histoire=8.0, svt=9.5, physique=8.5)

e4 = Eleve("E004", "Inès",    "Moreau", "Lycée Victor Hugo", "Générale",
           maths=12.0, francais=14.0, anglais=13.5,
           histoire=11.0, svt=12.5, physique=13.0)

e5 = Eleve("E005", "Tom",     "Bernard","Lycée Victor Hugo", "Générale",
           maths=7.5, francais=9.0, anglais=8.0,
           histoire=6.5, svt=None, physique=7.0)

e6 = Eleve("E006", "Jade",    "Petit",  "Lycée Victor Hugo", "Générale",
           maths=15.5, francais=15.0, anglais=17.0,
           histoire=16.0, svt=15.5, physique=16.0)

eleves = [e1, e2, e3, e4, e5, e6]

# ── 1. Vérification de __repr__ et __str__ ──────────────────────────────────
print("=" * 60)
print("1. REPRESENTATIONS")
print("=" * 60)
print("\n")
print("repr() — représentation technique :")
for e in eleves:
    print(" ", repr(e))

print("\n")
print("str() — représentation lisible :")
for e in eleves:
    print(e)

# ── 2. Construction de la Promotion ─────────────────────────────────────────
print("\n" + "=" * 60)
print("2. CONSTRUCTION DE LA PROMOTION")
print("=" * 60)

promo = Promotion("Générale T1", "Lycée Victor Hugo", "Générale")
for e in eleves:
    promo.ajouter(e)
print("\n")
print(f" repr(promo) : {repr(promo)}")
print(f" str(promo)  : {str(promo)}")
print(f" len(promo)  : {len(promo)}")

# ── 3. Rapport complet ───────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("3. RAPPORT COMPLET")
print("=" * 60)

promo.rapport()

# ── 4. Classement complet ────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("4. CLASSEMENT COMPLET (du meilleur au moins bon)")
print("=" * 60)

print()
for rang, eleve in enumerate(promo.classement(), start=1):
    print(f"  {rang}. {eleve}")

# ── 5. Opérateur in — test de __contains__ ──────────────────────────────────
print("\n" + "=" * 60)
print("5. OPERATEUR in — __contains__")
print("=" * 60)
print("\n")

print(f" e1 (Lucas Martin) in promo   : {e1 in promo}")   # True — ajouté
print(f" e2 (Camille Dubois) in promo : {e2 in promo}")    # True — ajouté
# Élève non ajouté à la promotion
e_absent = Eleve("E099", "Inconnu", "Absent", "Autre lycée", "Générale")
print(f" e_absent in promo            : {e_absent in promo}")  # False
print("\n")
# ── 6. sorted() vs classement() ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("6. sorted(promo) vs promo.classement()")
print("=" * 60)

print("sorted(promo) — utilise __iter__ et __lt__ :")
for rang, eleve in enumerate(sorted(promo), start=1):
    print(f"  {rang}. {eleve.prenom} {eleve.nom} — moy. {eleve.moyenne()}")

print("\n promo.classement() — même résultat, ordre décroissant :")
for rang, eleve in enumerate(promo.classement(), start=1):
    print(f"  {rang}. {eleve.prenom} {eleve.nom} — moy. {eleve.moyenne()}")

# Vérification que les deux listes contiennent les mêmes élèves
tries_asc  = sorted(promo)
tries_desc = promo.classement()
print(f"\n Même contenu (ordre inversé) : "
      f"{[e.id_eleve for e in tries_asc] == [e.id_eleve for e in reversed(tries_desc)]}")

# ── 7. Égalité — test de __eq__ ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("7. EGALITE — __eq__")
print("=" * 60)

e1_copie = Eleve("E001", "Lucas", "Martin", "Lycée Victor Hugo", "Générale",
                 maths=14.5, francais=13.0, anglais=16.0,
                 histoire=12.5, svt=15.0, physique=14.0)

print(f"\n e1 == e1_copie (même id)  : {e1 == e1_copie}")   # True
print(f" e1 == e2 (ids différents) : {e1 == e2}")            # False
print(f" e1 is e1_copie            : {e1 is e1_copie}")      # False — objets distincts

# ── 8. Cas limite — élève avec une note manquante ───────────────────────────
print("\n" + "=" * 60)
print("8. CAS LIMITE — note manquante (E005 Tom Bernard, svt=None)")
print("=" * 60)
print("\n")
print(f" Notes disponibles : {e5.notes()}")
print(f" Moyenne (5 notes) : {e5.moyenne()}")
print(f" Est admis (10.0)  : {e5.est_admis()}")
print(f" Est admis (8.0)   : {e5.est_admis(seuil=8.0)}")

# ── 9. Résumé des indicateurs ────────────────────────────────────────────────
print("\n" + "=" * 60)
print("9. INDICATEURS DE LA PROMOTION")
print("=" * 60)
print("\n")
print(f" Moyenne générale     : {promo.moyenne_generale()}/20")
print(f" Taux admission (10)  : {promo.taux_admission(seuil=10.0)}%")
print(f" Taux admission (12)  : {promo.taux_admission(seuil=12.0)}%")
print(f" Taux admission (8)   : {promo.taux_admission(seuil=8.0)}%")