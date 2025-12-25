import streamlit as st
import time
import os

# 1. Configurações da Página
st.set_page_config(page_title="Exame Unificado UEM 2025", layout="centered")

# 2. Banco de Dados (Mesclado conforme solicitado)
if "perguntas" not in st.session_state:
    # (Inserir aqui as listas m_qs e f_qs do seu código anterior)
    # Por brevidade, mantive a lógica de mesclagem que você já tem:
    m_qs = [
        {"id": 1, "p": "Indique as soluções da equação $-|x-2|+6=2$:", "opts": ["A. x=2 v x=6", "B. x=-4 v x=4", "C. x=2", "D. x=-2 v x=6", "E. x=4"], "c": "D", "img": None},
        # ... outras 39 questões de matemática ...
    ]
    f_qs = [
        {"id": 41, "p": "Um recipiente de vidro... água começa a se aquecer por:", "opts": ["A. Condução", "B. irradiação", "C. convecção", "D. condução e convecção", "E. convecção e irradiação"], "c": "C", "img": None},
        # ... outras 39 questões de física ...
    ]
    
    # Simulação da lista completa para o exemplo rodar:
    final_list = []
    # Nota: Usei um loop simples para o exemplo, mantenha seu zip(m_qs, f_qs) original
    for m, f in zip(m_qs, f_qs):
        final_list.append(m)
        final_list.append(f)
    st.session_state.perguntas = final_list

# 3. Inicialização de Estados
if "i" not in st.session_state: st.session_state.i = 0
if "respostas" not in st.session_state: st.session_state.respostas = {}
if "quiz_fim" not in st.session_state: st.session_state.quiz_fim = False
if "inicio_global" not in st.session_state: st.session_state.inicio_global = time.time()
if "inicio_questao" not in st.session_state: st.session_state.inicio_questao = time.time()

# 4. Constantes de Tempo
TEMPO_QUESTAO = 90  # segundos
TEMPO_GLOBAL = 10800 # 3 horas em segundos

def proxima_questao():
    if st.session_state.i + 1 < len(st.session_state.perguntas):
        st.session_state.i += 1
        st.session_state.inicio_questao = time.time()
    else:
        st.session_state.quiz_fim = True
    st.rerun()

# 5. Lógica de Tempo (Executa a cada refresh)
agora = time.time()
decorrido_global = agora - st.session_state.inicio_global
decorrido_questao = agora - st.session_state.inicio_questao

# Verifica fim do tempo global
if decorrido_global >= TEMPO_GLOBAL:
    st.session_state.quiz_fim = True
    st.error("⏱️ Tempo global esgotado!")

# Verifica fim do tempo da questão
if not st.session_state.quiz_fim and decorrido_questao >= TEMPO_QUESTAO:
    st.toast("⚠️ Tempo esgotado! Passando para a próxima...", icon="⏳")
    time.sleep(1) # Pequena pausa para o usuário perceber
    proxima_questao()

# 6. Interface
st.title("📚 Exame Integrado UEM 2025")

if not st.session_state.quiz_fim:
    # Barra Superior de Cronômetros
    cont_g, cont_q = st.columns(2)
    
    # Tempo Global
    restante_g = int(TEMPO_GLOBAL - decorrido_global)
    mins_g, segs_g = divmod(restante_g, 60)
    horas_g, mins_g = divmod(mins_g, 60)
    cont_g.metric("🕒 Tempo Total", f"{horas_g:02d}:{mins_g:02d}:{segs_g:02d}")
    
    # Tempo Questão
    restante_q = int(TEMPO_QUESTAO - decorrido_questao)
    cont_q.metric("⏱️ Tempo Questão", f"{restante_q}s", delta=f"-{int(decorrido_questao)}s", delta_color="inverse")

    st.divider()

    # Conteúdo da Questão
    q = st.session_state.perguntas[st.session_state.i]
    st.info(f"Questão {st.session_state.i + 1}/80")
    
    if q["img"]:
        st.warning(f"Figura: {q['img']} (Espaço para imagem)")

    st.write(f"**{q['p']}**")

    marcada = st.session_state.respostas.get(st.session_state.i, None)
    idx_radio = 0
    if marcada:
        for idx, opt in enumerate(q["opts"]):
            if opt.startswith(marcada): idx_radio = idx

    escolha = st.radio("Escolha uma opção:", q["opts"], index=idx_radio, key=f"rad_{st.session_state.i}")

    # Botões de Controle
    col_salvar, col_pular = st.columns([2, 1])
    with col_salvar:
        if st.button("💾 SALVAR E PRÓXIMA", use_container_width=True, type="primary"):
            st.session_state.respostas[st.session_state.i] = escolha[0]
            proxima_questao()
    with col_pular:
        if st.button("PULAR ➡️", use_container_width=True):
            proxima_questao()

    # Auto-refresh para o cronômetro (a cada 1 segundo)
    time.sleep(1)
    st.rerun()

else:
    # 7. Tela Final
    st.success("🏁 EXAME ENCERRADO")
    
    acertos = sum(1 for i, q in enumerate(st.session_state.perguntas) if st.session_state.respostas.get(i) == q["c"])
    nota = (acertos / 80) * 20
    
    res_c1, res_c2 = st.columns(2)
    res_c1.metric("Acertos", f"{acertos}/80")
    res_c2.metric("Nota Final", f"{nota:.2f}/20")

    if st.button("🔄 REINICIAR EXAME"):
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()

    # Detalhes da Correção
    with st.expander("Clique para ver a correção detalhada"):
        for i, q in enumerate(st.session_state.perguntas):
            resp = st.session_state.respostas.get(i, "Não respondida")
            cor = "green" if resp == q["c"] else "red"
            st.markdown(f"**Q{i+1}:** {q['p']}")
            st.markdown(f"Sua: :{cor}[{resp}] | Correta: **{q['c']}**")
            st.divider()
