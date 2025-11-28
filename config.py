import os
from dotenv import load_dotenv

# Charger variables depuis .env
load_dotenv()

# ==========================================
# CONFIGURATION SMTP
# ==========================================
SMTP_EMAIL = os.getenv('SMTP_EMAIL', 'kaced.kamal.ciel@gmail.com')
SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', '')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))

# ==========================================
# FICHIERS ET CHEMINS
# ==========================================
CHEMIN_EXCEL = os.getenv('CHEMIN_EXCEL', 'Liste_stage_test.xlsx')
CHEMIN_CV = os.getenv('CHEMIN_CV', 'Mon_cv.pdf')
CHEMIN_REFERENTIEL = os.getenv('CHEMIN_REFERENTIEL', 'Referentiel_bts.pdf')

# ==========================================
# PARAMÈTRES D'ENVOI
# ==========================================
DELAI_ENTRE_ENVOIS = int(os.getenv('DELAI_ENTRE_ENVOIS', '10'))
FORMAT_DATE = '%d/%m/%Y'

# Variable de test: date du jour pour tests rapides
from datetime import datetime as _datetime
TEST_DATE = '01/01/2027'

# ==========================================
# COLONNES EXCEL - Noms réels des colonnes dans le fichier
# ==========================================
COLONNES = [
    'ID_RECRUTEUR',
    'ENTREPRISE',
    'POSTE_CIBLE',
    'CODE_POSTAL',
    'VILLE',
    'PAYS',
    'EMAIL_ENTREPRISE',
    'CIVILITE_RESP',
    'NOM_RESP',
    'PRENOM_RESP',
    'POSTE_RESP',
    'MAIL_RESPONSABLE',
    'STATUT',
    'DATE_ENVOI'
]

# ==========================================
# LOGGING
# ==========================================
LOG_LEVEL = 'INFO'
LOG_FILE = 'stage_auto.log'

print('[CONFIG] Configuration chargée depuis .env')
