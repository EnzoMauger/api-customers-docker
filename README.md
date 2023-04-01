API CUSTOMERS
=

# Introduction

Cette API permet de gérer des customers (créer, lire, mettre à jour, supprimer)
Lors du lancement, un jeu de données sera déjà présent

# Installation & Exécution

## Installation

        git clone https://mi-git.univ-tlse2.fr/m1-iceld/2022-23/api-customers-docker.git
        cd api-customers-docker
        docker-compose build

## Exécution

        docker-compose up -d

# Utilisation

## API

L'api est joignable en local sur votre machine via l'url suivante : **[localhost:5000](localhost:5000)**

Vous trouverez l'ensemble des routes (et leur usage) ici : **[localhost:5000/docs](localhost:5000)**

## Interface base de données

L'interface de base de données est adminer, joignable en local sur votre machine via l'url suivante **[localhost:5001](localhost:5001)**

Ce projet étant un exercice dans le cadre d'un module universitaire, voici les informations nécessaire pour vous connecter

```
Système: MySQL	
Serveur: mariadb
Utilisateur: root
Mot de passe: root
Base de données: mydatabase
```

# Choix techniques

## Base de données

Le choix de **mariadb** a été fait car l'équipe de développement souhaitait utiliser un outils qu'elle connaissait et jugeait fiable et simple (et sans licence)

## Interface web de base de données

Le choix d'**adminer** a été fait car l'équipe n'a que peu d'expérience avec d'autres outils

## Applicatif

Le choix de **python** a été fait par soucis de simplicité et de rapidité de développement

Le choix de la librairie **Fastapi** a été fait car l'outils était connu d'une partie de l'équipe et simple d'apprentissage
