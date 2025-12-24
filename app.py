import streamlit as st
import time
import streamlit.components.v1 as components

# 1. Configurações Iniciais
st.set_page_config(page_title="Exame Física UEM 2025", layout="centered")

# 2. Banco de Dados
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

# 3. Inicialização de Estados (Session State)
if "i" not in st.session_state: st.session_state.i = 0
if "respostas_usuario" not in st.session_state: st.session_state.respostas_usuario = {}
if "inicio_global" not in st.session_state: st.session_state.inicio_global = time.time()
if "inicio_questao" not in st.session_state: st.session_state.inicio_questao = time.time()
if "quiz_finalizado" not in st.session_state: st.session_state.quiz_finalizado = False
if "ver_correcao" not in st.session_state: st.session_state.ver_correcao = False

# 4. Funções de Controle com Limpeza Real
def reiniciar_totalmente():
    # Limpa absolutamente todas as variáveis de controle
    keys_to_reset = ["i", "respostas_usuario", "inicio_global", "inicio_questao", "quiz_finalizado", "ver_correcao", "tempo_total_texto"]
    for key in keys_to_reset:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

def finalizar():
    gasto = int(time.time() - st.session_state.inicio_global)
    st.session_state.tempo_total_texto = f"{gasto // 60}m {gasto % 60}s"
    st.session_state.quiz_finalizado = True

# 5. Interface Principal
st.title("📘 Quiz Física – UEM 2025")

if not st.session_state.quiz_finalizado:
    # Lógica de Tempos
    agora = time.time()
    total_restante = max(0, 5400 - int(agora - st.session_state.inicio_global))
    questao_restante = max(0, 60 - int(agora - st.session_state.inicio_questao))

    if total_restante <= 0: finalizar(); st.rerun()

    c1, c2 = st.columns(2)
    c1.metric("⏳ Tempo Exame", f"{total_restante // 60}m {total_restante % 60}s")
    c2.metric("⏱️ Tempo Questão", f"{questao_restante}s")

    if questao_restante <= 0:
        st.session_state.i += 1
        st.session_state.inicio_questao = time.time()
        if st.session_state.i >= len(st.session_state.perguntas): finalizar()
        st.rerun()

    st.divider()

    # Conteúdo da Questão
    idx = st.session_state.i
    q = st.session_state.perguntas[idx]
    
    st.write(f"### Questão {idx + 1} de {len(st.session_state.perguntas)}")
    st.info(q['pergunta'])

    # Recuperação de resposta
    marcada = st.session_state.respostas_usuario.get(idx, None)
    idx_radio = 0
    if marcada:
        for i_opt, t_opt in enumerate(q['opcoes']):
            if t_opt.startswith(marcada): idx_radio = i_opt

    escolha = st.radio("Selecione:", q['opcoes'], index=idx_radio, key=f"q_{idx}")

    # Botões de Navegação
    if st.button("✅ CONFIRMAR E AVANÇAR", use_container_width=True, type="primary"):
        st.session_state.respostas_usuario[idx] = escolha[0]
        if idx + 1 < len(st.session_state.perguntas):
            st.session_state.i += 1
            st.session_state.inicio_questao = time.time()
        else:
            finalizar()
        st.rerun()

    col_v, col_p = st.columns(2)
    with col_v:
        if st.button("⬅️ VOLTAR", use_container_width=True, disabled=(idx == 0)):
            st.session_state.i -= 1
            st.session_state.inicio_questao = time.time()
            st.rerun()
    with col_p:
        if st.button("PULAR ➡️", use_container_width=True):
            if idx + 1 < len(st.session_state.perguntas):
                st.session_state.i += 1
                st.session_state.inicio_questao = time.time()
            else:
                finalizar()
            st.rerun()

    time.sleep(1)
    st.rerun()

# --- TELA DE RESULTADOS ---
else:
    st.success("🏁 EXAME FINALIZADO!")
    
    acertos = sum(1 for i_q, quest in enumerate(st.session_state.perguntas) if st.session_state.respostas_usuario.get(i_q) == quest['correta'])

    # Área de Impressão / Print
    st.markdown("### 📊 Resultado Final")
    res1, res2 = st.columns(2)
    res1.metric("✅ Pontuação", f"{acertos} / {len(st.session_state.perguntas)}")
    res2.metric("⏱️ Tempo Gasto", st.session_state.get('tempo_total_texto', '--'))

    # BOTÃO DE CAPTURA (PRINT SCREEN)
    if st.button("📸 FAZER CAPTURA DE TELA", use_container_width=True, type="primary"):
        # Aciona o comando de impressão do sistema, que permite capturar a página toda ou salvar PDF
        components.html("<script>window.print();</script>", height=0)

    st.divider()

    # Bloco de Correção (Inicia Fechado)
    if not st.session_state.ver_correcao:
        if st.button("🔍 EXIBIR GABARITO E CORREÇÃO", use_container_width=True):
            st.session_state.ver_correcao = True
            st.rerun()
    else:
        st.markdown("### 📝 Correção Detalhada")
        for i_q, quest in enumerate(st.session_state.perguntas):
            resp = st.session_state.respostas_usuario.get(i_q, "PULADA")
            corr = quest['correta']
            st.write(f"**Q{i_q+1}:** {quest['pergunta']}")
            if resp == corr:
                st.write(f"Resposta: :green[{resp} (Correta)]")
            else:
                st.write(f"Resposta: :red[{resp}] | Correta: :green[{corr}]")
            st.write("---")
        
        if st.button("⬆️ ESCONDER GABARITO", use_container_width=True):
            st.session_state.ver_correcao = False
            st.rerun()

    # O BOTÃO REINICIAR CHAMA A FUNÇÃO DE LIMPEZA TOTAL
    if st.button("🔄 REINICIAR TESTE DO ZERO", use_container_width=True):
        reiniciar_totalmente()
