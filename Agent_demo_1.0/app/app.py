import streamlit as st
from agente_v0_1 import conversar_com_agente

st.set_page_config(page_title="Agente de Requisitos", layout="centered")

st.title("🧠 Agente de Requisitos de Software")
st.markdown("Descreva sua ideia de projeto e receba sugestões de requisitos e tecnologias.")

# 🔽 Formulário: Entrada única com contexto descartado (stateless)
with st.form(key="chat_form", clear_on_submit=True):
    pergunta = st.text_area("💬 Sua ideia de projeto:", height=150)
    submitted = st.form_submit_button("Enviar")

    if submitted:
        pergunta_texto = pergunta.strip() if isinstance(pergunta, str) else ""
        if pergunta_texto == "":
            st.warning("Por favor, descreva sua ideia antes de continuar.")
        else:
            try:
                with st.spinner("Consultando o agente..."):
                    resposta = conversar_com_agente(pergunta_texto, contexto=[])

                if not isinstance(resposta, str) or resposta.strip() == "":
                    raise ValueError("Resposta inválida do agente")

                st.success("✅ Requisitos gerados com sucesso!")
                st.markdown("### 📄 Resposta do Agente:")
                st.write(resposta)

            except Exception as e:
                st.error(f"Erro ao gerar os requisitos: {e}")
