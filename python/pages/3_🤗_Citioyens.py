import streamlit as st
import pandas as pd
from ast import literal_eval

# -- Default detector list
detectorlist = ['H1','L1', 'V1']


MES_PREFERENCES = "Mes préférences"
MON_HISTORIQUE = "Mon historique"
CITIO_STATS = "CitioStats"

current_tab = st.sidebar.radio(
    "Communauté Citio",
    (MES_PREFERENCES, MON_HISTORIQUE, CITIO_STATS),
)

restaurants = pd.read_csv("data/restaurants.csv")
restaurants['food_constraints']=restaurants['food_constraints'].apply(literal_eval)

historique=pd.read_csv('data/historique.csv')
historique['name'] = historique['restaurant_id'].map(restaurants.set_index('id')['name'])
historique['pretty_date'] = pd.to_datetime(historique['date']).dt.strftime('%d %B %Y')
rating_mapping = {1: "⭐️", 2: "⭐️⭐️", 3: "⭐️⭐️⭐️", 4: "⭐️⭐️⭐️⭐️", 5: "🌟🌟🌟🌟🌟"}
historique['pretty_rating'] = historique['rating'].map(rating_mapping)

if current_tab==MES_PREFERENCES:
    st.markdown("# Régime préférentiel")
    
    df_food_contraints = pd.DataFrame({
        'food_constraints': restaurants['food_constraints'].explode().unique()
    })
    food_constraints = st.multiselect(
        'Mes préférences', options=df_food_contraints, default=[]
    )
    display_restaurants = st.button("Enregistrer préférences !")

    # TODO Faire que ça enregistre ! Et utilise ces valeurs dans les restos proposés


elif current_tab==MON_HISTORIQUE:
    history_to_display = historique[['pretty_date','name','pretty_rating']]
    st.data_editor(
        history_to_display, width=800, height=500
    )

