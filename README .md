# Mon Projet Django

Application web développée avec Django dans le cadre d'un projet académique. Le dépôt contient la structure de base d'un projet Django avec une application principale, des templates, des fichiers statiques et la configuration du panneau d'administration.

## Structure du projet

Le projet est organisé autour d'une configuration Django principale et d'une application métier.

```text
mon_projet/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── mon_projet/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── main/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
└── .gitignore
```

## Prérequis

- Python 3
- pip
- Un terminal Linux, WSL ou VS Code

## Installation

1. Cloner le dépôt GitHub :

```bash
git clone https://github.com/lahbaeilaymen3-prog/-mon_projet_django.git
cd -mon_projet_django
```

2. Créer un environnement virtuel :

```bash
python3 -m venv env
```

3. Activer l'environnement virtuel :

```bash
source env/bin/activate
```

4. Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Lancer le projet

Exécuter les migrations si nécessaire :

```bash
python3 manage.py migrate
```

Démarrer le serveur de développement :

```bash
python3 manage.py runserver
```

Puis ouvrir dans le navigateur :

```text
http://127.0.0.1:8000/
```

## Accès administration

Pour accéder à l’interface d’administration Django :

```text
http://127.0.0.1:8000/admin/
```

Si aucun compte administrateur n’existe encore, créer un superutilisateur avec :

```bash
python3 manage.py createsuperuser
```

Si le mot de passe admin a été oublié :

```bash
python3 manage.py changepassword NOM_UTILISATEUR
```

## Fonctionnalités

- Application Django structurée avec une application `main`
- Gestion des routes avec `urls.py`
- Vues Django dans `views.py`
- Modèles de données dans `models.py`
- Interface d’administration Django
- Utilisation de templates HTML et de fichiers statiques

## GitHub

Le code source du projet est disponible ici :

```text
https://github.com/lahbaeilaymen3-prog/-mon_projet_django
```

## Auteur

Projet réalisé par Skander Lahbaiel.
