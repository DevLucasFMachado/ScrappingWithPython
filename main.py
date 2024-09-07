import streamlit as st
from scrape import scrape_website


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
    print(resultado)