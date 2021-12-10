import pandas as pd
import streamlit as st

import src.quesitos as qst
import src.parecer_tecnico_inicial as pti

def main():
    modulos = ["Selecione um modelo", "Quesitos", "Parecer Técnico Inicial", "Parecer Técnico de Esclarecimento"]

    st.title('Gerador de Documentos')

    modulo = st.selectbox(label="Selecione o modelo:", options=modulos)

    if modulo == "Quesitos":
        qst.pagina_quesitos()

    if modulo == "Parecer Técnico Inicial":
        pti.pagina_parecer_tecnico()

if __name__ == "__main__":
    main()