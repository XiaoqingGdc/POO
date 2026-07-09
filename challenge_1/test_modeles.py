from modeles import Eleve

eleve_01 = Eleve("E001", "Lucas", "Martin", "Victor Hugo", "Generale", 14.5, 13.0, 16.0,12.5,15.0,14.0)
eleve_02 = Eleve("E002","Camille","Dubois","Lycée Victor Hugo","Générale",17.0, 16.5, 15.0, 14.0, 18.0, 17.5)
eleve_03 = Eleve("E003","Nathan","Leroy","Lycée Victor Hugo","Générale", 9.0, 11.0, 10.5, 8.0, 9.5, 8.5)
eleve_04 = Eleve("004","Inès","Moreau","Lycée Victor Hugo","Générale",12.0, 14.0, 13.5, 11.0, 12.5, 13.0)


list_test = [eleve_01,eleve_02,eleve_03,eleve_04]
for eleve in list_test:
    print(eleve.bulletin())
    print(eleve.notes())
    print(eleve.mention())



list_eleve_mat =[]
for eleve in list_test:
    if eleve.is_goodat_math():
        list_eleve_mat.append(eleve) 
nom_list_eleve_mat = [eleve.nom for eleve in list_eleve_mat]
print(f"Elève(s) avec moyenne en maths > moyenne générale :{nom_list_eleve_mat}")






    
        
