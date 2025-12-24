import streamlit as st
import time
import streamlit.components.v1 as components

# Configurações iniciais
st.set_page_config(page_title="Exame Física UEM 2025", layout="centered")

# Script para Captura de Tela (Abre a função de impressão do navegador)
def screenshot_button():
    js = """
    <script>
    function doPrint() {
        window.print();
    }
    </script>
    """
    components.html(js, height=0)
    if st.button("📸 Capturar Tela / Salvar PDF", use_container_width=True):
        components.html("<script>window.print();</script>", height=0)

# -------------------------------
# CONFIGURAÇÕES DE TEMPO
# -------------------------------
TEMPO_QUESTAO = 60
TEMPO_TOTAL_EXAME = 90 * 60 

# -------------------------------
# BANCO DE QUESTÕES
# -------------------------------
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
# SESSÃO
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

# Cronômetros
agora = time.time()
tempo_restante_global = max(0, TEMPO_TOTAL_EXAME - int(agora - st.session_state.inicio_global))
tempo_restante_questao = max(0, TEMPO_QUESTAO - int(agora - st.session_state.inicio_questao))

if tempo_restante_global <= 0:
    st.session_state.quiz_finalizado = True

# -------------------------------
# INTERFACE
# -------------------------------
st.title("📘 Quiz Física – UEM 2025")

if not st.session_state.quiz_finalizado and st.session_state.i < len(st.session_state.perguntas):
    
    col_t1, col_t2 = st.columns(2)
    with col_t1: st.metric("⏳ Tempo Total", f"{tempo_restante_global // 60}m {tempo_restante_global % 60}s")
    with col_t2: st.metric("⏱️ Tempo da Questão", f"{tempo_restante_questao}s")
    
    st.progress(min((time.time() - st.session_state.inicio_global) / TEMPO_TOTAL_EXAME, 1.0))

    if tempo_restante_questao <= 0:
        st.session_state.i += 1
        st.session_state.inicio_questao = time.time()
        st.rerun()

    st.divider()

    total_q = len(st.session_state.perguntas)
    q_atual = st.session_state.perguntas[st.session_state.i]
    
    st.write(f"### Questão {st.session_state.i + 1} / {total_q}")
    st.markdown(f"**{q_atual['pergunta']}**")
    
    index_salvo = 0
    if st.session_state.i in st.session_state.respostas_usuario:
        letra = st.session_state.respostas_usuario[st.session_state.i]
        for idx, opt in enumerate(q_atual["opcoes"]):
            if opt.startswith(letra): index_salvo = idx

    resposta = st.radio("Escolha uma opção:", q_atual["opcoes"], index=index_salvo, key=f"radio_{st.session_state.i}")

    if st.button("✅ RESPONDER E AVANÇAR", use_container_width=True, type="primary"):
        st.session_state.respostas_usuario[st.session_state.i] = resposta[0]
        st.session_state.i += 1
        st.session_state.inicio_questao = time.time()
        st.rerun()

    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("⬅️ VOLTAR ANTERIOR", use_container_width=True, disabled=(st.session_state.i == 0)):
            st.session_state.i -= 1
            st.session_state.inicio_questao = time.time()
            st.rerun()
    with col_btn2:
        if st.button("PULAR QUESTÃO ➡️", use_container_width=True):
            st.session_state.i += 1
            st.session_state.inicio_questao = time.time()
            st.rerun()

    time.sleep(1)
    st.rerun()

# -------------------------------
# TELA FINAL
# -------------------------------
else:
    st.success("🏁 EXAME FINALIZADO!")
    
    acertos = 0
    for idx, q in enumerate(st.session_state.perguntas):
        if st.session_state.respostas_usuario.get(idx) == q["correta"]:
            acertos += 1
            
    st.metric("Resultado Final", f"{acertos} de {len(st.session_state.perguntas)} Acertos")
    
    # BOTÃO DE CAPTURA DE TELA
    screenshot_button()
    
    if st.button("Reiniciar Novo Teste", use_container_width=True):
        reiniciar()
