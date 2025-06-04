# 📊 Mini-projet IA : Prédiction du Revenu Annuel des Marocains

## 📋 Description
Ce projet implémente un système complet de prédiction du revenu annuel des Marocains en utilisant des techniques de Machine Learning. Il utilise des données synthétiques réalistes pour construire un modèle prédictif accessible via une interface web conviviale.

## 🎯 Objectifs
- Générer un jeu de données synthétiques représentatif
- Analyser et préparer les données
- Développer des modèles de régression performants
- Déployer une solution accessible via une interface web

## 🔧 Technologies Utilisées
- Python 3.x
- Scikit-learn pour le Machine Learning
- FastAPI pour l'API REST
- Streamlit pour l'interface utilisateur
- Pandas & NumPy pour la manipulation des données
- Jupyter Notebook pour l'analyse exploratoire

## 📁 Structure du Projet
```
.
├── dataset_revenu_marocains.csv    # Données (40 000 entrées)
├── mini_projet_AI_Noms.ipynb       # Notebook d'analyse
├── api.py                          # API FastAPI
├── app.py                          # Interface Streamlit
└── requirements.txt                # Dépendances
```

## ⚙️ Installation

1. Cloner le dépôt :
```powershell
git clone https://github.com/ELMOURABETNADA/Prediction-du-revenu-annuel-d-un-marocain
```

2. Installer les dépendances :
```powershell
pip install -r requirements.txt
```

## 🚀 Démarrage

1. Lancer l'API FastAPI :
```powershell
uvicorn api:app --reload
```

2. Démarrer l'interface Streamlit :
```powershell
streamlit run app.py
```

3. Pour l'analyse des données, ouvrir le notebook Jupyter :
```powershell
jupyter notebook mini_projet_AI_Noms.ipynb
```

## 🤖 Modèles Implémentés

Nous avons implémenté et comparé 5 algorithmes de régression :
- Régression Linéaire
- Arbres de Décision
- Random Forest
- Gradient Boosting
- Réseaux de Neurones (MLP)

Les hyperparamètres ont été optimisés via GridSearchCV pour obtenir les meilleures performances.

## 👥 Auteurs

- Sadki Mohamed
- Nada El Mourabet
- Kaoutar Iabakriman

*Projet réalisé dans le cadre du module d'Intelligence Artificielle - 2ème année Cycle d'Ingénieurs GI2 (2024-2025)*
