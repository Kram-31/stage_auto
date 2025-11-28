# stage_auto

Ce script automatise l'envoi de candidatures par email à partir d'un fichier Excel contenant la liste des recruteurs.

## Fonctionnalités

- Lecture d'un fichier Excel avec les informations des recruteurs.
- Génération automatique d'emails personnalisés.
- Ajout du CV en pièce jointe.
- Mise à jour du fichier Excel après chaque envoi (statut et date).
- Simulation d'envoi (DRY RUN) pour les tests.

## Prérequis

- Python 3.x
- Modules : `pandas`, `openpyxl`, `smtplib`

## Installation

1. Cloner le dépôt ou copier les fichiers dans un dossier.
2. Installer les dépendances :
   ```
   pip install pandas openpyxl
   ```
3. Configurer le fichier `config.py` avec vos paramètres SMTP et chemins de fichiers.

## Utilisation

1. Préparer le fichier Excel avec les colonnes nécessaires (`ENTREPRISE`, `MAIL_RESPONSABLE`, etc.).
2. Placer votre CV au chemin indiqué dans `config.py`.
3. Lancer le script :
   ```
   python main.py
   ```

## Personnalisation

- Modifiez le corps du mail dans la fonction `fabriquer_mail` selon vos besoins.
- Adaptez le délai entre les envois dans `config.py`.

## Sécurité

Ne partagez pas vos identifiants SMTP. Utilisez des variables d'environnement pour plus de sécurité.

## Auteur

Kamal Kaced
