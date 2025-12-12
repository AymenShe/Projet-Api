# Projet E-Commerce API & Web Services

Ce projet est une application complète de commerce électronique, construite avec une architecture moderne séparant le backend et le frontend.

## Auteur
Aymen ALLOUNE
Amir BEN HASSEN

## 🚀 Technologies Utilisées

- **Backend**: FastAPI (Python), SQLAlchemy, Pydantic
- **Frontend**: React, Vite, TailwindCSS
- **Base de Données**: PostgreSQL
- **IA**: Recommandations de produits basées sur le contenu (TF-IDF)
- **Conteneurisation**: Docker & Docker Compose

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir installé :
- Python 3.11 ou supérieur
- Node.js et npm
- Docker et Docker Compose
- Make (optionnel, mais recommandé pour utiliser les commandes simplifiées)

## 🛠️ Installation

Le projet utilise un `Makefile` pour simplifier les tâches courantes.

1. **Installer toutes les dépendances (Backend & Frontend)** :
   ```bash
   make install
   ```
   Cette commande va installer les dépendances Python.

## ▶️ Démarrage

Pour lancer le backend complet (Base de données et Backend) :
Pour lancer le frontend complet (Frontend) :
```bash
make start
make start-frontend
```

- **Backend API** : Accessible sur [http://localhost:8000](http://localhost:8000)
- **Documentation API (Swagger)** : [http://localhost:8000/docs](http://localhost:8000/docs)
- **Frontend** : Accessible sur [http://localhost:5173](http://localhost:5173)

## 🧪 Tests et Qualité du Code

- **Lancer les tests unitaires et d'intégration** :
  ```bash
  make test
  ```

## 📂 Structure du Projet

- `app/` : Code source du backend FastAPI.
  - `api/` : Endpoints de l'API.
  - `core/` : Configuration, sécurité et authentification.
  - `db/` : Modèles de base de données et CRUD.
  - `services/` : Logique métier (IA, Paiement, etc.).
- `frontend/` : Code source du frontend React.
- `tests/` : Tests automatisés (Pytest).
- `docker-compose.yml` : Configuration des services Docker (DB, Adminer).
- `Makefile` : Raccourcis pour les commandes de développement.

## ✨ Fonctionnalités Principales

1. **Authentification** : Inscription, Connexion (JWT), Gestion de profil.
2. **Catalogue** : Liste de produits, recherche, filtrage par catégorie, géolocalisation des magasins.
3. **Panier & Commandes** : Gestion du panier, passage de commande.
4. **Intelligence Artificielle** : Système de recommandation de produits similaires.
5. **Sécurité** : Hachage des mots de passe, protection des routes API.
6. **Paiement** : Intégration de PayPal et Stripe (simulation).
7. **Livraison** : Suivi de commande en temps réel via l'API et l'interface utilisateur.
8. **GraphQL** : API GraphQL native pour des requêtes flexibles (backend side (localhost:8000)`/graphql`).
9. **UX Améliorée** : Feedback utilisateur (Toast), persistance du panier, et restrictions d'accès au paiement.
