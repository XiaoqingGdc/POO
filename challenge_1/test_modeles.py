from modeles import Eleve

e = Eleve("E001", "Lucas", "Martin", "Generale",
          maths=14.5, francais=13.0, anglais=16.0)

print(e.moyenne())
print(e.est_admis())
e.bulletin


promotion = [
    Eleve("E001", "Lucas", "Martin", "Generale",
          maths=14.5, francais=13.0, anglais=16.0,
          histoire=12.5, svt=15.0, physique=14.0),
    
    Eleve("E002", "Camille", "Dubois", "Generale",
          maths=17.0, francais=16.5, anglais=15.0,
          histoire=14.0, svt=18.0, physique=17.5),
    
    Eleve("E003", "Nathan", "Leroy", "Generale",
          maths=9.0, francais=11.0, anglais=10.5,
          histoire=8.0, svt=9.5, physique=8.5)
]

for eleve in promotion:
    eleve.bulletin()

non_admis = [e for e in promotion if not e.est_admis()]
