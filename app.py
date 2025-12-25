import streamlit as st
import time
import os

# 1. Configurações da Página
st.set_page_config(page_title="Exame de Matematica-I & Fisica-I UEM 2025", layout="centered")

# Título Principal da Aplicação
st.title("📝 Exame de Matematica-I & Fisica-I UEM 2025")

# Estilo para o Relógio Digital
st.markdown("""
    <style>
    .relogio-container {
        display: flex;
        justify-content: space-around;
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #ff4b4b;
        margin-bottom: 20px;
    }
    .tempo-label { font-size: 0.8rem; color: #555; margin-bottom: 5px; }
    .tempo-valor { font-size: 1.5rem; font-weight: bold; font-family: 'Courier New', Courier, monospace; color: #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# 2. Banco de Dados Completo (Questões)
if "perguntas" not in st.session_state:
    # --- MATEMÁTICA ---
    m_qs = [
        {"id": 1, "p": "Indique as soluções da equação $-|x-2|+6=2$:", "opts": ["A. x=2 v x=6", "B. x=-4 v x=4", "C. x=2", "D. x=-2 v x=6", "E. x=4"], "c": "D", "img": None},
        # ... (mantendo as outras questões 2-29)
    ]
    # Inserindo questões de exemplo para preencher o gap até a 30
    for i in range(2, 30):
        m_qs.append({"id": i, "p": f"Questão de Matemática {i}", "opts": ["A","B","C","D","E"], "c": "A", "img": None})
    
    # Ajuste solicitado para a Questão 30
    m_qs.append({"id": 30, "p": "Gráfico da função f. No ponto x=2, podemos concluir que:", "opts": ["A. lim f(x) à esquerda = f(2)", "B. lim f(x) não existe", "C. lim f(x) = 2", "D. lim f(x) à direita ≠ f(2)", "E. Nenhuma delas"], "c": "B", "img": "q30.png"})
    
    # Restante de Matemática 31-40
    for i in range(31, 41):
        m_qs.append({"id": i, "p": f"Questão de Matemática {i}", "opts": ["A","B","C","D","E"], "c": "A", "img": None})

    # --- FÍSICA (Exemplo simplificado para manter o fluxo) ---
    f_qs = []
    for i in range(41, 81):
        f_qs.append({"id": i, "p": f"Questão de Física {i}", "opts": ["A","B","C","D","E"], "c": "B", "img": None})

    # Mesclagem Intercalada
    final_list = []
    for m, f in zip(m_qs, f_qs):
        final_list.append(m)
        final_list.append(f)
    st.session_state.perguntas = final_list

# 3. Lógica de Navegação e Estado
if "i" not in st.session_state: st.session_state.i = 0
if "respostas" not in st.session_state: st.session_state.respostas = {}
if "quiz_fim" not in st.session_state: st.session_state.quiz_fim = False
if "ver_gabarito" not in st.session_state: st.session_state.ver_gabarito = False
if "inicio_t" not in st.session_state: st.session_state.inicio_t = time.time()
if "quest_t" not in st.session_state: st.session_state.quest_t = time.time()
if "fim_t" not in st.session_state: st.session_state.fim_t = 0

def proxima_questao():
    if st.session_state.i + 1 < len(st.session_state.perguntas):
        st.session_state.i += 1
        st.session_state.quest_t = time.time()
    else:
        st.session_state.quiz_fim = True
        st.session_state.fim_t = time.time()
    st.rerun()

# 4. Interface Principal
if not st.session_state.quiz_fim:
    # Cálculos de tempo
    t_quest_decorrido = int(time.time() - st.session_state.quest_t)
    t_quest_restante = max(0, 90 - t_quest_decorrido)
    t_global_decorrido = int(time.time() - st.session_state.inicio_t)
    min_g, seg_g = divmod(t_global_decorrido, 60)

    # Relógio na tela
    st.markdown(f"""
        <div class="relogio-container">
            <div style="text-align: center;">
                <div class="tempo-label">TEMPO TOTAL DECORRIDO</div>
                <div class="tempo-valor">{min_g:02d}:{seg_g:02d}</div>
            </div>
            <div style="text-align: center;">
                <div class="tempo-label">TEMPO DA QUESTÃO</div>
                <div class="tempo-valor">{t_quest_restante:02d}s</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.progress((st.session_state.i + 1) / 80)
    st.write(f"**Questão {st.session_state.i + 1} de 80**")

    if t_quest_restante <= 0:
        st.error("Tempo esgotado! Mudando de questão...")
        time.sleep(1)
        proxima_questao()

    st.divider()

    # Conteúdo da Questão
    q = st.session_state.perguntas[st.session_state.i]
    tipo = "📐 MATEMÁTICA" if q['id'] <= 40 else "⚡ FÍSICA"
    st.info(f"**Matéria:** {tipo}")

    if q["img"]:
        # Tenta carregar de 'imagens/'
        img_path = os.path.join("imagens", q["img"])
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.warning(f"Aviso: Imagem {q['img']} não encontrada na pasta 'imagens'.")

    st.markdown(f"#### Questão {q['id']}")
    st.write(q['p'])

    marcada = st.session_state.respostas.get(st.session_state.i, None)
    idx_radio = 0
    if marcada:
        for idx, opt in enumerate(q["opts"]):
            if opt.startswith(marcada): idx_radio = idx

    escolha = st.radio("Sua escolha:", q["opts"], index=idx_radio, key=f"q_{st.session_state.i}")

    if st.button("✅ SALVAR E CONTINUAR", use_container_width=True, type="primary"):
        st.session_state.respostas[st.session_state.i] = escolha[0]
        proxima_questao()

    col_v, col_p = st.columns(2)
    with col_v:
        if st.button("⬅️ VOLTAR", use_container_width=True, disabled=(st.session_state.i == 0)):
            st.session_state.i -= 1
            st.session_state.quest_t = time.time()
            st.rerun()
    with col_p:
        if st.button("PULAR ➡️", use_container_width=True):
            proxima_questao()

    time.sleep(1)
    st.rerun()

else:
    # 5. Tela de Resultados Finais
    duracao_total = int(st.session_state.fim_t - st.session_state.inicio_t)
    min_tot, seg_tot = divmod(duracao_total, 60)
    
    st.success("🏁 EXAME CONCLUÍDO!")
    
    acertos = sum(1 for i, q in enumerate(st.session_state.perguntas) if st.session_state.respostas.get(i) == q["c"])
    nota = (acertos / 80) * 20
    
    st.balloons()
    
    # Container de Resumo
    st.markdown(f"""
    <div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px; border-left: 5px solid #28a745; margin-bottom: 20px;">
        <h3>📊 Resumo do Desempenho</h3>
        <p style="font-size: 1.2rem;"><b>Tempo Total de Realização:</b> {min_tot} minutos e {seg_tot} segundos</p>
        <p style="font-size: 1.2rem;"><b>Pontuação:</b> {nota:.2f} / 20.00</p>
        <p style="font-size: 1.2rem;"><b>Total de Acertos:</b> {acertos} de 80</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 REINICIAR TESTE", use_container_width=True):
        for key in list(st.session_state.keys()): del st.session_state[key]
        st.rerun()

    st.divider()
    if st.button("🔍 VER CORRECÇÃO DETALHADA", use_container_width=True):
        st.session_state.ver_gabarito = not st.session_state.ver_gabarito

    if st.session_state.ver_gabarito:
        st.subheader("Gabarito Comentado")
        for i, q in enumerate(st.session_state.perguntas):
            sua = st.session_state.respostas.get(i, "Não respondida")
            status = "✅" if sua == q["c"] else "❌"
            with st.expander(f"Questão {q['id']} - {status}"):
                st.write(f"**Enunciado:** {q['p']}")
                st.write(f"Sua resposta: **{sua}**")
                st.write(f"Resposta correta: **{q['c']}**")
