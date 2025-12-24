import streamlit as st
import time

# Configurações iniciais
st.set_page_config(page_title="Exame Física UEM 2025", layout="centered")

# -------------------------------
# BANCO DE QUESTÕES
# -------------------------------
perguntas = [
    {
        "pergunta": "40) Um recipiente com água é colocado sobre um fogão aceso. O aquecimento da água ocorre principalmente por:",
        "opcoes": ["A) Condução", "B) Irradiação", "C) Convecção", "D) Radiação", "E) Evaporação"],
        "correta": "C"
    },
    {
        "pergunta": "41) Quais grandezas permitem distinguir um tipo de onda de outro?",
        "opcoes": ["A) Intensidade, área e velocidade", "B) Amplitude, velocidade, frequência e comprimento de onda", "C) Polarização, massa e energia", "D) Altura, timbre e intensidade", "E) Sentido e direção apenas"],
        "correta": "B"
    },
    {
        "pergunta": "42) Um transmissor de rádio opera a 20 MHz. Qual é o comprimento de onda emitido?",
        "opcoes": ["A) 5 m", "B) 10 m", "C) 15 m", "D) 20 m", "E) 25 m"],
        "correta": "C"
    },
    # ... (as outras questões seguem a mesma lógica)
]

TEMPO_MAX = 60 # Alterado para 60 segundos

# -------------------------------
# CONTROLO DE SESSÃO
# -------------------------------
if "i" not in st.session_state:
    st.session_state.i = 0
    st.session_state.pontos = 0
    st.session_state.erradas = []
    st.session_state.inicio = time.time()
    st.session_state.quiz_finalizado = False

def reiniciar():
    st.session_state.i = 0
    st.session_state.pontos = 0
    st.session_state.erradas = []
    st.session_state.inicio = time.time()
    st.session_state.quiz_finalizado = False
    st.rerun()

# -------------------------------
# INTERFACE
# -------------------------------
st.title("📘 Quiz Física – UEM 2025")

if not st.session_state.quiz_finalizado and st.session_state.i < len(perguntas):
    q = perguntas[st.session_state.i]
    
    # Lógica de Tempo
    tempo_passado = int(time.time() - st.session_state.inicio)
    tempo_restante = TEMPO_MAX - tempo_passado

    if tempo_restante <= 0:
        st.session_state.erradas.append((q["pergunta"], "Tempo Expirado", q["correta"]))
        st.session_state.i += 1
        st.session_state.inicio = time.time()
        st.rerun()

    # Exibição do Quiz
    st.info(f"⏱️ Questão {st.session_state.i + 1}/{len(perguntas)} | Tempo restante: {tempo_restante}s")
    
    resposta = st.radio(q["pergunta"], q["opcoes"], key=f"q_{st.session_state.i}")

    st.write("---")
    
    # BOTÕES SEPARADOS
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("✅ Responder"):
            letra = resposta[0]
            if letra == q["correta"]:
                st.session_state.pontos += 1
            else:
                st.session_state.erradas.append((q["pergunta"], letra, q["correta"]))
            
            st.session_state.i += 1
            st.session_state.inicio = time.time()
            st.rerun()

    with col2:
        if st.button("🔄 Reiniciar"):
            reiniciar()

    with col3:
        if st.button("🚪 Sair"):
            st.session_state.quiz_finalizado = True
            st.rerun()

    # Atualização do cronômetro em tempo real
    time.sleep(1)
    st.rerun()

# -------------------------------
# RESULTADO FINAL
# -------------------------------
else:
    st.success("🏁 Quiz Encerrado!")
    st.metric("Acertos", f"{st.session_state.pontos}")
    st.metric("Erros/Não respondidas", f"{len(st.session_state.erradas)}")

    if st.session_state.erradas:
        with st.expander("Ver Correções"):
            for p, r, c in st.session_state.erradas:
                st.write(f"**{p}**")
                st.write(f"Sua resposta: :red[{r}] | Correta: :green[{c}]")
                st.divider()

    if st.button("Tentar Novamente"):
        reiniciar()
