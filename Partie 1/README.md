# Hackathon SmartDoc.ai

**Membres du groupe :**
- **HIROUCHE Walid** : [walid.hirouche@centrale-casablanca.ma](mailto:walid.hirouche@centrale-casablanca.ma)
- **BENKIRANE Reda** : [reda.benkirane@centrale-casablanca.ma](mailto:reda.benkirane@centrale-casablanca.ma)

---

## **Résumé**

Ce projet a été réalisé dans le cadre du **Hackathon SmartDoc.ai**, et son objectif principal est de résoudre les problématiques liées à l’analyse des rapports SFCR grâce à des outils de Machine Learning et une architecture RAG (**Retrieval-Augmented Generation**).

---

## **Problématique**

Lorsqu'un Data Scientist travaille sur des rapports au format PDF, il est souvent confronté à des défis liés à la qualité des résultats des OCR :
1. Les **informations inutiles** (bas/hauts de page, contenus répétitifs) perturbent l’analyse.
2. Les données **non structurées** (ex. tableaux, graphes) nécessitent un travail supplémentaire pour en extraire des informations exploitables.

### Pourquoi ne pas trier par longueur de texte (`len`) ?
Une méthode basique comme un tri par la longueur des textes n'est pas efficace. Par exemple :
- Certains **paragraphes courts** peuvent être plus courts que certains **titres**, créant une zone grise difficile à distinguer.
- Les **bas de page répétitifs**, malgré leur contenu inutile, peuvent avoir une longueur suffisante pour être classés comme des titres.

C’est pourquoi nous avons développé une approche hybride combinant des manipulations manuelles et des modèles de Machine Learning.

---

## **Note importante sur les scripts**

Tous les scripts sont **flexibles** et acceptent un chemin en argument lors de leur exécution. Si aucun chemin n'est spécifié, un **chemin par défaut** sera utilisé. Cela vous évite de modifier constamment les scripts pour changer les dossiers de travail.

**Exemple** :
```bash
python csv_to_txt.py data/csv_model
```
Si le chemin `data/csv_model` n'est pas spécifié, le script utilisera par défaut `data/csv_model`.

---

## **Architecture du projet**

Le projet est structuré comme suit :

```
.
├── classification
│   ├── [requirements.txt](classification/requirements.txt)
│   ├── [training_model.ipynb](classification/training_model.ipynb)
│   └── weights
│       ├── pca.pkl
│       ├── scaler.pkl
│       └── xgboost_classifier.json
├── data
│   ├── csv
│   │   ├── allianz-1-to-94.csv
│   │   ...
│   │   └── covea-output-1-to-98.csv
│   ├── csv_manual
│   │   ├── axa-output-1-to-71.csv
│   │   └── training_data.csv
│   ├── csv_model
│   │   ├── predicted_allianz-1-to-94.csv
│   │   ...
│   │   └── predicted_covea-output-1-to-98.csv
│   ├── json
│   │   ├── allianz-1-to-94.json
│   │   ...
│   │   └── covea-output-1-to-98.json
│   └── txt
│       ├── predicted_allianz-1-to-94.txt
│       ...
│       └── predicted_covea-output-1-to-98.txt
├── [csv_to_txt.py](csv_to_txt.py)
├── [helper_improved.py](helper_improved.py)
├── [predict_labels.py](predict_labels.py)
├── [prepare_training_data.py](prepare_training_data.py)
└── README.md
```

---

## **Étapes détaillées**

### 1. **Conversion des JSON en CSV : [helper_improved.py](helper_improved.py)**

- **But** : Convertir les fichiers JSON produits par l’OCR en CSV structurés pour faciliter le traitement ultérieur.
- **Ajouts importants** :
  - Une colonne `id` pour conserver l’ordre des lignes, utile pour le reclassement après modification de l'ordre des lignes sur Excel.
  - Une colonne `label` vide pour permettre une classification manuelle dans Excel.

#### Commande à exécuter :
```bash
python helper_improved.py [data/json]
```

#### Résultat :
- Les fichiers JSON dans `data/json/` sont convertis en fichiers CSV et enregistrés dans `data/csv/`.

---

