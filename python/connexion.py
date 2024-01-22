import streamlit as st

# -- Set page config
st.set_page_config(page_title="Adopte un resto", page_icon="🔥")

left_co, cent_co, last_co = st.columns(3)
with cent_co:
    st.image("assets/AdopteUnResto.png", width=300)

st.write("# Plus d'excuse pour lâcher! 🍽😋")


def authentification_et_redirection():
    # Champ d'entrée pour l'identifiant
    id_utilisateur = st.text_input("Identifiant")

    # Champ d'entrée pour le mot de passe
    mdp_utilisateur = st.text_input("Mot de passe", type="password")

    # Bouton pour soumettre le formulaire et rediriger vers une autre page
    # bouton_connexion = st.button("VITE J'AI FAIM")

    st.link_button("VITE J'AI FAIM", "http://localhost:8503/Adopte_un_resto")
    # # Redirection vers une autre page (remplacez l'URL ci-dessous par celle de votre page d'authentification)
    # #st.markdown("<script>window.location.href = 'http://localhost:8501/Adopte_un_resto';</script>", unsafe_allow_html=True)
    # st.markdown('<a href="http://localhost:8501/Adopte_un_resto" target="_blank">Rediriger</a>', unsafe_allow_html=True)


# Appeler la fonction d'authentification et redirection
authentification_et_redirection()
st.write("### C'est juste pour faire genre j'ai trop la flemme juste clique sur les onglets à gauche")
