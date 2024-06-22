# rapport_auditif.py

import streamlit as st
from fpdf import FPDF
import base64

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Rapport Auditif', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
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
        f"Remarque : {remarque}\n\n"
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
                               ["légere", "moyenne", "severe", "profonde"])

surdite_lateralite = st.selectbox("Coté", 
                                  ["unilatérale", "bilatérale"])

appareils_type = st.selectbox("Type d'appareils", 
                              ["contours d'oreilles", "RIC", "INTRA"])

marque = st.selectbox("Marque", 
                      ["GN Resound", "GN Interton", "Earnet"])

embouts = st.selectbox("Embouts", 
                      ["embouts", "micro embouts"])

remarque = st.selectbox("Remarque",
                        ["Phrase 1", "Phrase 2" , "Phrase 3"])

if st.button("Générer le rapport PDF"):
    pdf = create_pdf(nom_prenom, age, surdite_type, surdite_gravite, surdite_lateralite, appareils_type, marque, embouts, remarque)
    pdf_download_link = get_pdf_download_link(pdf, "rapport_auditif.pdf")
    st.markdown(pdf_download_link, unsafe_allow_html=True)