### 2. **Classification manuelle dans Excel**

#### Étapes recommandées :
1. **Trier sur la colonne `chars`** :
   - Permet de regrouper les lignes avec peu de caractères, souvent inutiles, et de distinguer les paragraphes et titres.
2. **Trier sur la colonne `text`** :
   - Regroupe les lignes avec un format similaire (ex. `B.1`, `B.2`, `/`), pour classifier les titres par blocs.
3. **Finaliser avec la colonne `label`** :
   - Afin d'identifiez les lignes encore non classées si on a encore de la patience.
4. **Rétablir l’ordre initial** :
   - On utilise la colonne `id` pour cela.

**Attention** : Pas besoin de labéliser toutes les lignes. Le fichier suivant ne prendra que les lignes déjà classées dans les 4 fichiers et les fusionera dans un seul fichier d'entraînement `training_data.csv`.

---

### 3. **Préparation des données d’entraînement : [prepare_training_data.py](prepare_training_data.py)**

- **But** : Générer un fichier `training_data.csv` avec uniquement les lignes labélisées.
- **Actions** :
  - Concatène tous les fichiers de `data/csv_manual/`.
  - Supprime les colonnes inutiles à l'entraiînement : `id`, `text`, `num_page`.

#### Commande à exécuter :
```bash
python prepare_training_data.py [data/csv_manual]
```

#### Résultat :
- Un fichier `training_data.csv` est généré dans `data/csv_manual/`.

---

### 4. **Entraînement du modèle : [training_model.ipynb](classification/training_model.ipynb)**

- **But** : Entraîner plusieurs modèles de Machine Learning et choisir le meilleur pour la classification.
- **Modèles testés** :
  - K-Nearest Neighbors (KNN)
  - Support Vector Machine (SVM)
  - Decision Tree
  - Random Forest
  - XGBoost
  - Logistic Regression
  - Naive Bayes
  - Artificial Neural Network (ANN)

- **Étapes** :
  1. **Préparation des données** :
     - Analyse des corrélations.
     - Traitement des valeurs aberrantes.
     - Application de PCA pour réduire la dimensionnalité.
     - Scaling et équilibrage des classes (over/undersampling).
  2. **Évaluation des modèles** :
     - Validation croisée.
     - Meilleur modèle : **XGBoost** avec une précision de **97%**.
  3. **Sauvegarde des poids** :
     - Modèle, PCA, et scaler sauvegardés dans `classification/weights/`.

#### Commandes pour exécuter :
1. Installer les dépendances :
   ```bash
   pip install -r classification/requirements.txt
   ```
2. Lancer le notebook :
   ```bash
   jupyter notebook classification/training_model.ipynb
   ```

---

### 5. **Prédiction automatique : [predict_labels.py](predict_labels.py)**

- **But** : Remplir la colonne `label` des fichiers CSV non labélisés.
- **Actions** :
  - Utilise les poids sauvegardés pour prédire les labels.
  - Génère les fichiers labélisés dans `data/csv_model/`.

#### Commande à exécuter :
```bash
python predict_labels.py [data/csv]
```

#### Résultat :
- Les fichiers prédits sont enregistrés dans `data/csv_model/`.

---

### 6. **Génération des fichiers texte : [csv_to_txt.py](csv_to_txt.py)**

- **But** : Convertir les CSV labélisés en fichiers texte pour le RAG.
- **Contenu des fichiers texte** :
  - **Titres** : Précédés de `#`.
  - **Paragraphes** : Simples.
  - **Séparations de page** : `=======page <num>=======`.

#### Commande à exécuter :
```bash
python csv_to_txt.py [data/csv_model]
```

#### Résultat :
- Les fichiers texte sont générés dans `data/txt/`.

---

## **Liens utiles**

- [Dépôt GitHub de la compétition](https://github.com/AlumniECC/Hackathon_Smartdoc.ai)
- [Questions pour la RAG](https://centralecasablanca-my.sharepoint.com/:x:/g/personal/imad_zaoug_centrale-casablanca_ma/EWvYqsFs2oBKoSWg2X0Q2zcBStATPMiXvYKxVztwwfC3mA)
