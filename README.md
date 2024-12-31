# Projet : Bank Churn Prediction 

Ce projet a été réalisé par **Hella Bouhadda** et **Chirine Dexposito** dans le cadre du cours de Data Mining du Master 2 MoSEF. Il comprend plusieurs étapes allant de l'analyse exploratoire des données à la modélisation et l’évaluation des modèles prédictifs.

---

## 🚀 Organisation du Projet

### 📊 1. **Analyse des Données**
- **Script** : `1.analyse_donnees.py`
- **Description** :
  - Exploration des données avec des visualisations.
  - Analyse de la distribution des classes et corrélations entre les variables.
  - Identification des relations entre les variables numériques et la variable cible.

---

### 🛠️ 2. **Prétraitement des Données**
- **Script** : `2.pretraitement_donnees.py`
- **Description** :
  - Gestion des valeurs manquantes.
  - Encodage des variables catégoriques.
  - Standardisation des variables numériques.
  - Sauvegarde des données prétraitées.

---

### 🌟 3. **Feature Engineering**
- **Script** : `3.feature_engineering.py`
- **Description** :
  - Création de nouvelles caractéristiques à partir des données existantes (e.g., ratios et produits).
  - Suppression des colonnes inutiles.
  - Sauvegarde des données enrichies.

---

### 🤖 4. **Modélisation avec AutoGluon**
- **Script** : `4.modelisation_autogluon.py`
- **Description** :
  - Utilisation d’AutoGluon pour automatiser la construction d’un modèle prédictif.
  - Entraînement et évaluation sur le jeu de données.
  - Sauvegarde des prédictions pour le jeu de test.

---

### 🔍 5. **Analyse des Erreurs**
- **Script** : `5.analyse_erreurs.py`
- **Description** :
  - Évaluation des performances avec la matrice de confusion et le score ROC AUC.
  - Analyse des distributions des prédictions correctes et incorrectes.

---

### 🐱‍💻 6. **Modélisation avec CatBoost**
- **Script** : `6.modelisation_catboost.py`
- **Description** :
  - Entraînement d’un modèle en utilisant CatBoost avec validation croisée K-Fold.
  - Calcul et sauvegarde des prédictions pour le jeu de test.

---

### 🧩 7. **Modèle Ensemble**
- **Script** : `7.modele_ensemble.py`
- **Description** :
  - Combinaison des prédictions d’AutoGluon et CatBoost.
  - Création d’un modèle d’ensemble basé sur une moyenne simple des prédictions.
  - Sauvegarde des résultats finaux.

---

## 📝 Instructions pour Exécution

### 1️⃣ **Installation des Prérequis**
- Python 3.8+
- Librairies : `pandas`, `numpy`, `seaborn`, `matplotlib`, `autogluon`, `catboost`, `scikit-learn`

```bash
pip install pandas numpy seaborn matplotlib autogluon catboost scikit-learn
