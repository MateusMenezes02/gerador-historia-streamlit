import streamlit as st
import google.generativeai as genai

api_key = st.sidebar.text_input("Insira sua Gemini API Key aqui:", type="password")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.warning("Por favor, insira sua Gemini API Key para continuar.")
    st.stop()

st.title("Gerador de Início de História")

nome_protagonista = st.text_input("Nome do Protagonista:")

genero = st.selectbox(
    "Gênero Literário:",
    ("Fantasia", "Ficção Científica", "Mistério", "Aventura", "Romance", "Terror")
)

local_inicial = st.radio(
    "Local Inicial da História:",
    ("Uma floresta antiga", "Uma cidade futurista", "Um castelo assombrado", "Uma nave espacial à deriva",
     "Um laboratório secreto", "Uma ilha deserta")
)

frase_desafio = st.text_area(
    "Frase de Efeito ou Desafio Inicial (será incorporada à história):",
    "Ex: 'E de repente, tudo ficou escuro.' ou 'O mapa indicava um perigo iminente.'"
)

if st.button("Gerar Início da História"):
    if nome_protagonista and frase_desafio:
        prompt = (
            f"Crie o início de uma história de '{genero}' com o protagonista chamado '{nome_protagonista}'. "
            f"A história começa em '{local_inicial}'. "
            f"Incorpore a seguinte frase ou desafio no início: '{frase_desafio}'."
            f"A introdução deve ter um ou dois parágrafos."
        )

        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)

            st.subheader("Início da História Gerado:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Ocorreu um erro ao gerar a história: {e}")
            st.info("Por favor, verifique se sua Gemini API Key está correta e funcional.")
    else:
        st.warning("Por favor, preencha o nome do protagonista e a frase/desafio inicial para gerar a história.")