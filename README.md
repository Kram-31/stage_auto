# Stage Auto

Un script Python pour automatiser l'envoi de candidatures de stage personnalisées par email.

## Description

Ce projet a pour but de faciliter la recherche de stage en automatisant l'envoi d'emails à une liste de recruteurs.
Le script lit un fichier Excel contenant les informations des entreprises, génère un email personnalisé (avec salutation et nom de l'entreprise), attache automatiquement votre CV (PDF) et envoie le tout via un serveur SMTP (ex: Gmail).
Il met ensuite à jour le fichier Excel avec le statut de l'envoi et la date, pour éviter les doublons et assurer un suivi efficace.

## Getting Started

### Dependencies

* **OS:** Windows, macOS ou Linux.
* **Python:** Version 3.x recommandée.
* **Bibliothèques Python:**
    * `pandas` (gestion des données Excel)
    * `openpyxl` (lecture/écriture Excel)
    * `python-dotenv` (gestion des variables d'environnement)

### Installing

1.  **Cloner ou télécharger le projet**
    Téléchargez les fichiers dans un dossier local.

2.  **Organiser les fichiers**
    Assurez-vous que la structure des dossiers est respectée :
    * `assets/` : Placez votre CV ici (ex: `Mon_cv.pdf`).
    * `data/` : Placez votre fichier de suivi Excel ici (ex: `Liste_stage_test.xlsx`).
    * `.env` : À créer à la racine (voir ci-dessous).

3.  **Installer les dépendances**
    Ouvrez un terminal dans le dossier du projet et lancez :
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration (.env)**
    Créez un fichier nommé `.env` à la racine et ajoutez vos identifiants (ne partagez jamais ce fichier) :
    ```ini
    SMTP_EMAIL=votre.email@gmail.com
    SMTP_PASSWORD=votre_mot_de_passe_application
    CHEMIN_EXCEL=data/Liste_stage_test.xlsx
    CHEMIN_CV=assets/Mon_cv.pdf
    ```

### Executing program

1.  Assurez-vous que votre fichier Excel contient bien les colonnes : `ENTREPRISE`, `MAIL_RESPONSABLE`, `CIVILITE_RESP`, `NOM_RESP`, `STATUT`.
2.  Fermez le fichier Excel s'il est ouvert sur votre ordinateur.
3.  Lancez le script :

```bash
python main.py
