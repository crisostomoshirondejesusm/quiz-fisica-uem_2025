import streamlit as st
import time
import streamlit.components.v1 as components

# Configurações da Página
st.set_page_config(page_title="Exame Física UEM 2025", layout="centered")

# Função de Captura de Tela (Abre a interface de captura/impressão do sistema)
def screenshot_button():
    if st.button("📸 FAZER CAPTURA DE TELA (PRINT)", use_container_width=True, type="primary"):
        # JavaScript para abrir a ferramenta de captura/impressão do navegador
        components.html("<script>window.print();</script>", height=0)

# -------------------------------
# BANCO DE QUESTÕES
# -------------------------------
TEMPO_QUESTAO_MAX = 60
TEMPO_TOTAL_MAX = 90 * 60 

if "perguntas" not in st.session_state:
    st.session_state.perguntas = [
        {"pergunta": "40) Um recipiente com água é colocado sobre um fogão aceso. O aquecimento da água ocorre principalmente por:", "opcoes": ["A) Condução", "B) Irradiação", "C) Convecção", "D) Radiação", "E) Evaporação"], "correta": "C"},
        {"pergunta": "41) Quais grandezas permitem distinguir um tipo de onda de outro?", "opcoes": ["A) Intensidade, área e velocidade", "B) Amplitude, velocidade, frequência e comprimento de onda", "C) Polarização, massa e energia", "D) Altura, timbre e intensidade", "E) Sentido e direção apenas"], "correta": "B"},
        {"pergunta": "42) Um transmissor de rádio opera a 20 MHz. Qual é o comprimento de onda emitido?", "opcoes": ["A) 5 m", "B) 10 m", "C) 15 m", "D) 20 m", "E) 25 m"], "correta": "C"},
        {"pergunta": "43) Um corpo de 1 kg absorve 1250 cal ao ser aquecido de 30 °C a 80 °C. O calor específico é:", "opcoes": ["A) 0,025 cal/g°C", "B) 0,25 cal/g°C", "C) 1,25 cal/g°C", "D) 25 cal/g°C", "E) 150 cal/g°C"], "correta": "B"},
        {"pergunta": "44) Uma lâmpada incandescente (T = 3000 K) emite radiação máxima com comprimento de onda:", "opcoes": ["A) 96 nm", "B) 165 nm", "C) 350 nm", "D) 500 nm", "E) 966 nm"], "correta": "E"},
        {"pergunta": "45) Em um gráfico de emissividade, qual corpo é o menos quente?", "opcoes": ["A) X", "B) Y", "C) Z", "D) X e Y", "E) Y e Z"], "correta": "B"},
        {"pergunta": "46) Uma estrela tem área igual à do Sol e potência 2,43×10²⁴ W. Qual é a temperatura aproximada?", "opcoes": ["A) 19 000 K", "B) 24 000 K", "C) 28 000 K", "D) 30 000 K", "E) 34 000 K"], "correta": "A"},
        {"pergunta": "47) Qual é a energia de um fotão de frequência 7,5×10¹⁸ Hz?", "opcoes": ["A) 1,99×10⁻¹⁵ J", "B) 2,99×10⁻¹⁵ J", "C) 3,99×10⁻¹⁵ J", "D) 4,99×10⁻¹⁵ J", "E) 5,99×10⁻¹⁵ J"], "correta": "D"},
        {"pergunta": "48) A interação eletromagnética ocorre entre:", "opcoes": ["A) Protões e neutrões", "B) Protões e protões", "C) Eletrões e eletrões", "D) Fotões e fotões", "E) Eletrões e fotões"], "correta": "E"},
        {"pergunta": "49) Um fotão tem comprimento de onda 198,6 nm. Qual é a sua energia?", "opcoes": ["A) 1,0×10⁻¹⁸ J", "B) 2,0×10⁻¹⁸ J", "C) 3,0×10⁻¹⁸ J", "D) 4,0×10⁻¹⁸ J", "E) 5,0×10⁻¹⁸ J"], "correta": "B"},
        {"pergunta": "50) A radioatividade é consequência de:", "opcoes": ["A) Combustão química", "B) Alterações no núcleo dos átomos", "C) Escape de eletrões", "D) Ruptura de ligações químicas", "E) Variação de temperatura"], "correta": "B"}
    ]

# -------------------------------
# ESTADO DA SESSÃO
# -------------------------------
if "i" not in st.session_state:
    st.session_state.i = 0
    st.session_state.respostas_usuario = {}
    st.session_state.inicio_global = time.time()
    st.session_state.inicio_questao = time.time()
    st.session_state.quiz_finalizado = False
    st.session_state.ver_correcao = False 

