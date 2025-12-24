import streamlit as st
import time

# Configurações iniciais
st.set_page_config(page_title="Exame Física UEM 2025", layout="centered")

# -------------------------------
# CONFIGURAÇÕES DE TEMPO
# -------------------------------
TEMPO_QUESTAO = 60
TEMPO_TOTAL_EXAME = 90 * 60  # 1h30min em segundos

# -------------------------------
# BANCO DE QUESTÕES COMPLETO
# -------------------------------
if "perguntas" not in st.session_state:
    st.session_state.perguntas = [
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
        {
            "pergunta": "43) Um corpo de 1 kg absorve 1250 cal ao ser aquecido de 30 °C a 80 °C. O calor específico é:",
            "opcoes": ["A) 0,025 cal/g°C", "B) 0,25 cal/g°C", "C) 1,25 cal/g°C", "D) 25 cal/g°C", "E) 150 cal/g°C"],
            "correta": "B"
        }
    ]

# -------------------------------
# INICIALIZAÇÃO DA SESSÃO
# -------------------------------
if "i" not in st.session_state:
    st.session_state.i = 0
    st.session_state.respostas_usuario = {} 
    st.session_state.inicio_global = time.time()
    st.session_state.inicio_questao = time.time()
    st.session_state.quiz_finalizado = False

def reiniciar():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# -------------------------------
# CÁLCULO DOS CRONÔMETROS
# -------------------------------
agora = time.time()
tempo_decorrido_total = int(agora - st.session_state.inicio_global)
tempo_restante_global = max(0, TEMPO_TOTAL_EXAME - tempo_decorrido_total)

tempo_decorrido_questao = int(agora - st.session_state.inicio_questao)
tempo_restante_questao = max(0, TEMPO_QUESTAO - tempo_decorrido_questao)

# Verificar fim do tempo total (1h30)
if tempo_restante_global <= 0:
    st.session_state.quiz_finalizado = True

# -------------------------------
# INTERFACE DO QUIZ
# -------------------------------
st.title("📘 Quiz Física – UEM 2025")

if not st.session_state.quiz_finalizado and st.session_state.i < len(st.session_state.perguntas):
    
    # 1. Relógios e Progresso
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.metric("⏳ Tempo Total (1h30)", f"{tempo_restante_global // 60}m {tempo_restante_global % 60}s")
    with col_t2:
        st.metric("⏱️ Tempo da Questão", f"{tempo_restante_questao}s")
    
    st.progress(min(tempo_decorrido_total / TEMPO_TOTAL_EXAME, 1.0))

    # Avanço automático se os 60s da questão acabarem
    if tempo_restante_questao <= 0:
        st.session_state.i += 1
        st.session_state.inicio_questao = time.time()
        st.rerun()

    st.divider()

    # 2. Exibição da Questão (TEXTO DA PERGUNTA)
    q_atual = st.session_state.perguntas[st.session_state.i]
    
    st.subheader(f"Questão {st.session_state.i + 1}")
    st.markdown(f"### {q_atual['pergunta']}") # Aqui exibe o texto da pergunta
    
    # Recuperar marcação anterior se o aluno voltou
    index_salvo = 0
    if st.session_state.i in st.session_state.respostas_usuario:
        letra = st.session_state.respostas_usuario[st.session_state.i]
        for idx, opt in enumerate(q_atual["opcoes"]):
            if opt.startswith(letra):
                index_salvo = idx

    resposta = st.radio("Escolha a opção correta:", q_atual["opcoes"], index=index_salvo, key=f"radio_{st.session_state.i}")

    st.write("")

    # 3. BOTÕES DE NAVEGAÇÃO GRANDES
    # Botão de Confirmar (Ocupa a largura toda)
    if st.button("✅ CONFIRMAR E AVANÇAR", use_container_width=True, type="primary"):
        st.session_state.respostas_usuario[st.session_state.i] = resposta[0]
        st.session_state.i += 1
        st.session_state.inicio_questao = time.time()
        st.rerun()

    # Botões de Voltar e Pular
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("⬅️ QUESTÃO ANTERIOR", use_container_width=True, disabled=(st.session_state.i == 0)):
            st.session_state.i -= 1
            st.session_state.inicio_questao = time.time()
            st.rerun()
    with col_btn2:
        if st.button("PULAR QUESTÃO ➡️", use_container_width=True):
            st.session_state.i += 1
            st.session_state.inicio_questao = time.time()
            st.rerun()

    # Botão de Sair
    if st.button("🚪 FINALIZAR EXAME E VER RESULTADOS", use_container_width=True):
        st.session_state.quiz_finalizado = True
        st.rerun()

    # Loop do cronômetro
    time.sleep(1)
    st.rerun()

# -------------------------------
# RESULTADOS FINAIS
# -------------------------------
else:
    st.success("🏁 EXAME FINALIZADO!")
    
    acertos = 0
    total = len(st.session_state.perguntas)
    
    for idx, q in enumerate(st.session_state.perguntas):
        resp = st.session_state.respostas_usuario.get(idx, "Não respondida")
        if resp == q["correta"]:
            acertos += 1
            
    st.metric("Sua Pontuação", f"{acertos} / {total}")
    
    if st.button("Reiniciar Exame", use_container_width=True):
        reiniciar()
