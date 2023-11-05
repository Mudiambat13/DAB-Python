solde = 0

while True:
  print("""
  1. Retrait
  2. Dépôt 
  3. Solde
  4. Quitter
  """)

  choix = input("Votre choix: ")

  if choix == "1":
    retrait = input("Montant à retirer: ")
    try:
      retrait = float(retrait)
    except ValueError:
      print("Montant invalide. Veuillez entrer un nombre.")
      continue
    
    if retrait > solde:
      print("Solde insuffisant!")
    else:
      solde -= retrait
      print(f"Retrait effectué ! Nouveau solde: {solde}")

  elif choix == "2":
    depot = input("Montant à déposer: ")
    try:
      depot = float(depot)  
    except ValueError:
      print("Montant invalide. Veuillez entrer un nombre.")
      continue
    
    solde += depot
    print(f"Dépôt effectué ! Nouveau solde: {solde}")

  elif choix == "3":
    print(f"Votre solde est de {solde}")

  elif choix == "4":
    print("Au revoir !")
    break
  
  else:
    print("Choix invalide")
