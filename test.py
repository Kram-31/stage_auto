import pandas as pd
import numpy as np

# Nom du fichier à nettoyer
file_name = "3.5_ListeEntrepriseStage_2024.xlsx"

# Charger le fichier en utilisant la deuxième ligne comme en-tête (header=1)
df = pd.read_excel(file_name, header=1)

# --- 1. Suppression des colonnes vides ou non pertinentes ---
columns_to_drop = [
    'Unnamed: 0',
    'Évaluation de l\'accueil de l\'entreprise',
    'Publication de l\'entreprise sur les Espaces Parents et Élèves pour la recherche de stage',
    'Nombre max stagiaires',
    'Commentaire publié',
    'Montant 2024',
    'Nb',
    'Offres Attribuées',
    'Adresse 4',
    'Libellé postal',
    'Hébergement',
    'Dérogation pour mineurs de plus de 15 ans',
    'Date de dérogation',
    'Famille'
]
df_cleaned = df.drop(columns=columns_to_drop, errors='ignore')

# --- 2. Suppression des lignes de continuation (lignes éparses) ---
# Ceci est crucial pour avoir une seule ligne par entreprise.
# On convertit 'Raison Sociale' en chaîne de caractères, on retire les espaces,
# et on remplace les chaînes vides par NaN pour les supprimer.
df_cleaned['Raison Sociale'] = df_cleaned['Raison Sociale'].astype(str).str.strip()
df_cleaned['Raison Sociale'].replace('', np.nan, inplace=True)

# Suppression des lignes où le nom de l'entreprise est vide
df_cleaned.dropna(subset=['Raison Sociale'], inplace=True)
df_cleaned.reset_index(drop=True, inplace=True)


# --- 3. Nettoyage de la colonne 'N° SIRET' ---
def clean_siret(siret):
    """Convertit un numéro SIRET en chaîne de caractères (14 chiffres)."""
    if pd.isna(siret):
        return np.nan
    try:
        # Convertir les floats (notation scientifique) en string d'entier
        if isinstance(siret, float):
            siret = int(siret)

        # Retirer les caractères non numériques et conserver les 14 premiers chiffres
        siret_str = str(siret).replace('.', '').replace(' ', '').strip()
        return siret_str[:14] if siret_str else np.nan
    except:
        return np.nan

df_cleaned['N° SIRET'] = df_cleaned['N° SIRET'].apply(clean_siret)

# --- 4. Nettoyage final et réorganisation ---

# Retirer les espaces des noms de colonnes
df_cleaned.columns = df_cleaned.columns.str.strip()

# Retirer les espaces des données textuelles
for col in df_cleaned.select_dtypes(include=['object']).columns:
    df_cleaned[col] = df_cleaned[col].str.strip()

# Définir l'ordre des colonnes souhaité
desired_order = [
    'Raison Sociale', 'Dénomination commerciale', 'Siège social',
    'Activité', 'APE', 'Métiers', 'Accepte les stagiaires',
    'Adresse 1', 'Adresse 2', 'Adresse 3', 'Code Postal', 'Ville', 'Pays',
    'Téléphone fixe', 'Téléphone portable', 'No Fax', 'Email', 'Site Web',
    'N° SIRET', 'N° URSAFF',
    'Civilité du responsable', 'Nom du responsable', 'Prénom du responsable', 'Fonction du responsable',
    'Téléphone fixe du responsable', 'Téléphone portable du responsable', 'No Fax du responsable', 'Email du responsable',
    'Horaires', 'Nb de stagiaires de l\'année en cours', 'Nb de stagiaires des années précédentes',
    'Date de création', 'Commentaire', 'Taxe d\'apprentissage', 'Compagnie d\'assurance', 'Police d\'assurance'
]

# Sélectionner et ordonner les colonnes
present_columns = [col for col in desired_order if col in df_cleaned.columns]
df_cleaned = df_cleaned[present_columns]
