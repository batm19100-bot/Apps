# 📚 Application de Gestion des Documents Archivés - ISSEA

Application Streamlit pour gérer efficacement les documents (mémoire, rapport de stage, projet tutoré et groupe de travail (GT) archivés de l'ISSEA avec stockage en JSON.

## 📊 Base de données ISSEA

L'application contient **550 documents** archivés de l'ISSEA couvrant la période de **1988 à 2024**.

### Statistiques de la base de données
- **Période couverte** : 1988 - 2024 (36 ans)
- **Types de documents** : Mémoire, Rapport, Projet tutoré, Groupe de travail
- **Formations** : Initiale, Continue
- **Filières** : IAS, ISE, AS, TSS, MAP, MSA, MDSMS, L2BD, LGTSD

## 🎯 Fonctionnalités

### 1. Tableau de bord
- Vue d'ensemble de tous les documents archivés
- Métriques en temps réel (nombre de documents, années, auteurs)
- Filtres multiples (année, type, formation)
- Modification et suppression de documents

### 2. Ajouter un document
- Formulaire intuitif pour ajouter de nouveaux documents
- Validation des champs obligatoires
- Enregistrement automatique dans le fichier JSON

### 3. Recherche avancée
- Recherche en temps réel dans tous les champs
- Affichage détaillé des résultats

### 4. Statistiques
- Graphiques interactifs par année, type, formation et filière
- Top 10 des auteurs les plus prolifiques
- Distribution par décennie
- Métriques récapitulatives

## 📋 Structure des données

Chaque document contient les informations suivantes :
- **Année** : Année de référence du document
- **Titre** : Titre complet du document
- **Type** : Type de document (Rapport, Mémoire, Projet tutoré, Groupe de travail)
- **Formation** : Type de formation (Initiale, Continue)
- **Filière** : Filière d'études (IAS, ISE, AS, etc.)
- **Auteur** : Nom de l'auteur du document

## 🚀 Installation

### Prérequis
- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Installer les dépendances** :
```bash
pip install -r requirements.txt
```

2. **Lancer l'application** :
```bash
streamlit run app_gestion_archives.py
```

3. **Accéder à l'application** :
L'application s'ouvrira automatiquement dans votre navigateur à l'adresse :
```
http://localhost:8501
```

## 📁 Fichiers

- `app_gestion_archives.py` : Code principal de l'application
- `archives_documents.json` : Base de données JSON avec les 304 documents ISSEA
- `convertir_issea.py` : Script de conversion du format ISSEA original
- `requirements.txt` : Liste des dépendances Python

## 💾 Stockage des données

Les données sont stockées dans le fichier `archives_documents.json` au format suivant :

```json
[
  {
    "id": 1,
    "annee": "1988",
    "titre": "Population et logements à Yaoundé : situation actuelle et perspectives",
    "type": "Mémoire",
    "formation": "Initiale",
    "filiere": "IAS",
    "auteur": "Bernard Docgne",
    "date_ajout": "2024-11-15 10:30:00"
  }
]
```

## 🔧 Utilisation

### Ajouter un document
1. Sélectionnez "➕ Ajouter un document" dans le menu
2. Remplissez tous les champs obligatoires (Année, Titre, Type, Formation, Filière, Auteur)
3. Cliquez sur "💾 Enregistrer le document"

### Rechercher un document
1. Sélectionnez "🔍 Rechercher" dans le menu
2. Tapez un mot-clé dans la barre de recherche (auteur, titre, filière, etc.)
3. Les résultats s'affichent automatiquement avec tous les détails

### Modifier un document
1. Dans le tableau de bord, trouvez le document à modifier
2. Cliquez sur le bouton "✏️ Modifier"
3. Modifiez les champs souhaités
4. Cliquez sur "💾 Enregistrer"

### Supprimer un document
1. Dans le tableau de bord, trouvez le document à supprimer
2. Cliquez sur le bouton "🗑️ Supprimer"
3. Le document est immédiatement supprimé

## 📊 Visualisation des statistiques

Le menu "📊 Statistiques" propose :
- Graphiques par année (1988-2024)
- Graphiques par type de document
- Graphiques par formation
- Graphiques par filière
- Top 10 des auteurs les plus prolifiques
- Distribution par décennie
- Métriques récapitulatives

## 🔄 Conversion des données ISSEA

Si vous avez un nouveau fichier ISSEA.json à importer :

1. Placez le fichier `ISSEA.json` dans le dossier
2. Exécutez le script de conversion :
```bash
python convertir_issea.py
```
3. Le fichier `archives_documents.json` sera mis à jour automatiquement

## 🛡️ Sauvegarde

Les données sont automatiquement sauvegardées dans le fichier JSON après chaque opération (ajout, modification, suppression).

**Recommandation** : Sauvegardez régulièrement le fichier `archives_documents.json` pour éviter toute perte de données.

## 💡 Conseils d'utilisation

- Utilisez la recherche pour trouver rapidement un document par auteur, titre, ou mot-clé
- Les filtres du tableau de bord permettent de naviguer facilement par année, type ou formation
- Les statistiques offrent une vue d'ensemble de l'évolution des publications
- Le champ "Titre" accepte les titres longs (zone de texte extensible)

## 🐛 Résolution de problèmes

**L'application ne démarre pas** :
- Vérifiez que toutes les dépendances sont installées (`pip install streamlit pandas`)
- Assurez-vous d'utiliser Python 3.7+

**Les données ne se sauvegardent pas** :
- Vérifiez les permissions d'écriture dans le dossier
- Assurez-vous que le fichier JSON n'est pas ouvert dans un autre programme

**Erreur lors de la recherche** :
- Vérifiez que le fichier `archives_documents.json` existe et est valide

## 📈 Évolution de la base de données

La base de données actuelle contient :
- **304 documents** couvrant **36 années** (1988-2024)
- Principalement des **Mémoires** de formation **Initiale**
- Répartition sur **9 filières** différentes

## 📞 Support

Pour toute question ou problème, vérifiez d'abord que vous avez suivi toutes les étapes d'installation.

---

**Développé avec ❤️ pour l'ISSEA | Données stockées en JSON**
