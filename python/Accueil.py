import streamlit as st
import pandas as pd

# -- Set page config
st.set_page_config(page_title="Adopte un resto", page_icon="🔥")

left_co, cent_co, last_co = st.columns(3)
with cent_co:
    st.image("assets/AdopteUnResto.png", width=300)

filters = pd.DataFrame(
    {
        "Filtre": ["Goûter", "Vegan uniquement", "Arrondissement", "Prix", "Lieu"],
        "Description": ["Spécial patisseries végan, la touche du chef", "Restaurant 100% végan pour limiter les prises de tête", "Arrondissement, contient Montrouge flemme de ma part de faire un cas à part", "€ (0-10), €€ (10-20) et €€€ (20-plus)","Permet de choisir pour que ce soit 'proche' de chez toi ou de ton taff"],
    }
)

st.write("# Plus d'excuse pour lâcher! 🍽😋")

st.write("## Petit guide d'utilisation de ce super site :")

st.write("T'as deux onglets, l'un permet de voir une carte avec la position des restaurants ou la liste. Le second permet de te proposer 3 restaurants ou boulangeries au hasard si tu cherches de l'inspi !")
st.write("Dans le premier t'as différents filtres. Voici à quoi ils servent :")
st.dataframe(filters, hide_index=True)
st.write("Si jamais t'as des bugs ou des idées d'amélioration dis moi (nouvelle feature, adresse à ajouter...)!! (Genre vraiment c'est du 'taff cool' pour moi)")

st.write("### Et oui t'as bien lu j'ai listé les patisseries véganes (c'était le but à la base). J'espère que tu ne connaîtras plus jamais le désespoir de l'absence de goûter 😁")
