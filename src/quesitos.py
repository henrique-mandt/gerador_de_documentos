import pandas as pd
import os

import streamlit as st
from st_aggrid import AgGrid

from .gerador_documento import gerar_documento, templates


DATA_PATH = r".\src\assets\data\quesitos.xlsx"

def get_quesitos(df, contexto='vale_brumadinho', assuntos=[]):
      
    df = df.query(f"'{contexto}' in contexto")
    df = df[df.classificacao.isin(assuntos)]
    
    colunas = ['descricao', 'quesitos']
    df = df[colunas]
     
    return df

def pagina_quesitos():
    @st.cache
    def load_data():
        df = pd.read_excel(DATA_PATH)
        return df
   
    opcoes_quesitos = templates["Parecer"].keys()

    st.title('Gerador de Quesitos')

    template = str(st.selectbox(label="Selecione o modelo:", options=opcoes_quesitos))
    
    n_autos = st.text_input('N.º dos autos:', value="5002036-50.2019.8.13.0090", help="Ex.: 5002036-50.2019.8.13.0090")
    vara = st.text_input("Vara:", value="2ª Vara Cível, Criminal e de Execuções Penais da Comarca de Brumadinho", help="2ª Vara Cível, Criminal e de Execuções Penais da Comarca de Brumadinho")
    classe = st.text_input('Classe da ação: ', value="Dano Material")
    autor = st.text_input("Autor:", value="Maria Vera Lucia ", help="Ex.: ")
    reu =st.text_input("Réu", value="Você", help="Ex.: ")
    
    dados = {
        'n_autos': n_autos,
        'vara': vara,
        'autor': autor,
        'reu': reu,
        }

    df = load_data()
    assuntos = st.multiselect('Incluir quesitos sobre:', df.classificacao.unique())
    quesitos_df = get_quesitos(df, contexto='vale_brumadinho', assuntos=assuntos)
    quesitos_dict = quesitos_df.to_dict("list")

    if st.checkbox("Preview"):
        # st.dataframe(quesitos)
        AgGrid(quesitos_df)
        st.write(quesitos_dict)

    if st.button('Gerar quesitos'):
        dados.update(quesitos_dict)
        _ = gerar_documento(dados, documento="Quesitos", template=template)
        if _:
            st.success(f"Quesitos gerados com sucesso! {os.getcwd()}")
        