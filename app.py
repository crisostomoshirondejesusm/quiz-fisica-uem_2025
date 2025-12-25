import streamlit as st
import time

# ======================================================
# CONFIGURAÇÃO DA PÁGINA
# ======================================================
st.set_page_config(
    page_title="Simulado de Física – UEM 2025",
    layout="centered"
)

# ======================================================
# BANCO DE QUESTÕES (EXEMPLO)
# ======================================================
QUESTOES = [
    {
        "id": 46,
        "pergunta": "O gráfico da lei do deslocamento de Wien mostra três corpos X, Y e Z. Qual deles tem menor temperatura?",
        "opcoes": ["A. X", "B. Y", "C. Z", "D. X = Y", "E. Y = Z"],
        "correta": "B"
    },
    {
        "id": 47,
        "pergunta": "Uma estrela irradia potência de 2,43×10²⁴ W. Qual a temperatura aproximada?",
        "opcoes": ["A. 19000 K", "B. 24000 K", "C. 28000 K", "D. 30000 K", "E. 34000 K"],
        "correta": "A"
    },
]

# ======================================================
# FUNÇÃO RESET
# ======================================================
def reset():
    st.session_state.clear()
    st.rerun()

# ======================================================
# ESTADOS
# ======================================================
if "i" not in st.session_state:
    st.session_state.i = 0

if "respostas" not in st.session_state:
    st.session_state.respostas = {}

if "inicio_total" not in st.session_state:
    st.session_state.inicio_total = time.time()

if "inicio_questao" not in st.session_state:
    st.session_state.inicio_questao = time.time()

if "fim" not in st.session_state:
    st.session_state.fim = False

# ======================================================
# TEMPOS
# ======================================================
TEMPO_TOTAL = 90 * 60      # 90 minutos
TEMPO_QUESTAO = 30         # 30 segundos por questão

tempo_total_restante = max(
    0, TEMPO_TOTAL - int(time.time() - st.session_state.inicio_total)
)

tempo_q_restante = max(
    0, TEMPO_QUESTAO - int(time.time() - st.session_state.inicio_questao)
)

# ======================================================
# CABEÇALHO
# ======================================================
st.title("🧪 Simulado de Física – UEM 2025")

st.info(f"⏳ Tempo total restante: {tempo_total_restante//60}m {tempo_total_restante%60}s")
st.warning(f"⏱️ Tempo desta questão: {tempo_q_restante}s")

st.divider()

# ======================================================
# FIM AUTOMÁTICO
# ======================================================
if tempo_total_restante <= 0:
    st.session_state.fim = True

# ======================================================
# QUIZ
# ======================================================
if not st.session_state.fim:

    q = QUESTOES[st.session_state.i]

    st.subheader(f"Questão {q['id']}")

    resposta = st.radio(
        q["pergunta"],
        q["opcoes"],
        key=f"q_{st.session_state.i}"
    )

    # ⏱️ ESTOURO DO TEMPO DA QUESTÃO
    if tempo_q_restante <= 0:
        st.session_state.respostas[st.session_state.i] = "Sem resposta"
        st.session_state.i += 1
        st.session_state.inicio_questao = time.time()
        st.rerun()

    col1, col2, col3 = st.columns(3)

    if col1.button("⬅️ Anterior", disabled=st.session_state.i == 0):
        st.session_state.i -= 1
        st.session_state.inicio_questao = time.time()
        st.rerun()

    if col2.button("💾 Guardar"):
        st.session_state.respostas[st.session_state.i] = resposta[0]
        st.success("Resposta guardada")

    if col3.button("➡️ Próxima"):
        st.session_state.respostas[st.session_state.i] = resposta[0]
        st.session_state.i += 1
        st.session_state.inicio_questao = time.time()
        st.rerun()

# ======================================================
# RESULTADOS
# ======================================================
else:
    st.success("🎉 Fim do Simulado!")

    acertos = sum(
        1 for i, q in enumerate(QUESTOES)
        if st.session_state.respostas.get(i) == q["correta"]
    )

    nota = (acertos / len(QUESTOES)) * 20

    st.metric("✔️ Acertos", acertos)
    st.metric("📊 Nota", f"{nota:.1f} / 20")

    if st.button("🔄 Refazer"):
        reset()
