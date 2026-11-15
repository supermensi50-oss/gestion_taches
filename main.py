taches=[]
choix=""
while choix!="0":
    print()
    print("=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche   2. Afficher   3. Rechercher   0. Quitter")
    choix=input("Votre choix : ")
    if choix=="1":
        titre=input("Titre de la tâche : ")
        if titre=="":
            print("Erreur : le titre ne peut pas être vide.")
        else:
            taches.append(titre)
            print("Tâche ajoutée avec succès.")
    elif choix=="2":
        if len(taches)==0:
            print("Aucune tâche pour le moment.")
        else:
            numero=1
            for titre in taches:
                print(numero,"-",titre)
                numero=numero+1
    elif choix=="3":
        mot=input("Mot-clé : ").lower()
        if mot=="":
            print("Erreur : le mot-clé ne peut pas être vide.")
        else:
            trouve=False
            numero=1
            for titre in taches:
                if mot in titre.lower():
                    print(numero,"-",titre)
                    trouve=True
                numero=numero+1
            if trouve==False:
                print("Aucune tâche trouvée.")
    elif choix=="0":
        print("Au revoir !")
    else:
        print("Erreur : option invalide.")
