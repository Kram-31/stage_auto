import os 
import smtplib
import time
import pandas as pd
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Charger configuration depuis config.py
from config import (
    SMTP_EMAIL,
    SMTP_PASSWORD,
    SMTP_SERVER,
    SMTP_PORT,
    CHEMIN_EXCEL,
    CHEMIN_CV,
    DELAI_ENTRE_ENVOIS,
    FORMAT_DATE,
)
 

# ==========================================
# FONCTION : LIRE LE FICHIER CSV
# ==========================================

def lire_excel(chemin_fichier):
    print(f"Ouverture du fichier : {chemin_fichier}")
    
    try:
        df = pd.read_excel(chemin_fichier)
        return df
        
    except FileNotFoundError:
        print("Erreur : pas de fichier xlsx trouvé.")
        return None
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return None

def mettre_a_jour_mail_envoye(dataframe, index_ligne, chemin_fichier):
    """Met à jour STATUT et DATE_ENVOI"""
    date_actuelle = datetime.now().strftime(FORMAT_DATE)
  
    
    # Convertir les colonnes en type objet avant assignation
    if 'STATUT' in dataframe.columns:
        dataframe['STATUT'] = dataframe['STATUT'].astype('object')
        dataframe.loc[index_ligne, 'STATUT'] = 'Mail Envoyé'
        print(f"  → STATUT mis à jour: 'Mail Envoyé'")
    
    # Mise à jour de la date d'envoi
    if 'DATE_ENVOI' in dataframe.columns:
        dataframe['DATE_ENVOI'] = dataframe['DATE_ENVOI'].astype('object')
        dataframe.loc[index_ligne, 'DATE_ENVOI'] = date_actuelle
        print(f"  → DATE_ENVOI: {date_actuelle}")
    
    # Sauvegarde
    try:
        dataframe.to_excel(chemin_fichier, index=False, engine='openpyxl')
        print(f" Mail envoyé enregistré dans Excel")
    except Exception as e:
        print(f"ERREUR LORS DE LA MISE À JOUR du fichier Excel: {e}")

# ==========================================
# FONCTION : FABRIQUER LE MAIL (TEXTE + PDF)
# ==========================================

def attacher_fichier(message, chemin_fichier):
    try:
        import mimetypes
        ctype, encoding = mimetypes.guess_type(chemin_fichier)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'

        maintype, subtype = ctype.split('/', 1)

        with open(chemin_fichier, 'rb') as f:
            fichier_lu = f.read()

        piece_jointe = MIMEBase(maintype, subtype)
        piece_jointe.set_payload(fichier_lu)
        encoders.encode_base64(piece_jointe)

        nom_fichier = os.path.basename(chemin_fichier)
        piece_jointe.add_header('Content-Disposition', 'attachment', filename=nom_fichier)
        message.attach(piece_jointe)
    except FileNotFoundError:
        print("pas de cv")
    except Exception as e:
        print(f"erreur: {e}")

def fabriquer_mail(recruteur):
    nom_responsable = recruteur.get('NOM_RESP', '')
    civilite = recruteur.get('CIVILITE_RESP', '')
    if nom_responsable and pd.notna(nom_responsable) and civilite and pd.notna(civilite):
        salutation = f"Bonjour {civilite} {nom_responsable}"
    else:
        salutation = "Madame, Monsieur"
    
    message = MIMEMultipart('mixed')
    email_destinataire = recruteur.get('MAIL_RESPONSABLE') or recruteur.get('EMAIL_ENTREPRISE')
    message['From'] = SMTP_EMAIL
    message['To'] = email_destinataire
    message['Subject'] = f"Candidature Stage {recruteur.get('ENTREPRISE', 'Entreprise')}"

    corps_html = f"""\
        <html>
            <body>
                <p>{salutation},</p>
                <p>Je vous écris pour postuler chez <b>{recruteur.get('ENTREPRISE', 'cette entreprise')}</b>...</p>
                <p>Mon CV est en pièce jointe.</p>
                <p>Cordialement,</p>
                <p>Kamal Kaced</p>
            </body>
        </html>
        """
    partie_html = MIMEText(corps_html, 'html')
    message_alternatif = MIMEMultipart('alternative')
    message_alternatif.attach(partie_html)
    message.attach(message_alternatif)
    
    attacher_fichier(message, CHEMIN_CV)

    return message

def main():
    chemin_excel = CHEMIN_EXCEL
    print("Lecture des données")
    df = lire_excel(chemin_excel)
    
    if df is None or df.empty:
        print("Aucune donnée de recruteurs. Arrêt.")
        return

    print(f"{len(df)} recruteurs trouvés")

    server = None

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        print(" Connecté au serveur mail\n")

    except smtplib.SMTPAuthenticationError:
        print("Erreur de connexion : problème d'authentification")
        return

    except smtplib.SMTPException as e:
        print(f"Erreur SMTP : {e}")
        return

    # ==========================================
    # ENVOYER LES MAILS
    # ==========================================
    print("="*70)
    print("PHASE : ENVOI DES MAILS")
    print("="*70)
    
    count_envoi = 0
    
    for index_ligne, row in df.iterrows():
        recruteur = row.to_dict()
        email_destinataire = recruteur.get('MAIL_RESPONSABLE') or recruteur.get('EMAIL_ENTREPRISE')
        entreprise = recruteur.get('ENTREPRISE', 'Entreprise')
        statut = str(recruteur.get('STATUT', '')).strip() if pd.notna(recruteur.get('STATUT')) else ''

        # Vérifier si le mail a déjà été envoyé
        if statut and statut != '':
            print(f"⏭ Déjà traité : {entreprise} (Statut: {statut})")
            continue

        # Vérifier qu'on a une adresse mail
        if not email_destinataire or pd.isna(email_destinataire):
            print(f"Pas d'email pour : {entreprise}")
            continue

        try:
            email_pret = fabriquer_mail(recruteur)
            server.sendmail(SMTP_EMAIL, email_destinataire, email_pret.as_string())
            date_actuelle = datetime.now().strftime(FORMAT_DATE)
            print(f"Mail envoyé à : {entreprise} ({email_destinataire})")  
            print(f"  DATE_ENVOI : {date_actuelle}")
            
            # Mettre à jour le statut et date d'envoi
            mettre_a_jour_mail_envoye(df, index_ligne, chemin_excel)
            count_envoi += 1

        except smtplib.SMTPException as e:
            print(f" Erreur d'envoi pour : {entreprise}. Erreur: {e}")
        
        except Exception as e:
            print(f" Erreur inattendue pour : {entreprise}. Erreur: {e}")
        
        time.sleep(DELAI_ENTRE_ENVOIS)

    print(f"\n{'='*70}")
    print(f" Résumé : {count_envoi} mails envoyés")
    print(f"{'='*70}\n")

    # ==========================================
    # FIN
    # ==========================================
    if server:
        server.quit()
    
    print("="*70)
    print("Exécution terminée avec succès!")
    print("="*70)


if __name__ == "__main__":
    main()