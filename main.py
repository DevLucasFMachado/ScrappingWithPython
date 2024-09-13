import streamlit as st
from scrape import (
    scrape_website, 
    split_dom_content, 
    clean_body_content,
    extract_body_content,
)
from parse import parse_with_ollama

#Criou um titulo para o site
st.title("Raspando dados com AI")
#Cria um campo pedindo um URL para o usuário
url = st.text_input("Coloque o URL do Website")
#Cria um botão no Website
if st.button("Obter os dados"):
    #Escreve no Website a string abaixo
    st.write("Obtenção em andamento...")
    #armazena o html mandado pela função scrape_website
    
    dom_content = scrape_website(url) #Recebe o conteudo DOM da função
    body_content = extract_body_content(dom_content) #Pega apenas o body e salva na varaivel
    cleaned_content = clean_body_content(body_content) #Tira todas as tags e scripts do body

    st.session_state.dom_content = cleaned_content #Serve para guardar os dados de clean_content mesmo se a variavel for modificada

    with st.expander("Ver DOM Content"):
        st.text_area("Dom Content", cleaned_content, height=300) #Cria um ícone para expandir e aparecer o DOM Content

if "dom_content" in st.session_state:
    parse_description = st.text_area("Descreva o que você quer analizar")  #Recebe a descrição para mandar para a LLM

    if st.button("Analizar"): #Cria um botão
        st.write("Analizando o DOM Content") #Cria um Texto

        dom_chunks = split_dom_content(st.session_state.dom_content) #Divide o conteúdo de dom_content em pedaços para que a LLM consiga interpreta-los
        resultado = parse_with_ollama(dom_chunks, parse_description) #Recebe o produto final organizado da LLM
        st.write(resultado)