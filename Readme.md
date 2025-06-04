# Mini-projet : Prédiction du revenu annuel d’un Marocain

## Description du projet
Ce mini-projet a pour objectif de construire un pipeline complet de Machine Learning en Python pour prédire le revenu annuel des Marocains à partir de données simulées réalistes. Le projet couvre toutes les étapes du processus de Machine Learning, de la génération des données à leur déploiement sous forme d'une application web.

## Compétences visées
- Génération de données synthétiques.
- Nettoyage et transformation des données.
# Mini-projet IA : Prédiction du Revenu Annuel des Marocains

## Objectif
Construire un pipeline complet de Machine Learning pour prédire le revenu annuel des Marocains à partir de données synthétiques réalistes, en suivant les étapes :
- Génération de données  
- Nettoyage et exploration  
- Modélisation (5 algorithmes de régression)  
- Déploiement via FastAPI et Streamlit  


## Installation
1. Cloner le dépôt :
   ```bash
   git clone https://github.com/ELMOURABETNADA/Prediction-du-revenu-annuel-d-un-marocain

Installer les dépendances :

bash
pip install -r requirements.txt
 Exécution
1. Générer le dataset (optionnel)
bash
python generate_dataset.py
2. Lancer l'analyse (Jupyter Notebook)
Ouvrir mini_projet_AI_nom.ipynb et exécuter les cellules.

3. Déployer l'API
bash
uvicorn api:app --reload
4. Lancer l'application Streamlit
bash
streamlit run app.py
 Modèles implémentés

Régression Linéaire

Arbres de Décision

Random Forest

Gradient Boosting

MLP (Réseaux de Neurones)

Spécifications techniques
Langage : Python 3

Librairies : Pandas, NumPy, Scikit-learn, Matplotlib, Streamlit, FastAPI

Hyperparamètres : Optimisés via GridSearchCV


Auteurs
Sadki Mohamed

Nada El Mourabet

Kaoutar Iabakriman

*Projet réalisé dans le cadre du module d'Intelligence Artificielle - 2ème année Cycle d'Ingénieurs GI2 (2024-2025)*
