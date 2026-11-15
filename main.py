l=[""]
print("=== GESTION DES TÂCHES ===")
print("1. Ajouter une tâche 2. Afficher 3. Rechercher 0. Quitter")
e=input("votre choix :")
while e==1:
    print("votre choix :",e)
    t=input("Titre de la tâche :")
    while t!="":
        t=input("Titre de la tâche :")
        t=t+l
if e==2 and l!="":
    k=0
    for i in l:
        print(i)
        k=l.index[i]
        print(k)
else:
    print("error")
if e==3:
    o=input(" mot-clé :")

    