# Demander à l'utilisateur de saisir le montant 
# La fonction input() renvoie une chaîne de caractères, il faut la convertir en nombre
try: 
    destinataire=float(input("veuillez entrer le numero de destinataire:")) 
    montant = float(input("Veuillez entrer le montant de la transaction : ")) 
except ValueError: 
    print("Entrée invalide. Veuillez entrer un nombre.") 
    exit() # Quitter le programme si la saisie est incorrecte 
 
# Variables par défaut (vous pouvez aussi les demander en utilisant input()) 
expediteur = "Daniel songo (0812403653)" 
destinataire = "Rosaline (0812403653)" 
date_heure = "17/09/2025 09:44" 
reference = "TEST-001" 
 
# Calculer les frais selon la règle 
# Les frais sont de 1% du montant 
frais = montant * 0.01 
 
# Si les frais calculés sont inférieurs à 100 CDF, on prend 100 
if frais < 100: 
    frais = 100 
 
# Le total débité est le montant plus les frais 
total_debite = montant + frais 
 
# Afficher le reçu avec les f-strings pour plus de lisibilité 
print("\n=== REÇU ===") 
print(f"Date/Heure : {date_heure}") 
print(f"Expéditeur : {expediteur}") 
print(f"Destinataire : {destinataire}") 
print(f"Montant : {montant} CDF") 
print(f"Frais : {frais} CDF") 
print(f"Total débité : {total_debite} CDF") 
print(f"Référence : {reference}")