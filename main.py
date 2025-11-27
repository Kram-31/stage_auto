import smtplib
import time
import pandas as pd
#// module pour construire le mail 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

mon_email = "kamal.kaced@lycee-mirepoix.fr"
mon_mot_de_passe = ""
smtp_server = "smtp.gmail.com"
smtp_port = 587
fichier_cv = "Mon_cv.pdf"
fichiere_referentiel = "Referentiel_bts.pdf"
 

#// ==========================================
#// 2. FONCTION : LIRE LE FICHIER CSV
#// ==========================================


def lire_excel(chemin_fichier):
    liste_recruteurs = []

    print(f" Ouverture du fichier : {chemin_fichier}")
    
    try:
            
            df = pd.read_excel(chemin_fichier)
            for index, row in df.iterrows():
                email_choisi = row.get('MAIL_RESPONSABLE')

                if not email_choisi:
                    email_choisi = row.get('MAL_ENTREPRISE')
                if not email_choisi:
                    continue

                recruteur = row.to_dict()

                liste_recruteurs.append(recruteur)
            return liste_recruteurs
        
    except FileNotFoundError:
        print("Erreur pas de fichier xlsx.")
        return[]

#// ==========================================
#// 2. FONCTION : LIRE LE FICHIER CSV
#// ==========================================

if __name__ == "__main__":
    recruteurs = lire_excel("/home/kram/Documents/dev/stage_auto/3.5_ListeEntrepriseStage_2024.xlsx")
    print(f"nombre de recruteurs : {len(recruteurs)}")
    print(recruteurs)

