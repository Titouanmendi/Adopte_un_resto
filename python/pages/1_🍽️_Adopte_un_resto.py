import streamlit as st
import pandas as pd
from streamlit_dynamic_filters import DynamicFilters

# -- Set page config
apptitle = 'Adopte un resto'

st.set_page_config(page_title=apptitle, page_icon=":fork_knife_plate:")

# -- Default detector list
detectorlist = ['H1','L1', 'V1']

# Title the app
st.title('Liste de restaurants')

st.markdown("""
 * Choisissez un restaurant grâce aux filtres à gauche
""")

    
st.sidebar.markdown("## Filtres")
time_available = st.sidebar.slider('Distance (minutes)', 1, 30, 1)  # min, max, default


check1 = st.sidebar.button("Manger !")

# display dynamic multi select filters
# Créer une liste de données pour la colonne "Régime"

donnees_regime = ['Vegetarien', 'Vegan', 'Lactose free', 'pas porc', 'gluten', 'kasher','froid','chaud']
donnee_platsPasEnvie = ['Hamburger', 'Pizza', 'Hot-dog', 'Frites', 'Spaghetti Bolognaise', 'sushi'],

# Créer un DataFrame avec deux colonnes : "MaColonne" et "Régime"
dfRegime = pd.DataFrame({
    'Regime': donnees_regime
})

dfPlats = pd.DataFrame({
    'platBof': donnee_platsPasEnvie
})


dynamic_filters = DynamicFilters(dfRegime , filters=['Regime'])
dynamic_filters = DynamicFilters(dfPlats , filters=['platsBof'])
dynamic_filters.display_filters(location='sidebar')
df_filtered = dynamic_filters.filter_df()

# df = pd.read_csv("/Users/citio/Projects/squad-m/data/restaurants.csv")






