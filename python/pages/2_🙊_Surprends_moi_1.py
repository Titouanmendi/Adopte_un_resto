import streamlit as st
import folium
import pandas as pd
from folium.plugins import FastMarkerCluster
from streamlit_folium import folium_static


LYBY = (48.8432804,2.3720586)

show_map = st.toggle("Liste / Carte", value=True)

df = pd.read_csv('data/1_resto.csv')
if show_map:
    st.markdown(
            "### Carte des restaurants"
        )
    lat_lon = df.apply(lambda row: (row['lat'],row['lon'])).to_list()
    m = folium.Map(location=LYBY, tiles="Cartodb Positron", zoom_start=14)
    FastMarkerCluster(data=lat_lon).add_to(m)

    folium_static(m, width=800, height=500)
else:
    st.markdown(
            "### Liste des restaurants"
        ) 
