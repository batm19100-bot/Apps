import streamlit as st
import json
import os
from datetime import datetime
import pandas as pd

# Configuration de la page
st.set_page_config(
    page_title="Gestion des Archives ISSEA",
    page_icon="📚",
    layout="wide"
)

# Chargement et affichage du logo dans la barre latérale
#st.sidebar.image("logo.png", use_column_width=True)
st.sidebar.image("logo.png", use_container_width=True)

# Modifier la couleur de fond de la barre latérale
st.markdown(
    """
    <style>
    /* Modifier la couleur de fond de la barre latérale */
    .sidebar .sidebar-content {
        background-color: #03370C;  /* Remplacez #f0f0f0 par la couleur souhaitée */
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Fichier JSON pour stocker les données
JSON_FILE = "archives_documents.json"

# Fonction pour charger les données depuis le fichier JSON
def charger_donnees():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Fonction pour sauvegarder les données dans le fichier JSON
def sauvegarder_donnees(donnees):
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(donnees, f, ensure_ascii=False, indent=2)

# Fonction pour ajouter un document
def ajouter_document(annee, titre, type_doc, formation, filiere, auteur):
    donnees = charger_donnees()
    nouveau_doc = {
        "id": len(donnees) + 1,
        "annee": annee,
        "titre": titre,
        "type": type_doc,
        "formation": formation,
        "filiere": filiere,
        "auteur": auteur,
        "date_ajout": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    donnees.append(nouveau_doc)
    sauvegarder_donnees(donnees)
    return True

# Fonction pour supprimer un document
def supprimer_document(doc_id):
    donnees = charger_donnees()
    donnees = [doc for doc in donnees if doc['id'] != doc_id]
    sauvegarder_donnees(donnees)

# Fonction pour modifier un document
def modifier_document(doc_id, annee, titre, type_doc, formation, filiere, auteur):
    donnees = charger_donnees()
    for doc in donnees:
        if doc['id'] == doc_id:
            doc['annee'] = annee
            doc['titre'] = titre
            doc['type'] = type_doc
            doc['formation'] = formation
            doc['filiere'] = filiere
            doc['auteur'] = auteur
            doc['date_modification'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break
    sauvegarder_donnees(donnees)

# Titre principal
st.title("📚 Système de Gestion des Mémoires professionnels et Rapports de stage Archivés - ISSEA")
st.markdown("---")

# Barre latérale pour la navigation
menu = st.sidebar.selectbox(
    "Menu",
    ["🏠 Tableau de bord", "➕ Ajouter un document", "🔍 Rechercher", "📊 Statistiques"]
)

# TABLEAU DE BORD
if menu == "🏠 Tableau de bord":
    st.header("📋 Tous les documents archivés")
    
    donnees = charger_donnees()
    
    if donnees:
        # Affichage du nombre total de documents
        col1, col2, col3 = st.columns(3)
        col1.metric("📁 Total de documents", len(donnees))
        col2.metric("📅 Années couvertes", len(set([str(d['annee']) for d in donnees])))
        col3.metric("👥 Auteurs différents", len(set([d['auteur'] for d in donnees])))
        
        st.markdown("---")
        
        # Conversion en DataFrame pour l'affichage
        df = pd.DataFrame(donnees)
        
        # Options de filtrage
        st.subheader("🔎 Filtres")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            annees = ["Toutes"] + sorted(list(set([str(d['annee']) for d in donnees])), reverse=True)
            filtre_annee = st.selectbox("Année", annees)
        
        with col2:
            types = ["Tous"] + sorted(list(set([d['type'] for d in donnees])))
            filtre_type = st.selectbox("Type", types)
        
        with col3:
            formations = ["Toutes"] + sorted(list(set([d['formation'] for d in donnees])))
            filtre_formation = st.selectbox("Formation", formations)
        
        # Application des filtres
        donnees_filtrees = donnees.copy()
        if filtre_annee != "Toutes":
            donnees_filtrees = [d for d in donnees_filtrees if str(d['annee']) == filtre_annee]
        if filtre_type != "Tous":
            donnees_filtrees = [d for d in donnees_filtrees if d['type'] == filtre_type]
        if filtre_formation != "Toutes":
            donnees_filtrees = [d for d in donnees_filtrees if d['formation'] == filtre_formation]
        
        st.markdown("---")
        st.subheader(f"📑 Documents trouvés: {len(donnees_filtrees)}")
        
        # Affichage des documents avec options de modification et suppression
        for doc in donnees_filtrees:
            with st.expander(f"📄 {doc['type']} - {doc['auteur']} ({doc['annee']})"):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.write(f"**ID:** {doc['id']}")
                    st.write(f"**Année:** {doc['annee']}")
                    st.write(f"**Titre:** {doc['titre']}")
                    st.write(f"**Type:** {doc['type']}")
                    st.write(f"**Formation:** {doc['formation']}")
                    st.write(f"**Filière:** {doc['filiere']}")
                    st.write(f"**Auteur:** {doc['auteur']}")
                    if 'date_ajout' in doc:
                        st.write(f"**Date d'ajout:** {doc['date_ajout']}")
                
                with col2:
                    if st.button(f"✏️ Modifier", key=f"edit_{doc['id']}"):
                        st.session_state[f'editing_{doc["id"]}'] = True
                    
                    if st.button(f"🗑️ Supprimer", key=f"del_{doc['id']}"):
                        supprimer_document(doc['id'])
                        st.success("Document supprimé avec succès!")
                        st.rerun()
                
                # Formulaire de modification
                if st.session_state.get(f'editing_{doc["id"]}', False):
                    st.markdown("---")
                    st.subheader("✏️ Modifier le document")
                    
                    with st.form(key=f'form_edit_{doc["id"]}'):
                        edit_annee = st.text_input("Année", value=str(doc['annee']))
                        edit_titre = st.text_area("Titre", value=doc['titre'], height=100)
                        edit_type = st.text_input("Type", value=doc['type'])
                        edit_formation = st.text_input("Formation", value=doc['formation'])
                        edit_filiere = st.text_input("Filière", value=doc['filiere'])
                        edit_auteur = st.text_input("Auteur", value=doc['auteur'])
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            submit = st.form_submit_button("💾 Enregistrer")
                        with col2:
                            cancel = st.form_submit_button("❌ Annuler")
                        
                        if submit:
                            modifier_document(doc['id'], edit_annee, edit_titre, edit_type, 
                                            edit_formation, edit_filiere, edit_auteur)
                            st.session_state[f'editing_{doc["id"]}'] = False
                            st.success("Document modifié avec succès!")
                            st.rerun()
                        
                        if cancel:
                            st.session_state[f'editing_{doc["id"]}'] = False
                            st.rerun()
    else:
        st.info("📭 Aucun document archivé pour le moment. Ajoutez-en un pour commencer!")

# AJOUTER UN DOCUMENT
elif menu == "➕ Ajouter un document":
    st.header("➕ Ajouter un nouveau document")
    
    with st.form("form_ajout"):
        col1, col2 = st.columns(2)
        
        with col1:
            annee = st.text_input("Année *", placeholder="Ex: 2024")
            type_doc = st.text_input("Type de document *", placeholder="Ex: Rapport, Mémoire, Projet tutoré, Groupe de Travail")
            formation = st.text_input("Formation *", placeholder="Ex: Initiale, Continue")
        
        with col2:
            filiere = st.text_input("Filière *", placeholder="Ex: IAS, ISE, AS, TSS, MDSMS, MAP, L2BD, MSA, ...")
            auteur = st.text_input("Auteur *", placeholder="Ex: Nom Prénom")
        
        titre = st.text_area("Titre du document *", placeholder="Ex: Modèle génératif ...", height=100)
        
        st.markdown("*Champs obligatoires")
        
        submitted = st.form_submit_button("💾 Enregistrer le document")
        
        if submitted:
            if annee and titre and type_doc and formation and filiere and auteur:
                ajouter_document(annee, titre, type_doc, formation, filiere, auteur)
                st.success("✅ Document ajouté avec succès!")
                st.balloons()
            else:
                st.error("⚠️ Veuillez remplir tous les champs obligatoires.")

# RECHERCHER
elif menu == "🔍 Rechercher":
    st.header("🔍 Recherche avancée")
    
    donnees = charger_donnees()
    
    if donnees:
        recherche = st.text_input("🔎 Rechercher dans tous les champs", 
                                   placeholder="Tapez un mot-clé...")
        
        if recherche:
            resultats = []
            recherche_lower = recherche.lower()
            
            for doc in donnees:
                # Recherche dans tous les champs
                if (recherche_lower in str(doc.get('annee', '')).lower() or
                    recherche_lower in str(doc.get('titre', '')).lower() or
                    recherche_lower in str(doc.get('type', '')).lower() or
                    recherche_lower in str(doc.get('formation', '')).lower() or
                    recherche_lower in str(doc.get('filiere', '')).lower() or
                    recherche_lower in str(doc.get('auteur', '')).lower()):
                    resultats.append(doc)
            
            st.markdown(f"### 📊 Résultats: {len(resultats)} document(s) trouvé(s)")
            
            if resultats:
                # Affichage des résultats
                for doc in resultats:
                    with st.expander(f"📄 {doc['auteur']} ({doc['annee']}) - {doc['titre'][:80]}..."):
                        st.write(f"**ID:** {doc['id']}")
                        st.write(f"**Année:** {doc['annee']}")
                        st.write(f"**Titre:** {doc['titre']}")
                        st.write(f"**Type:** {doc['type']}")
                        st.write(f"**Formation:** {doc['formation']}")
                        st.write(f"**Filière:** {doc['filiere']}")
                        st.write(f"**Auteur:** {doc['auteur']}")
            else:
                st.warning("Aucun résultat trouvé pour votre recherche.")
    else:
        st.info("Aucun document disponible pour la recherche.")

# STATISTIQUES
elif menu == "📊 Statistiques":
    st.header("📊 Statistiques des archives")
    
    donnees = charger_donnees()
    
    if donnees:
        df = pd.DataFrame(donnees)
        df['annee'] = df['annee'].astype(str)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📅 Documents par année")
            annees_count = df['annee'].value_counts().sort_index()
            st.bar_chart(annees_count)
        
        with col2:
            st.subheader("📚 Documents par type")
            types_count = df['type'].value_counts()
            st.bar_chart(types_count)
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.subheader("🎓 Documents par formation")
            formations_count = df['formation'].value_counts()
            st.bar_chart(formations_count)
        
        with col4:
            st.subheader("🔬 Documents par filière")
            filieres_count = df['filiere'].value_counts()
            st.bar_chart(filieres_count)
        
        # Tableau récapitulatif
        st.markdown("---")
        st.subheader("📋 Tableau récapitulatif")
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total documents", len(donnees))
        col2.metric("Années distinctes", df['annee'].nunique())
        col3.metric("Types distincts", df['type'].nunique())
        col4.metric("Auteurs distincts", df['auteur'].nunique())
        
        # Top 10 des auteurs les plus prolifiques
        st.markdown("---")
        st.subheader("🏆 Top 10 des auteurs les plus prolifiques")
        top_auteurs = df['auteur'].value_counts().head(10)
        st.bar_chart(top_auteurs)
        
        # Distribution par décennie
        st.markdown("---")
        st.subheader("📆 Distribution par décennie")
        df['decennie'] = (df['annee'].astype(int) // 10) * 10
        decennie_count = df['decennie'].value_counts().sort_index()
        st.bar_chart(decennie_count)
        
    else:
        st.info("Aucune donnée disponible pour générer des statistiques.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>📚 Système de Gestion des Documents Archivés ISSEA | copyright Freddy BAT (MDSMS, 2025)</p>
    </div>
    """,
    unsafe_allow_html=True
)
