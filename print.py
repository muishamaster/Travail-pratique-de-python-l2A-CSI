# 1. Déclarer les variables par défaut 
montant = 25000.00  # Montant de la transaction 
expediteur = "Daniel songo(+24397000000)" 
destinataire = "Rosaline (+24382000000)" 
date_heure = "17/09/2025 09:44" 
reference = "TEST-001" 
 
# 2. Calculer les frais selon la règle 
# Les frais sont de 1% du montant 
frais = montant * 0.01 
 
# Si les frais calculés sont inférieurs à 100 CDF, on prend 100 
if frais < 100: 
    frais = 100 
 
# Leq total débité est le montant plus les frais 
total_debite = montant + frais 
 
# 3. Afficher un premier reçu avec les f-strings 
print("=== REÇU (f-string) ===") 
print(f"Date/Heure : {date_heure}") 
print(f"Expéditeur : {expediteur}") 
print(f"Destinataire : {destinataire}") 
print(f"Montant : {montant} CDF") 
print(f"Frais : {frais} CDF") 
print(f"Total débité : {total_debite} CDF") 
print(f"Référence : {reference}") 
 
# Un séparateur pour la clarté 
print("\n" + "="*30 + "\n") 
 
# 4. Afficher le même reçu avec la méthode str.format() 
print("=== REÇU (str.format) ===") 
print("Date/Heure : {}".format(date_heure)) 
print("Expéditeur : {}".format(expediteur)) 
print("Destinataire : {}".format(destinataire)) 
print("Montant : {} CDF".format(montant)) 
print("Frais : {} CDF".format(frais)) 
print("Total débité : {} CDF".format(total_debite)) 
print("Référence : {}".format(reference)) 
 
# Un autre séparateur 
print("\n" + "="*30 + "\n") 
 
# 5. Afficher le même reçu avec l'opérateur % 
print("=== REÇU (% operator) ===") 
print("Date/Heure : %s" % date_heure) 
print("Expéditeur : %s" % expediteur) 
print("Destinataire : %s" % destinataire)