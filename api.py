from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()
model = joblib.load('RandomForestRegressor_model.joblib')

class InputData(BaseModel):
    # Numerical features
    age: float
    categorie_age: float
    niveau_education: float
    annees_experience: float
    categorie_socio: float
    nombre_enfants: float
    
    # Binary features
    possesion_bien: int
    visa_Schengen: int
    
    # Secteur emploi
    secteur_emploi_Agriculture: int
    secteur_emploi_Chômeur: int
    secteur_emploi_Industrie: int
    secteur_emploi_Privé: int
    secteur_emploi_Public: int
    secteur_emploi_Services: int
    
    # Type logement
    type_logement_Logement_Basique: int
    type_logement_Logement_Standard: int
    type_logement_Logement_Confort: int
    type_logement_Logement_Supérieur: int
    type_logement_Résidence_Prestige: int
    
    # Statut matrimonial
    statut_matrimonial_Célibataire: int
    statut_matrimonial_Divorcé_e: int
    statut_matrimonial_Marié_e: int
    statut_matrimonial_Veuf_ve: int
    
    # Regions (EXACTLY as in your database)
    region_Béni_Mellal_Khénifra: int
    region_Casablanca_Settat: int
    region_Rabat_Salé_Kénitra: int
    region_Marrakech_Safi: int
    region_Fès_Meknès: int
    region_Tanger_Tétouan_Al_Hoceïma: int
    region_Oriental: int
    region_Souss_Massa: int
    region_Guelmim_Oued_Noun: int
    region_Laâyoune_Sakia_El_Hamra: int
    region_Dakhla_Oued_Ed_Dahab: int
    region_Drâa_Tafilalet: int
    
    # Milieu
    milieu_Rural: int
    milieu_Urbain: int
    
    # Sexe
    sexe_femme: int
    sexe_homme: int

@app.post("/predict")
def predict(data: InputData):
    input_array = np.array(list(data.dict().values())).reshape(1, -1)
    prediction = model.predict(input_array)
    return {"prediction": round(prediction[0], 2)}

@app.get("/health")
def health_check():
    return {"status": "OK"}