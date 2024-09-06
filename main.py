import streamlit as st

#Criou um titulo para o site
st.title("Raspando dados com AI")
#Cria um campo pedindo um URL para o usuário
url = st.text_imput("Coloque o URL do Website")
#Cria um botão no Website
if st.button("Obter os dados"):
    #Escreve no Website a string abaixo
    st.write("Obtenção em andamento...")