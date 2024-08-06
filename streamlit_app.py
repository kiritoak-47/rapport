# rapport_auditif.py

import streamlit as st
from fpdf import FPDF
import base64

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 20, '', 0, 1)  
        self.cell(0, 10, 'Rapport Auditif', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.set_x((210 - 150) / 2)  # Center the text
        self.multi_cell(150, 10, body)  # Adjust the width of the multi-cell
        self.ln()

def create_pdf(nom_prenom, age, surdite_type, surdite_gravite, surdite_lateralite, appareils_type, marque, embouts, remarque):
    pdf = PDF()
    pdf.add_page()

    text = (
        f"\n \n Mr/Mme {nom_prenom}, âgé(e) de {age} ans, présente une surdité de {surdite_type}, "
        f"{surdite_gravite}, et {surdite_lateralite}. Nous avons proposé des appareils {appareils_type} "
        f"de la marque {marque} avec des {embouts}.\n\n"
        "Les appareils auditifs mis à l'essai apportent un excellent gain d'intelligibilité de la parole "
        "et sont très bien acceptés.\n\n"
        f"Observation :\n {remarque}\n\n"
        "Nous contrôlerons régulièrement ses seuils sans appareils et son gain avec appareils pour assurer "
        "un bon entretien de ses aides auditives et une bonne efficacité de l'adaptation prothétique.\n\n"
        "Donc il s'agit d'un appareillage concluant."
    )

    pdf.chapter_body(text)
    return pdf

def get_pdf_download_link(pdf, filename):
    pdf_output = pdf.output(dest="S").encode("latin1")
    b64 = base64.b64encode(pdf_output).decode('latin1')
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}">Télécharger le rapport</a>'
    return href

st.title("Rapport Auditif \n \n")

nom_prenom = st.text_input("Mr/Mme")

age = st.number_input("Age", min_value=0, max_value=120, value=25, step=1)

surdite_type = st.selectbox("Type de surdité", 
                            ["transmission", "perception", "mixte"])

surdite_gravite = st.selectbox("Niveau de surdité", 
                               ["légere", "moyenne", "severe", "profonde", "moyenne a severe", "severe a profonde"])

surdite_lateralite = st.selectbox("Coté", 
                                  ["unilatérale", "bilatérale"])

appareils_type = st.selectbox("Type d'appareils", 
                              ["contours d'oreilles", "contours d'oreilles a ecouteur déporté", "Intra-auriculaire"])

marque = st.selectbox("Marque", 
                      ["GN Resound", "GN Interton", "Earnet"])

embouts = st.selectbox("Embouts", 
                      ["embouts", "micro embouts"])

remarque = st.selectbox("Observation",
                        ["Les résultats du test audiométrique montrent une amélioration significative de l'audition du patient avec l'appareil auditif. Les niveaux d'appareillage sont ajustés pour maximiser le confort auditif tout en maintenant une excellente clarté sonore.", 
                         "Le test de réduction du bruit a montré que l'appareil auditif offre une réduction efficace des bruits ambiants tout en permettant une clarté de parole optimale. Le patient a remarqué une amélioration notable de la qualité sonore dans les environnements bruyants." ,
                         "Le patient a bien réagi à l'appareil auditif dès la première utilisation. Il a noté une amélioration significative de son audition et s'est rapidement adapté au nouvel appareil. Aucun problème de confort ou de fonctionnement n'a été signalé." ,
                         "Après le teste d'appareil, le patient se dit très satisfait de l'appareil auditif. Elle a remarqué une meilleure compréhension des conversations en milieu bruyant et s'est bien habituée aux réglages automatiques. Un léger ajustement de volume a été effectué pour un confort optimal." ,
                         "La fonctionnalité de suppression des acouphènes a été activée et configurée avec succès, offrant un soulagement significatif au patient" ,
                         "Le test de réglage en milieu extérieur a montré que les appareils auditifs réduisent efficacement le bruit, tout en maintenant une bonne clarté de la parole." ,
                         "Le mode de directionnalité du microphone a été ajusté pour se concentrer sur les sources sonores frontales, améliorant la clarté des conversations en face à face"])

if st.button("Générer le rapport"):
    if nom_prenom and age and surdite_type and surdite_gravite and surdite_lateralite and appareils_type and marque and embouts and remarque:
        pdf = create_pdf(nom_prenom, age, surdite_type, surdite_gravite, surdite_lateralite, appareils_type, marque, embouts, remarque)
        pdf_download_link = get_pdf_download_link(pdf, "rapport_auditif.pdf")
        st.markdown(pdf_download_link, unsafe_allow_html=True)
    else:
        st.error("Tous les champs doivent être remplis.")
