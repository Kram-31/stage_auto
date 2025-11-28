# 🚀 Stage Auto - Automatisation de Candidatures

Ce projet est un outil d'automatisation développé en Python pour faciliter la recherche de stage. Il permet d'envoyer des emails de candidature personnalisés en masse à partir d'une liste de recruteurs stockée dans un fichier Excel, tout en attachant automatiquement un CV au format PDF.

## 📋 Fonctionnalités

* **Personnalisation :** Adapte la salutation (M./Mme) et le nom de l'entreprise dans le corps du mail.
* **Suivi automatique :** Met à jour le fichier Excel après chaque envoi avec le statut "Mail Envoyé" et la date du jour.
* **Pièces jointes :** Attache automatiquement le CV (PDF) situé dans le dossier `assets`.
* **Anti-Spam :** Intègre un délai configurable entre chaque envoi pour éviter d'être bloqué par le serveur SMTP.
* **Sécurité :** Utilise des variables d'environnement (.env) pour ne jamais exposer les mots de passe dans le code.

## 📂 Structure du Projet

Voici comment organiser vos fichiers pour que le script fonctionne :

```text
stage_auto/
├── assets/              # Placez ici votre CV (ex: Mon_cv.pdf)
├── data/                # Placez ici votre fichier Excel (ex: Liste_stage.xlsx)
├── docs/                # Documentation et pseudo-code
├── .env                 # Fichier de configuration secret (non versionné)
├── config.py            # Script de configuration des chemins et variables
├── main.py              # Script principal à lancer
├── requirements.txt     # Liste des modules Python nécessaires
└── README.md            # Ce fichier

⚙️ Installation
1. Préparer l'environnement
Ouvrez un terminal et lancez les commandes suivantes :

''''Bash

# Créer un environnement virtuel pour isoler le projet
python -m venv venv

# Activer l'environnement (Sur Windows)
venv\Scripts\activate
# OU (Sur Mac/Linux)
# source venv/bin/activate

# Installer les dépendances listées dans requirements.txt
pip install -r requirements.txt

2. Configuration des secrets (.env)Créez un fichier nommé .env à la racine du projet et ajoutez-y vos informations.Attention : Ce fichier ne doit jamais être partagé sur GitHub.Ini, TOML# Exemple de contenu du fichier .env
SMTP_EMAIL=votre.email@gmail.com
# Pour Gmail, utilisez un "Mot de passe d'application" (pas votre mdp habituel)
SMTP_PASSWORD=votre_mot_de_passe_application
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587

# Configuration des fichiers (Optionnel, valeurs par défaut dans config.py)
CHEMIN_EXCEL=data/Liste_stage_test.xlsx
CHEMIN_CV=assets/Mon_cv.pdf
DELAI_ENTRE_ENVOIS=15
📊 Format du fichier ExcelPour que le script fonctionne, votre fichier Excel dans le dossier data/ doit contenir les colonnes exactes suivantes :Nom de la colonneDescriptionObligatoire ?ENTREPRISENom de l'entreprise (utilisé dans le mail)OUIMAIL_RESPONSABLEAdresse email du destinataireOUICIVILITE_RESPM. ou MmeNonNOM_RESPNom de famille du recruteurNonSTATUTLaisser vide. Sera rempli par "Mail Envoyé".NonDATE_ENVOILaisser vide. Sera rempli par la date.NonNote : Si MAIL_RESPONSABLE est vide, le script cherchera dans une colonne EMAIL_ENTREPRISE.🚀 UtilisationUne fois tout configuré, lancez simplement le script :Bashpython main.py
Le script va :Lire le fichier Excel.Ignorer les lignes où le STATUT est déjà rempli.Envoyer les mails un par un avec une pause de 10-15 secondes.Sauvegarder l'avancement dans le fichier Excel en temps réel.⚠️ Notes de sécurité (Gmail)Si vous utilisez Gmail, vous devez activer la "Validation en deux étapes" sur votre compte Google, puis générer un Mot de passe d'application pour l'utiliser dans le fichier .env. N'utilisez jamais votre vrai mot de passe Gmail.👤 AuteurKamal Kaced - Étudiant en BTS CIEL IR (Cybersécurité, Informatique et Réseaux).
