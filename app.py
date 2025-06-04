import streamlit as st
import requests

# Configuration de la page
st.set_page_config(
    page_title="Prédiction de Revenu Annuel", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS personnalisé
st.markdown("""
    <style>
        .header {
            font-size: 28px;
            font-weight: bold;
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .section {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .section-title {
            font-size: 18px;
            font-weight: bold;
            color: #3498db;
            margin-bottom: 15px;
        }
        .prediction {
            font-size: 24px;
            color: #27ae60;
            font-weight: bold;
            text-align: center;
            padding: 20px;
            background-color: #e8f5e9;
            border-radius: 10px;
            margin-top: 20px;
        }
        .stButton>button {
            background-color: #3498db;
            color: white;
            font-weight: bold;
            width: 100%;
            padding: 10px;
            border-radius: 5px;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            background-color: #2980b9;
            transform: scale(1.02);
        }
        .stRadio>div {
            flex-direction: row;
            gap: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Titre principal
st.markdown('<div class="header">Estimateur de Revenu Annuel au Maroc</div>', unsafe_allow_html=True)
st.markdown("Renseignez les informations ci-dessous pour obtenir une estimation de votre revenu annuel potentiel.")

# Initialisation des étapes dans session_state
if 'current_step' not in st.session_state:
    st.session_state.current_step = 1
if 'form_data' not in st.session_state:
    st.session_state.form_data = {}

# Fonction pour passer à l'étape suivante
def next_step():
    st.session_state.current_step += 1

# Fonction pour revenir à l'étape précédente
def prev_step():
    st.session_state.current_step -= 1

# Fonction pour créer des sections organisées
def create_section(title):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
    return st.container()

# Étape 1: Informations Personnelles
if st.session_state.current_step == 1:
    with st.form("step1_form"):
        st.markdown('<div class="section-title">Informations Personnelles</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.slider("Âge", 16, 63, 30, help="Sélectionnez votre âge entre 16 et 63 ans")
            categorie_age = st.selectbox("Catégorie d'âge", ["Jeune", "Adulte", "Senior", "Âgé"])
            niveau_education = st.selectbox("Niveau d'éducation", 
                ["Sans niveau", "Fondamental", "Secondaire", "Supérieur"])
        
        with col2:
            annees_experience = st.slider("Années d'expérience", 0, 40, 5)
            groupe_socio = st.selectbox("Groupe socioprofessionnel", 
                ["Groupe 1", "Groupe 2", "Groupe 3", "Groupe 4", "Groupe 5", "Groupe 6"])
            sexe = st.radio("Genre", ["Femme", "Homme"], horizontal=True)
        
        submitted = st.form_submit_button("Suivant", use_container_width=True)
        
        if submitted:
            st.session_state.form_data.update({
                "age": age,
                "categorie_age": categorie_age,
                "niveau_education": niveau_education,
                "annees_experience": annees_experience,
                "groupe_socio": groupe_socio,
                "sexe": sexe
            })
            next_step()
            st.rerun()

# Étape 2: Situation Familiale et Résidentielle
elif st.session_state.current_step == 2:
    with st.form("step2_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="section-title">Situation Familiale</div>', unsafe_allow_html=True)
            statut_matrimonial = st.selectbox("Statut matrimonial", 
                ["Célibataire", "Divorcé(e)", "Marié(e)", "Veuf(ve)"])
            nombre_enfants = st.slider("Nombre d'enfants", 0, 10, 0)
        
        with col2:
            st.markdown('<div class="section-title">Situation Résidentielle</div>', unsafe_allow_html=True)
            type_logement = st.selectbox("Type de logement", 
                ["Logement_Basique", "Logement_Standard", "Logement_Confort", 
                 "Logement_Supérieur", "Résidence_Prestige"])
            milieu = st.radio("Environnement", ["Rural", "Urbain"], horizontal=True)
            possesion_bien = st.selectbox("Propriétaire immobilier", [0, 1],
                format_func=lambda x: "Oui" if x == 1 else "Non")
        
        col_prev, _, col_next = st.columns([1, 3, 1])
        with col_prev:
            if st.form_submit_button("Précédent", use_container_width=True):
                prev_step()
                st.rerun()
        with col_next:
            submitted = st.form_submit_button("Suivant", use_container_width=True)
        
        if submitted:
            st.session_state.form_data.update({
                "statut_matrimonial": statut_matrimonial,
                "nombre_enfants": nombre_enfants,
                "type_logement": type_logement,
                "milieu": milieu,
                "possesion_bien": possesion_bien
            })
            next_step()
            st.rerun()

# Étape 3: Informations Professionnelles et Géographiques
elif st.session_state.current_step == 3:
    with st.form("step3_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="section-title">Informations Professionnelles</div>', unsafe_allow_html=True)
            secteur_emploi = st.radio("Secteur d'emploi", 
                ["Agriculture", "Chômeur", "Industrie", "Privé", "Public", "Services"], 
                horizontal=True)
            visa_Schengen = st.selectbox("Accès à l'espace Schengen", [0, 1],
                format_func=lambda x: "Oui" if x == 1 else "Non")
        
        with col2:
            st.markdown('<div class="section-title">Localisation Géographique</div>', unsafe_allow_html=True)
            region = st.selectbox("Région", [
                "Béni_Mellal_Khénifra", "Casablanca_Settat", "Dakhla_Oued_Ed_Dahab",
                "Drâa_Tafilalet", "Fès_Meknès", "Guelmim_Oued_Noun",
                "Laâyoune_Sakia_El_Hamra", "Marrakech_Safi", "Oriental",
                "Rabat_Salé_Kénitra", "Souss_Massa", "Tanger_Tétouan_Al_Hoceïma"
            ])
        
        col_prev, _, col_submit = st.columns([1, 3, 1])
        with col_prev:
            if st.form_submit_button("Précédent", use_container_width=True):
                prev_step()
                st.rerun()
        with col_submit:
            submitted = st.form_submit_button("Estimer le Revenu", use_container_width=True)
        
        if submitted:
            st.session_state.form_data.update({
                "secteur_emploi": secteur_emploi,
                "visa_Schengen": visa_Schengen,
                "region": region
            })
            
            # Conversion des données pour l'API
            categorie_age_map = {"Jeune": 0.0, "Adulte": 0.33, "Senior": 0.66, "Âgé": 1.0}
            niveau_education_map = {
                "Sans niveau": 0.0, 
                "Fondamental": 0.33, 
                "Secondaire": 0.66, 
                "Supérieur": 1.0
            }
            groupe_socio_map = {
                "Groupe 1": 0.0, "Groupe 2": 0.2, "Groupe 3": 0.4,
                "Groupe 4": 0.6, "Groupe 5": 0.8, "Groupe 6": 1.0
            }

            input_data = {
                "age": float(st.session_state.form_data["age"]),
                "categorie_age": categorie_age_map[st.session_state.form_data["categorie_age"]],
                "niveau_education": niveau_education_map[st.session_state.form_data["niveau_education"]],
                "annees_experience": float(st.session_state.form_data["annees_experience"]),
                "categorie_socio": groupe_socio_map[st.session_state.form_data["groupe_socio"]],
                "nombre_enfants": float(st.session_state.form_data["nombre_enfants"]),
                "possesion_bien": st.session_state.form_data["possesion_bien"],
                "visa_Schengen": st.session_state.form_data["visa_Schengen"],
                "sexe": 1 if st.session_state.form_data["sexe"] == "Homme" else 0,
                "statut_matrimonial": st.session_state.form_data["statut_matrimonial"],
                "secteur_emploi": st.session_state.form_data["secteur_emploi"],
                "milieu": st.session_state.form_data["milieu"],
                "type_logement": st.session_state.form_data["type_logement"],
                "region": st.session_state.form_data["region"]
            }

            # Affichage d'un spinner pendant la requête
            with st.spinner('Calcul en cours...'):
                try:
                    response = requests.post("http://localhost:8000/predict", json=input_data)
                    if response.status_code == 200:
                        prediction = response.json()["prediction"]
                        st.markdown(
                            f'<div class="prediction">Revenu annuel estimé: {prediction:,.0f} DH</div>', 
                            unsafe_allow_html=True
                        )
                        st.balloons()
                    else:
                        st.error(f"Erreur lors de la prédiction: {response.text}")
                except Exception as e:
                    st.error(f"Erreur de connexion au serveur: {str(e)}")
                    st.info("Veuillez vérifier que le serveur de prédiction est en cours d'exécution.")