# FUNÇÃO REINICIAR CORRIGIDA
def reiniciar_tudo():
    # Limpamos todas as chaves manualmente para garantir o reset total
    chaves_para_remover = ["i", "respostas_usuario", "inicio_global", "inicio_questao", "quiz_finalizado", "ver_correcao", "tempo_total_gasto"]
    for chave in chaves_para_remover:
        if chave in st.session_state:
            del st.session_state[chave]
    st.rerun()

def finalizar_exame():
    agora = time.time()
    gasto = int(agora - st.session_state.inicio_global)
    st.session_state.tempo_total_gasto = f"{gasto // 60}m {gasto % 60}s"
    st.session_state.quiz_finalizado = True

# -------------------------------
# EXECUÇÃO
# -------------------------------
st.title("📘 Quiz Física – UEM 2025")

if not st.session_state.quiz_finalizado:
    # Lógica de tempo e questões
    agora = time.time()
    tempo_decorrido = int(agora - st.session_state.inicio_global)
    tempo_restante_global = max(0, TEMPO_TOTAL_MAX - tempo_decorrido)
    tempo_restante_questao = max(0, TEMPO_QUESTAO_MAX - int(agora - st.session_state.inicio_questao))

    if tempo_restante_global <= 0:
        finalizar_exame()
        st.rerun()

    # Exibição de cabeçalho
    c1, c2 = st.columns(2)
    with c1: st.metric("⏳ Tempo Global", f"{tempo_restante_global // 60}m {tempo_restante_global % 60}s")
    with c2: st.metric("⏱️ Tempo Questão", f"{tempo_restante_questao}s")
    
    if tempo_restante_questao <= 0:
        st.session_state.i += 1
        st.session_state.inicio_questao = time.time()
        st.rerun()

    st.divider()

    # Pergunta
    q = st.session_state.perguntas[st.session_state.i]
    st.write(f"### Questão {st.session_state.i + 1} / {len(st.session_state.perguntas)}")
    st.markdown(f"#### {q['pergunta']}")

    # Resposta anterior
    idx_prev = 0
    if st.session_state.i in st.session_state.respostas_usuario:
        l = st.session_state.respostas_usuario[st.session_state.i]
        for idx, o in enumerate(q["opcoes"]):
            if o.startswith(l): idx_prev = idx

    resp = st.radio("Sua resposta:", q["opcoes"], index=idx_prev, key=f"rad_{st.session_state.i}")

    # Botões de navegação
    if st.button("✅ CONFIRMAR E AVANÇAR", use_container_width=True, type="primary"):
        st.session_state.respostas_usuario[st.session_state.i] = resp[0]
        if st.session_state.i + 1 < len(st.session_state.perguntas):
            st.session_state.i += 1
            st.session_state.inicio_questao = time.time()
        else:
            finalizar_exame()
        st.rerun()

    col_v, col_p = st.columns(2)
    with col_v:
        if st.button("⬅️ VOLTAR", use_container_width=True, disabled=(st.session_state.i == 0)):
            st.session_state.i -= 1
            st.session_state.inicio_questao = time.time()
            st.rerun()
    with col_p:
        if st.button("PULAR ➡️", use_container_width=True):
            if st.session_state.i + 1 < len(st.session_state.perguntas):
                st.session_state.i += 1
                st.session_state.inicio_questao = time.time()
            else:
                finalizar_exame()
            st.rerun()

    time.sleep(1)
    st.rerun()

# -------------------------------
# TELA FINAL
# -------------------------------
else:
    st.success("🏁 EXAME FINALIZADO!")
    
    # Contagem de pontos
    acertos = sum(1 for idx, q in enumerate(st.session_state.perguntas) if st.session_state.respostas_usuario.get(idx) == q["correta"])
    
    st.markdown("### 📊 Resultado para Captura")
    c1, c2 = st.columns(2)
    with c1: st.metric("✅ Pontos", f"{acertos} / {len(st.session_state.perguntas)}")
    with c2: st.metric("⏱️ Tempo Gasto", st.session_state.get("tempo_total_gasto", "--"))
    
    # Botão de captura
    screenshot_button()
    st.divider()

    # Gabarito
    if not st.session_state.ver_correcao:
        if st.button("🔍 VER GABARITO E CORREÇÃO", use_container_width=True):
            st.session_state.ver_correcao = True
            st.rerun()
    else:
        for idx, q in enumerate(st.session_state.perguntas):
            r = st.session_state.respostas_usuario.get(idx, "N/A")
            cor = "✅" if r == q["correta"] else "❌"
            with st.expander(f"Questão {idx + 1}: {cor}"):
                st.write(f"Sua resposta: {r} | Correta: {q['correta']}")
        
        if st.button("⬆️ OCULTAR GABARITO", use_container_width=True):
            st.session_state.ver_correcao = False
            st.rerun()

    # Botão reiniciar (Garante o fechamento de tudo)
    if st.button("🔄 REINICIAR TESTE", use_container_width=True):
        reiniciar_tudo()
