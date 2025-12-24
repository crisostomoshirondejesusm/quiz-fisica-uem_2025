import streamlit as st
import time
import streamlit.components.v1 as components

# 1. Configurações da Página
st.set_page_config(page_title="Exame Física UEM 2025", layout="centered")

# 2. Banco de Dados Completo (Extraído do PDF)
QUESTOES_PDF = [
    {"id": 41, "p": "Um recipiente de vidro está quase cheio com água... Isso ocorre devido à propagação de calor por:", "opts": ["A. Condução", "B. irradiação", "C. convecção", "D. condução e convecção", "E. convecção e irradiação"], "c": "C"},
    {"id": 42, "p": "Quais são as características capazes de distinguir um tipo de onda electromagnética de outro?", "opts": ["A. intensidade, velocidade, área, comprimento", "B. amplitude, velocidade da propagação, frequência, comprimento de onda", "C. amplitude, polarização, frequência, direcção da propagação", "D. altura, intensidade, timbre, velocidade", "E. amplitude, perturbação, propagação, sentido"], "c": "B"},
    {"id": 43, "p": "Um transmissor de rádio... opera a uma frequência de 20 MHz. Qual é o comprimento de onda?", "opts": ["A. 15 m", "B. 25 m", "C. 35 m", "D. 45 m", "E. 55 m"], "c": "A"},
    {"id": 44, "p": "Um corpo de massa 100 g recebeu 1250 cal ao ser aquecido de 30°C a 80°C. Determine o calor específico.", "opts": ["A. 0.025 cal/g.°C", "B. 2.50 cal/g.°C", "C. 2,5 cal/g.°C", "D. 25 cal/g.°C", "E. 0,25 cal/g.°C"], "c": "E"},
    {"id": 45, "p": "Lâmpada incandescente (T=3000K). Determine o comprimento de onda de emissão máxima (nm). (b=2,9x10^-3 mK)", "opts": ["A. 966", "B. 765", "C. 438", "D. 350", "E. 320"], "c": "A"},
    {"id": 46, "p": "Gráfico de emissividade: Qual dos corpos é menos quente?", "opts": ["A. Ty=Tx", "B. Ty", "C. Tz", "D. Tz=Ty", "E. Tx"], "c": "B"},
    {"id": 47, "p": "Estrela (Área=1/10*10^15 m², Potência=24,3x10^23 W). Qual a temperatura (K)?", "opts": ["A. 19000", "B. 24000", "C. 28000", "D. 30000", "E. 34000"], "c": "A"},
    {"id": 48, "p": "Determine a energia de fotões de raios X com comprimento de onda = 1,0x10^-10 m.", "opts": ["A. 5,99x10^-15J", "B. 4,99x10^-15J", "C. 3,99x10^-15J", "D. 2,99x10^-15J", "E. 1,99x10^-15J"], "c": "E"},
    {"id": 49, "p": "Variação de energia de um átomo ao absorver quantum com comprimento de onda de 198,6 nm.", "opts": ["A. 0.25x10^-18J", "B. 0.5x10^-18J", "C. 1x10^-18J", "D. 2x10^-18J", "E. 3x10^-18J"], "c": "C"},
    {"id": 50, "p": "O efeito fotoeléctrico ocorre devido à interação entre:", "opts": ["A. protões e electrões", "B. fotões e electrões", "C. electrões e electrões", "D. fotões e fotões", "E. protões e fotões"], "c": "B"},
    {"id": 51, "p": "Quantos fotões entram no olho humano por segundo (P=2x10^-17 W, compr.=0,5 micróm.)?", "opts": ["A. 50", "B. 70", "C. 100", "D. 120", "E. 140"], "c": "A"},
    {"id": 52, "p": "Número de fotões que um átomo de H pode emitir com electrão na 3ª órbita?", "opts": ["A. 1", "B. 2", "C. 3", "D. 4", "E. 5"], "c": "C"},
    {"id": 53, "p": "Energia cinética de electrões acelerados por 5000 V (carga 1,6x10^-19 C)?", "opts": ["A. 2,0x10^-16J", "B. 4,0x10^-16J", "C. 6,0x10^-16J", "D. 8,0x10^-16J", "E. 10,0x10^-16J"], "c": "D"},
    {"id": 54, "p": "Tensão (kV) no ânodo de tubo de raios X para frequência máxima de 3x10^19 Hz?", "opts": ["A. 124", "B. 130", "C. 132", "D. 140", "E. 142"], "c": "A"},
    {"id": 55, "p": "Qual transição é responsável pela emissão de fotões com o maior momento linear?", "opts": ["A. 1", "B. 2", "C. 3", "D. 4", "E. 5"], "c": "A"},
    {"id": 56, "p": "A radioactividade emitida por amostras de substâncias provém de:", "opts": ["A. energia térmica", "B. alterações em núcleos de átomos", "C. escape de electrões", "D. rupturas de ligações", "E. reorganização de átomos"], "c": "B"},
    {"id": 57, "p": "Sobre partículas alfa e beta, é correto afirmar que:", "opts": ["A. beta são 2p+2n", "B. alfa são 2p+2e", "C. alfa são 2e+2p+2n", "D. alfa são apenas 2p", "E. beta são electrões emitidos pelo núcleo"], "c": "E"},
    {"id": 58, "p": "Quantos neutrões tem um núcleo do isótopo de 208/83 Bi?", "opts": ["A. 83", "B. 125", "C. 208", "D. 291", "E. 308"], "c": "B"},
    {"id": 59, "p": "A incógnita X na reacção (Al + gama -> Mg + X) representa o núcleo de:", "opts": ["A. alumínio", "B. oxigénio", "C. carbono", "D. hidrogénio", "E. hélio"], "c": "D"},
    {"id": 60, "p": "Qual é o tipo de radiação que atinge o detector no ponto 3 (Bloco de Chumbo)?", "opts": ["A. Infravermelha", "B. Ultravioleta", "C. alfa", "D. beta", "E. gama"], "c": "D"},
    # ... Adicione as demais questões seguindo este padrão até a 80
]

