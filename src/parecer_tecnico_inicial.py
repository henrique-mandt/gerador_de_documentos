import datetime
import os
import locale
import streamlit as st

from .gerador_documento import templates, gerar_documento

locale.setlocale(locale.LC_ALL, 'pt_br.UTF-8')


def brumadinho_padrao_concordante():
    atingido = st.selectbox("Imóvel afetado pelos rejeitos?", options=["Não","Parcialmente", "Sim"])
    distancia_rio = st.text_input("Distância até o leito do rio:", value="580,00 metros", help="Ex.: 580,00 metros")
    zas = st.selectbox("Inserido em Zona de Autossalvamento - ZAS:", options=["Não","Parcialmente", "Sim"], index=0)
    abastecimento = st.selectbox("Tipo de abastecimento de água do imóvel e região:", options=["COPASA","Poço artesiano", "Copasa e Poço artesiano", "Outros"], index=0)
    ano_pesquisa_mercado = st.text_input("Ano da pesquisa de mercado:", value="2021")
    valor_2018 = float(st.text_input("Valor em 2018:", value="R$ 200.000,00").split('R$')[-1].replace('.','').replace(',','.'))
    valor_2019 = float(st.text_input("Valor em 2019:", value="R$ 300.000,00").split('R$')[-1].replace('.','').replace(',','.'))
    valor_2021 = float(st.text_input("Valor em 2020:", value="R$ 400.000,00").split('R$')[-1].replace('.','').replace(',','.'))

    variacao_2018_2019 = str(round(((valor_2019 - valor_2018)/valor_2019)*100, 2)).replace('.',',')
    variacao_2018_2021 = str(round(((valor_2021 - valor_2018)/valor_2021)*100, 2)).replace('.',',')

    dados_parecer = {   
    'atingido': atingido,
    'distancia_rio': distancia_rio,
    'zas': zas,
    'abastecimento': abastecimento,
    'ano_pesquisa_mercado': ano_pesquisa_mercado,
    'valor_2018': valor_2018,
    'valor_2019': valor_2019,
    'valor_2021': valor_2021,
    'variacao_2018_2019': variacao_2018_2019,
    'variacao_2018_2021': variacao_2018_2021, 
    }

    return dados_parecer

def brumadinho_distancia_concordante():
    atingido = st.selectbox("Imóvel afetado pelos rejeitos?", options=["Não","Parcialmente", "Sim"])
    distancia_rio = st.text_input("Distância até o leito do rio:", value="580,00 metros", help="Ex.: 580,00 metros")
    zas = st.selectbox("Inserido em Zona de Autossalvamento - ZAS:", options=["Não","Parcialmente", "Sim"], index=0)
    abastecimento = st.selectbox("Tipo de abastecimento de água do imóvel e região:", options=["COPASA","Poço artesiano", "Copasa e Poço artesiano", "Outros"], index=0)
    
    dados_parecer = {   
    'atingido': atingido,
    'distancia_rio': distancia_rio,
    'zas': zas,
    'abastecimento': abastecimento,
    }

    return dados_parecer

def brumadinho_avaliacao_discordante():
    atingido = st.selectbox("Imóvel afetado pelos rejeitos?", options=["Não","Parcialmente", "Sim"])
    distancia_rio = st.text_input("Distância até o leito do rio:", value="580,00 metros", help="Ex.: 580,00 metros")
    zas = st.selectbox("Inserido em Zona de Autossalvamento - ZAS:", options=["Não","Parcialmente", "Sim"], index=0)
    abastecimento = st.selectbox("Tipo de abastecimento de água do imóvel e região:", options=["COPASA","Poço artesiano", "Copasa e Poço artesiano", "Outros"], index=0)
    
    dados_parecer = {   
    'atingido': atingido,
    'distancia_rio': distancia_rio,
    'zas': zas,
    'abastecimento': abastecimento,
    }

    return dados_parecer

def pagina_parecer_tecnico():
    opcoes_parecer = templates["Parecer"].keys()

    st.title('Gerador de Parecer Técnico')

    template = str(st.selectbox(label="Selecione o modelo:", options=opcoes_parecer))
    
    n_autos = st.text_input('N.º dos autos:', value="5002036-50.2019.8.13.0090", help="Ex.: 5002036-50.2019.8.13.0090")
    vara = st.text_input("Vara:", value="2ª Vara Cível, Criminal e de Execuções Penais da Comarca de Brumadinho", help="2ª Vara Cível, Criminal e de Execuções Penais da Comarca de Brumadinho")
    autor = st.text_input("Autor:", value="Maria Vera Lucia ", help="Ex.: ")
    reu =st.text_input("Réu", value="Você", help="Ex.: ")
    endereco_imovel = st.text_input("Endereço do imóvel", value="Rua Carlos Nogueira, n.º 32, Bairro São Conrado, em Brumadinho/MG", help="Ex.: Rua X, n.º 00")
    data_vistoria = st.date_input("Data da vistoria", value=datetime.date(2021,7,6), help="Ex.: 13/07/2021").strftime("%d/%m/%Y")
    id_laudo = st.text_input("ID do Laudo Pericial:", value="6329018070", help="Ex.: 6329018070")

    dados = {
    'n_autos': n_autos,
    'vara': vara,
    'autor': autor,
    'reu': reu,
    'endereco_imovel': endereco_imovel,
    'data_vistoria': data_vistoria,
    'id_laudo': id_laudo,
    }

    if template == list(templates["Parecer"])[0]:
        dados_parecer = brumadinho_padrao_concordante()

    if template == list(templates["Parecer"])[1]:
        dados_parecer = brumadinho_distancia_concordante()
    
    if template == list(templates["Parecer"])[2]:
        dados_parecer = brumadinho_avaliacao_discordante()

    dados.update(dados_parecer)

    if st.button('Gerar parecer técnico'):
        _ = gerar_documento(dados, documento="Parecer", template=template)
        if _:
            st.success(f"Parecer Técnico gerado com sucesso! \n\nDisponível em: {os.getcwd()}")
        