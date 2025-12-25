import streamlit as st
import time
import os

# 1. Configurações da Página
st.set_page_config(page_title="Exame Unificado UEM 2025", layout="centered")

# 2. Banco de Dados (resumido aqui; usar o seu completo)
if "perguntas" not in st.session_state:
    # Insira aqui todas as 80 questões, conforme seu código original
    st.session_state.perguntas = [
        {"id": 1, "p": "Indique as soluções da equação $-|x-2|+6=2$:", "opts": ["A. x=2 v x=6", "B. x=-4 v x=4", "C. x=2", "D. x=-2 v x=6", "E. x=4"], "c": "D", "img": None},
        {"id": 2, "p": "Dizemos que $|x|>3$ se:", "opts": ["A. x ∈ ]-∞,-3[ ∪ ]3,+∞[", "B. x ∈ R", "C. x ∈ ]-3,3[", "D. x ∈ ]-∞,-3] ∪ [3,+∞[", "E. x ∈ ]3,+∞["], "c": "A", "img": None},
        # ...
    ]

# 3. Inicialização de estados
if "i" not in st.session_state: st.session_state.i = 0
if "respostas" not in st.session_state: st.session_state.respostas = {}
if "quiz_fim" not in st.session_state: st.session_state.quiz_fim = False
if "inicio_t" not in st.session_state: st.session_state.inicio_t = time.time()
if "quest_t" not in st.session_state: st.session_state.quest_t = time.time()

# Funções de navegação
def avancar():
    if st.session_state.i + 1 < len(st.session_state.perguntas):
        st.session_state.i += 1
        st.session_state.quest_t = time.time()
    else:
        st.session_state.quiz_fim = True

def voltar():
    if st.session_state.i > 0:
        st.session_state.i -= 1
        st.session_state.quest_t = time.time()

# --- Lógica de tempo ---
tempo_restante_q = int(90 - (time.time() - st.session_state.quest_t))
tempo_restante_total = int(10800 - (time.time() - st.session_state.inicio_t))
if tempo_restante_q <= 0 and not st.session_state.quiz_fim:
    avancar()
    st.experimental_rerun()
if tempo_restante_total <= 0:
    st.session_state.quiz_fim = True

# 4. Interface Principal
st.title("📚 Exame Integrado UEM 2025")

if not st.session_state.quiz_fim:
    # Cabeçalho
    c1, c2, c3 = st.columns(3)
    c1.metric("⏳ Exame", f"{tempo_restante_total//60}m")
    c2.metric("⏱️ Questão", f"{tempo_restante_q}s")
    c3.metric("📊 Progresso", f"{st.session_state.i + 1}/{len(st.session_state.perguntas)}")
    st.progress((st.session_state.i + 1)/len(st.session_state.perguntas))

    st.divider()

    # Questão Atual
    q = st.session_state.perguntas[st.session_state.i]
    st.info(f"**Matéria:** {'📐 MATEMÁTICA' if q['id'] <= 40 else '⚡ FÍSICA'}")
    
    # Imagem
    if q["img"]:
        path = f"imagens/{q['img']}"
        if os.path.exists(path): st.image(path)
        else: st.warning(f"Figura: {q['img']}")

    # Enunciado completo
    st.markdown(f"### Questão {q['id']}")
    st.write(q['p'])

    # Recupera escolha anterior
    resp_salva = st.session_state.respostas.get(st.session_state.i, None)
    idx = 0
    if resp_salva:
        for i_opt, opt in enumerate(q["opts"]):
            if opt.startswith(resp_salva): idx = i_opt

    escolha = st.radio("Selecione a opção:", q["opts"], index=idx, key=f"rad_{st.session_state.i}")

    # Botões de ação
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        if st.button("⬅️ VOLTAR", disabled=(st.session_state.i==0)):
            voltar()
            st.experimental_rerun()
    with col2:
        if st.button("✅ SALVAR"):
            st.session_state.respostas[st.session_state.i] = escolha[0]
    with col3:
        if st.button("PRÓXIMA ➡️"):
            st.session_state.respostas[st.session_state.i] = escolha[0]
            avancar()
            st.experimental_rerun()

else:
    # Resultados
    st.success("🏁 EXAME CONCLUÍDO!")
    acertos = sum(1 for i, q in enumerate(st.session_state.perguntas) if st.session_state.respostas.get(i) == q["c"])
    st.metric("Nota Final", f"{(acertos/len(st.session_state.perguntas))*20:.1f} / 20")
    
    if st.button("🔄 REINICIAR EXAME"):
        st.session_state.clear()
        st.experimental_rerun()
