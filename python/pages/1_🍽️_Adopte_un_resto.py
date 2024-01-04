import streamlit as st
import pandas as pd
from ast import literal_eval

import folium
from folium.plugins import FastMarkerCluster
from streamlit_folium import folium_static

# -- Set page config
apptitle = 'Adopte un resto'

st.set_page_config(page_title=apptitle, page_icon=":fork_knife_plate:")

# -- Default detector list
detectorlist = ['H1','L1', 'V1']


# -- Sidebar

df = pd.read_csv("data/restaurants.csv")
df['food_constraints']=df['food_constraints'].apply(literal_eval)
df['food_type']=df['food_type'].apply(literal_eval)

    
st.sidebar.markdown("## Filtres")

time_available = st.sidebar.slider('Distance (minutes)', 0, 30, 1)  

df_food_contraints = pd.DataFrame({
    'food_constraints': df['food_constraints'].explode().unique()
})
food_constraints = st.sidebar.multiselect(
    'Régime', options=df_food_contraints, default=[]
)

# df_food_type = pd.DataFrame({
#     'food_type': df['food_type'].explode().unique()
# })
# food_types = st.sidebar.multiselect(
#     'Pas envie', options=df_food_type, default=[]
# )

price = st.sidebar.radio(
    "Prix",
    ("€", "€€", "€€€"),
    help="(€ (0-10), €€ (10-20) et €€€ (20-plus)",
)

price_mapping = {"€":1, "€€":2, "€€€":3}
price_value = price_mapping[price]


filtered_df = df[df['dist_minutes']<=time_available].assign(**{
    'all_constraints_validated': lambda df: df['food_constraints'].apply(lambda c: set(food_constraints) <= set(c))
})
filtered_df = filtered_df[filtered_df['all_constraints_validated']]

filtered_df = filtered_df[filtered_df['price']<=price_value]

print(filtered_df)
  

display_restaurants = st.sidebar.button("Manger !")


# -- Main page

LYBY = (48.8432804, 2.3720586)

show_map = st.toggle("Liste / Carte", value=True)

# df = pd.read_csv("data/restaurants.csv")
if show_map:
    st.markdown("### Carte des restaurants")
    lat_lon = filtered_df.apply(lambda row: (row["lat"], row["lon"]), axis=1).to_list()
    m = folium.Map(location=LYBY, tiles="Cartodb Positron", zoom_start=14)
    for index, row in filtered_df.iterrows():
        popup_content = (
            f'<h3>{row["name"]}</h3>'
            f'<p><b>Food Type:</b> {row["food_type"]}</p>'
            f'<p><b>Price:</b> {row["price"]}</p>'
            f'<p><b>Distance (minutes):</b> {row["dist_minutes"]}</p>'
            f'<p><b>Food Constraints:</b> {row["food_constraints"]}</p>'
        )
        folium.Marker(
            [row["lat"], row["lon"]], popup=folium.Popup(popup_content, max_width=300)
        ).add_to(m)
    FastMarkerCluster(data=lat_lon).add_to(m)

    folium_static(m, width=800, height=500)
else:
    st.markdown("### Liste des restaurants")