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
# BANCO DE QUESTÕES (Exemplo)
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
# INTERFACE DO USUÁRIO
# -------------------------------
st.title("📘 Quiz Física – UEM 2025")

if not st.session_state.quiz_finalizado and st.session_state.i < len(st.session_state.perguntas):
    
    # Exibição dos Tempos
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.metric("⏳ Tempo Total (1h30)", f"{tempo_restante_global // 60}m {tempo_restante_global % 60}s")
    with col_t2:
        cor_tempo = "normal" if tempo_restante_questao > 10 else "inverse"
        st.metric("⏱️ Tempo da Questão", f"{tempo_restante_questao}s", delta_color=cor_tempo)
    
    # Barra de progresso visual do exame
    progresso = tempo_decorrido_total / TEMPO_TOTAL_EXAME
    st.progress(min(progresso, 1.0), text="Progresso do tempo total")

    # Lógica de Avanço Automático por tempo de questão
    if tempo_restante_questao <= 0:
        st.warning("Tempo esgotado nesta questão! Pulando...")
        time.sleep(1)
        st.session_state.i += 1
        st.session_state.inicio_questao = time.time()
        st.rerun()

    st.divider()

    # Conteúdo da Questão
    q = st.session_state.perguntas[st.session_state.i]
    
    # Recuperar marcação prévia
    index_atual = 0
    if st.session_state.i in st.session_state.respostas_usuario:
        letra_salva = st.session_state.respostas_usuario[st.session_state.i]
        for idx, opt in enumerate(q["opcoes"]):
            if opt.startswith(letra_salva):
                index_atual = idx

    resposta = st.radio(f"Questão {st.session_state.i + 1} de {len(st.session_state.perguntas)}:", 
                        q["opcoes"], index=index_atual, key=f"radio_{st.session_state.i}")

    st.write("")

    # -------------------------------
    # BOTÕES DE NAVEGAÇÃO (GRANDES)
    # -------------------------------
    
    # Botão de Confirmar Resposta (Principal)
    if st.button("✅ RESPONDER E AVANÇAR", use_container_width=True, type="primary"):
        st.session_state.respostas_usuario[st.session_state.i] = resposta[0]
        st.session_state.i += 1
        st.session_state.inicio_questao = time.time() # Reseta o relógio para a próxima
        st.rerun()

    # Coluna para Voltar e Pular
    col_nav1, col_nav2 = st.columns(2)
    with col_nav1:
        # Botão Voltar (Desabilitado na primeira questão)
        if st.button("⬅️ QUESTÃO ANTERIOR", use_container_width=True, disabled=(st.session_state.i == 0)):
            st.session_state.i -= 1
            st.session_state.inicio_questao = time.time() # Reseta o relógio ao voltar
            st.rerun()
            
    with col_nav2:
        if st.button("PULAR QUESTÃO ➡️", use_container_width=True):
            st.session_state.i += 1
            st.session_state.inicio_questao = time.time()
            st.rerun()

    # Botões de Utilidade (Sair/Reiniciar)
    st.divider()
    col_ut1, col_ut2 = st.columns(2)
    with col_ut1:
        if st.button("🔄 REINICIAR TUDO", use_container_width=True):
            reiniciar()
    with col_ut2:
        if st.button("🚪 FINALIZAR AGORA", use_container_width=True):
            st.session_state.quiz_finalizado = True
            st.rerun()

    # Auto-refresh para o cronômetro
    time.sleep(1)
    st.rerun()

# -------------------------------
# RESULTADOS
# -------------------------------
else:
    st.success("🏁 EXAME FINALIZADO!")
    
    acertos = 0
    total = len(st.session_state.perguntas)
    
    for idx, q in enumerate(st.session_state.perguntas):
        resp = st.session_state.respostas_usuario.get(idx, "Não respondida")
        if resp == q["correta"]:
            acertos += 1
            
    st.balloons()
    st.metric("Sua Pontuação Final", f"{acertos} / {total}")
    
    if st.button("Reiniciar Quiz", use_container_width=True):
        reiniciar()
