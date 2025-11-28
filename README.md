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
