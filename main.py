import streamlit as st
from scrape import (
    scrape_website, 
    split_dom_content, 
    clean_body_content,
    extract_body_content,
)


#Criou um titulo para o site
st.title("Raspando dados com AI")
#Cria um campo pedindo um URL para o usuário
url = st.text_input("Coloque o URL do Website")
#Cria um botão no Website
if st.button("Obter os dados"):
    #Escreve no Website a string abaixo
    st.write("Obtenção em andamento...")
    #armazena o html mandado pela função scrape_website
    resultado = scrape_website(url)
    body_content = extract_body_content(resultado)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("Dom Content", cleaned_content, height=300)

