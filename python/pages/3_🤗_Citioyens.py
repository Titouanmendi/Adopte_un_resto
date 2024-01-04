import streamlit as st
import pandas as pd
from ast import literal_eval

# -- Set page config
st.set_page_config(page_title="Adopte un resto", page_icon="🔥")

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
historique['pretty_date'] = pd.to_datetime(historique['date'], format="%d-%m-%Y").dt.strftime('%d %B %Y')
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

    st.markdown("# Mon historique")

    history_to_display = historique[['pretty_date','name','pretty_rating']].rename(
        columns={
            'pretty_date': 'Date 📆',
            'name': 'Restaurant 🍽️',
            'pretty_rating': 'Ma note ✨',
        }
    )
    st.data_editor(
        history_to_display, width=800, height=500, hide_index=True
    )


    with st.expander("Ajouter mon repas d'aujourd'hui ..."):
        today = st.selectbox(
            "Où avez-vous mangé aujourd'hui ?",
            restaurants['name']
        )
        st.radio(
        "Niveau de kiff du repas",
        [ "⭐️",  "⭐️⭐️",  "⭐️⭐️⭐️",  "⭐️⭐️⭐️⭐️",  "🌟🌟🌟🌟🌟"],
        horizontal=True
        )

        display_restaurants = st.button("Enregistrer !")


elif current_tab==CITIO_STATS:

    st.markdown("# Podium de la semaine 🥇")

    st.markdown(f"Restaurant le plus visité: LBT")
    st.markdown(f"Restaurant le mieux noté: King Marcel")


    st.markdown("# Dans l'assiette des Citioyens 🍽️")

    st.markdown(f"## Restaurants les plus visités dernièrement")
    st.markdown(f"Laure: Poke Star")
    st.markdown(f"Adrien: LBT")
    st.markdown(f"Sarah: LBT")
    st.markdown(f"Marc: Poke Star")
    st.markdown(f"Marik: King Marcel")
    st.markdown(f"Titouan: King Marcel")
    st.markdown(f"Esther: LBT")
    st.markdown(f"Alice: La Cafet de LYBY")

