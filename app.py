# app.py
import streamlit as st
import openai
import time

st.set_page_config(page_title="SiteGen AI", layout="centered")
st.title("SiteGen AI com API da OpenAI")
st.markdown("### Gera uma LP  completa de restaurantes")
st.caption("Feito por Erick Costa – Nov/2025")

# Campo da API Key 
api_key = st.text_input("Sua OpenAI API Key", type="password", help="Pegue a sua em platform.openai.com/api-keys")
if api_key:
    openai.api_key = api_key

col1, col2 = st.columns(2)
with col1:
    nome = st.text_input("Nome do restaurante", "Pizzaria Bella Napoli")
with col2:
    cidade = st.text_input("Cidade", "São Paulo")

tipo = st.selectbox("Tipo de comida", [
    "Pizzaria", "Hamburgueria", "Comida Japonesa", 
    "Açaí", "Doceria", "Comida Saudável", "Brasileira"
])

if st.button("Gerar Site Completo", type="primary", use_container_width=True):
    if not api_key:
        st.error("Coloca sua API Key aí, irmão!")
    else:
        with st.spinner("Gerando site lindo com GPT-4o..."):
            try:
                resposta = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{
                        "role": "user",
                        "content": f"Crie um site completo, bonito e responsivo em HTML+CSS para o restaurante '{nome}', {tipo} em {cidade}. Inclua: cabeçalho com logo, menu com 8 pratos (com preço), seção sobre, contato com WhatsApp e rodapé. Use cores vibrantes e estilo moderno. Retorne APENAS o código HTML completo, sem explicação."
                    }],
                    temperature=0.7
                )
                codigo = resposta.choices[0].message.content
                codigo = codigo.replace("```html", "").replace("```", "").strip()
                
                st.success("Site gerado com sucesso!")
                st.code(codigo, language="html")
                
                st.download_button(
                    label="Baixar site.html",
                    data=codigo,
                    file_name=f"{nome.replace(' ', '_')}_site.html",
                    mime="text/html"
                )
                
                st.balloons()
                
            except Exception as e:
                st.error(f"Erro: {e}")
