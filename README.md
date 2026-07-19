# POO — Programmation Orientée Objet en Python  Edustat

Ce dépôt regroupe les exercices, tests et notes réalisés dans le cadre du brief hebdomadaire consacré à la Programmation Orientée Objet (POO) en Python.  
Ce travail s’inscrit dans mon parcours de formation Data Analyst.

---

## 📁 Structure du projet

```
POO/
├── challenge_1/        # Challenge 1 : classes, objets, méthodes
├── challenge_2/        # Challenge 2 : méthodes spéciales, classe Promotion
├── challenge_3/        # Challenge 3 : héritage, polymorphisme, analyseurs
├── challenge_4/        # Challenge 4 : modules, packages, classmethod & staticmethod
├── edustat/            # Challenge 5 : DataProfiler, encapsulation et héritage
├── notes.py            # Notes personnelles et exemples de code
├── requirements.txt    # Dépendances Python
└── .gitignore
```
---

## 🎯 Objectifs 

### 🔸 Comprendre les bases de la POO challenge 1
- Définition de classes et création d’objets  
- Attributs d’instance et de classe  
- Méthodes simples (notes(), moyenne(), est_admis())
- 1er test manuel

### 🔸 Approfondir les mécanismes avancés challenge 2
 
- Comparaison d’objets (`__lt__`, `__eq__`)  
- Représentation d'objet (`__str__`, `__repr__`)  
- Itération et contenuers ('__len__', '__iter__', '__contains__')
- Tri personnalisé avec sorted() 
- Construction d’une classe Promotion complète
- Tests unitaires

### 🔸 Comprendre Heritage challenge 3
- Création d’une classe mère AnalyseurPromotion
- Classes filles spécialisées : AnalyseurGenerale,AnalyseurTechno,AnalyseurPro
- Utilisation de super()
- Vérification des types avec isinstance()
- Comprendre polymorphisme : une même méthode → comportements différents


### 🔸 edustat(challenge 4) — Modules, Packages & Méthodes de classe
- comprendre @classmethod & @staticmethod et utiliser dans les classs Eleve Promotion
- Structuration propre et modulaire d’un projet Python avec l'ensemble de fichier construis depuis début de la semaine
- Lecture, nettoyage et transformation de données CSV généré par notes.py 

### 🔸 edustat(challenge 5) — Mini-projet : DataProfiler
-  un mini projet pour comprendre le dataset, taille,doublon,type, etc, création :profiler.py 
-  encapsuler ce workflowdans une classe réutilisable : le DataProfiler.
-  tout assemblé en un outil concret que nous pouvons réutiliser sur n'importe quel DataFrame. 

## 🚀 Installation

```bash
git clone https://github.com/XiaoqingGdc/POO.git
cd POO
pip install -r requirements.txt