# 3. Funções de Controle
def reset_total():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# Inicialização Forçada
if "perguntas" not in st.session_state or len(st.session_state.perguntas) < 20:
    st.session_state.perguntas = QUESTOES_PDF
    st.session_state.i = 0
    st.session_state.respostas_usuario = {}
    st.session_state.inicio_global = time.time()
    st.session_state.quiz_finalizado = False
    st.session_state.ver_correcao = False

# 4. Interface Principal
st.title("📘 Exame de Física I - UEM 2025")

if not st.session_state.quiz_finalizado:
    # Cronômetro (90 min) 
    agora = time.time()
    total_seg = 5400 - int(agora - st.session_state.inicio_global)
    
    if total_seg <= 0:
        st.session_state.quiz_finalizado = True
        st.rerun()

    st.metric("⏳ Tempo Restante", f"{total_seg // 60}m {total_seg % 60}s")
    
    # Questão Atual
    idx = st.session_state.i
    q = st.session_state.perguntas[idx]
    
    st.subheader(f"Questão {idx + 1} de {len(st.session_state.perguntas)}")
    st.info(q['p'])

    # Radio Button
    escolha = st.radio("Alternativas:", q['opts'], key=f"q{idx}")

    # Navegação
    if st.button("✅ CONFIRMAR E AVANÇAR", use_container_width=True, type="primary"):
        st.session_state.respostas_usuario[idx] = escolha[0]
        if idx + 1 < len(st.session_state.perguntas):
            st.session_state.i += 1
        else:
            st.session_state.quiz_finalizado = True
        st.rerun()
    
    time.sleep(1)
    st.rerun()

# 5. Tela de Resultados
else:
    st.success("🏁 EXAME FINALIZADO!")
    
    acertos = sum(1 for i, q in enumerate(st.session_state.perguntas) if st.session_state.respostas_usuario.get(i) == q['c'])
    
    st.markdown("### 📊 Seu Desempenho")
    c1, c2 = st.columns(2)
    c1.metric("Acertos", f"{acertos} / {len(st.session_state.perguntas)}")
    c2.metric("Nota", f"{(acertos/len(st.session_state.perguntas))*100:.1f}%")

    # BOTÃO DE CAPTURA (PRINT)
    if st.button("📸 FAZER CAPTURA DE TELA (PRINT)", use_container_width=True, type="primary"):
        components.html("<script>window.print();</script>", height=0)

    st.divider()

    # GABARITO (Inicia Fechado)
    if not st.session_state.ver_correcao:
        if st.button("🔍 VER GABARITO", use_container_width=True):
            st.session_state.ver_correcao = True
            st.rerun()
    else:
        for i, q in enumerate(st.session_state.perguntas):
            resp = st.session_state.respostas_usuario.get(i, "N/A")
            cor = "✅" if resp == q['c'] else "❌"
            st.write(f"**Q{i+1}:** {cor} (Sua: {resp} | Correta: {q['c']})")
        
        if st.button("⬆️ ESCONDER GABARITO", use_container_width=True):
            st.session_state.ver_correcao = False
            st.rerun()

    # REINICIAR (Fecha tudo)
    if st.button("🔄 REINICIAR DO ZERO", use_container_width=True):
        reset_total()
