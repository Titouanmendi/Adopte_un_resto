import streamlit as st
import folium
import pandas as pd
from folium.plugins import FastMarkerCluster
from streamlit_folium import folium_static


LYBY = (48.8432804, 2.3720586)

show_map = st.toggle("Liste / Carte", value=True)

df = pd.read_csv("data/restaurants.csv")
if show_map:
    st.markdown("### Carte des restaurants")
    lat_lon = df.apply(lambda row: (row["lat"], row["lon"]), axis=1).to_list()
    m = folium.Map(location=LYBY, tiles="Cartodb Positron", zoom_start=14)
    for index, row in df.iterrows():
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
