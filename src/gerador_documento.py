from docxtpl import DocxTemplate

#from docx import Documet as Document_compose

templates = {
    "Parecer":{
        "Réu - Vale Brumadinho - Padrão - Concordante": "parecer_inicial_brumadinho_padrao_concordante",
        "Réu - Vale Brumadinho - Proximidade rio, sem avaliação - Concordante": "parecer_inicial_brumadinho_distancia_concordante",
        "Réu - Vale Brumadinho - Caracteristicas e Avaliação sem fundamentação - Parcialmente Discordante": "parecer_inicial_brumadinho_avaliacao sem fundamentacao_discordante",
    },
    "Quesitos":{
        "Réu - Vale Brumadinho - Padrão": "quesitos_inicial_brumadinho_padrao",
    },
    
}

titulos_documentos = {
    "Parecer": "PARECER TÉCNICO",
    "Parecer Esclarecimento": "PARECER TÉCNICO ESCL.",
    "Quesitos": "SUG. QUES.",
}

def gerar_documento(dados, documento="Parecer", template="opcoes_parecer"):
    #composer = Composer()
    doc = DocxTemplate(rf'.\src\assets\templates\{templates[documento][template]}.docx')
    context = dados
    doc.render(context)
    doc.save(f"{titulos_documentos[documento]} {dados['autor'].upper()} x {dados['reu'].upper().replace('/', '')}.docx")

    return True
