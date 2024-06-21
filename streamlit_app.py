import streamlit as st

st.title("Rapport Auditif")

# Informations générales
age = st.number_input("Âgé(e) de", min_value=0, max_value=120, value=25, step=1)

surdite_type = st.selectbox("Présente une surdité de", 
                            ["transmission", "perception", "mixte"])

surdite_gravite = st.selectbox("Gravité de la surdité", 
                               ["légere", "moyenne", "severe", "profonde"])

surdite_lateralite = st.selectbox("Latéralité de la surdité", 
                                  ["unilatérale", "bilatérale"])

# Proposition d'appareils
appareils_type = st.selectbox("Nous avons proposé des appareils", 
                              ["contours d'oreilles", "RIC", "INTRA"])

marque = st.selectbox("de la marque", 
                      ["GN Resound", "GN Interton", "Earnet"])

embouts = st.text_input("avec des embouts")

st.write("### Conclusion")

st.write("Les appareils auditifs mis à l'essai apportent un excellent gain d'intelligibilité de la parole et sont très bien acceptés.")

st.write("Nous contrôlerons régulièrement ses seuils sans appareils et son gain avec appareils pour assurer un bon entretien de ses aides auditives et une bonne efficacité de l'adaptation prothétique.")

# Ajouter un bouton pour imprimer
st.write("\n\n")
st.button("Imprimer ce rapport")
