# Chemin vers votre fichier CSV
fichier_csv = "dataset.csv"

# Chemin vers le nouveau fichier CSV
nouveau_fichier_csv = "data.csv"

# Ouvrir le fichier CSV en lecture
with open(fichier_csv, 'r', encoding='utf-8') as f_in:
    # Lire les lignes du fichier
    lignes = f_in.readlines()

# Ouvrir le fichier CSV en écriture
with open(nouveau_fichier_csv, 'w', encoding='utf-8') as f_out:
    # Parcourir chaque ligne
    for ligne in lignes:
        # Supprimer les guillemets en début et en fin de ligne
        ligne = ligne.strip().strip('"')
        # Remplacer chaque virgule en dehors des deux premières colonnes par ","
        ligne = ligne.replace(',', '","', 2)
        # Écrire la ligne dans le nouveau fichier CSV
        f_out.write(f'"{ligne}"\n')

print("Les données ont été écrites dans le fichier:", nouveau_fichier_csv)
