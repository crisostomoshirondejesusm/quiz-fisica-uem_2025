import streamlit as st
import time

# Configurações iniciais
st.set_page_config(page_title="Exame Física UEM 2025", layout="centered")

# -------------------------------
# CONFIGURAÇÕES DE TEMPO
# -------------------------------
TEMPO_QUESTAO = 120  # Aumentado para 2 minutos devido à complexidade dos cálculos
TEMPO_TOTAL_EXAME = 90 * 60  # 90 minutos conforme instrução do PDF [cite: 3]

# -------------------------------
# BANCO DE QUESTÕES COMPLETO (41 a 80)
# -------------------------------
if "perguntas" not in st.session_state:
    st.session_state.perguntas = [
        {"id": 41, "pergunta": "Um recipiente de vidro está quase cheio com água em temperatura ambiente. Ao colocá-lo sobre uma chama de fogão, a água em seu interior começa a se aquecer. Isso ocorre devido à propagação de calor por:", "opcoes": ["A. Condução", "B. irradiação", "C. convecção", "D. condução e convecção", "E. convecção e irradiação"], "correta": "C", "imagem": None},
        {"id": 42, "pergunta": "Quais são as características capazes de distinguir um tipo de onda electromagnética de outro?", "opcoes": ["A. intensidade, velocidade, área, comprimento", "B. amplitude, velocidade da propagação, frequência, comprimento de onda", "C. amplitude, polarização, frequência, direcção da propagação", "D. altura, intensidade, timbre, velocidade", "E. amplitude, perturbação, propagação, sentido"], "correta": "B", "imagem": None},
        {"id": 43, "pergunta": "Um transmissor de rádio de satélite artificial da Terra opera a uma frequência de 20 MHz. Qual é o comprimento de onda do transmissor?", "opcoes": ["A. 15 m", "B. 25 m", "C. 35 m", "D. 45 m", "E. 55 m"], "correta": "A", "imagem": None},
        {"id": 44, "pergunta": "Um corpo de massa 100 g recebeu 1250 cal ao ser aquecido de 30°C a 80°C. Determine o seu calor específico.", "opcoes": ["A. 0.025 cal/g.°C", "B. 2.50 cal/g.°C", "C. 2,5 cal/g.°C", "D. 25 cal/g.°C", "E. 0,25 cal/g.°C"], "correta": "E", "imagem": None},
        {"id": 45, "pergunta": "Uma lâmpada incandescente (corpo negro) tem temperatura de filamento T=3000K. Determine o comprimento de onda de emissão máxima (nm). Considere b=2,9x10^-3 mK", "opcoes": ["A. 966", "B. 765", "C. 438", "D. 350", "E. 320"], "correta": "A", "imagem": None},
        {"id": 46, "pergunta": "O gráfico representa a emissividade de corpos X, Y e Z. Qual dos corpos é menos quente?", "opcoes": ["A. Ty=Tx", "B. Ty", "C. Tz", "D. Tz=Ty", "E. Tx"], "correta": "B", "imagem": "grafico_emissividade.png"}, # 
        {"id": 47, "pergunta": "Uma estrela tem área superficial de 1/10 * 10^15 m² e potência de 24,3x10^23 W. Qual a temperatura (K)? (sigma=5,67x10^-8)", "opcoes": ["A. 19000", "B. 24000", "C. 28000", "D. 30000", "E. 34000"], "correta": "A", "imagem": None},
        {"id": 48, "pergunta": "Determine a energia de fotões de raios X com comprimento de onda = 1,0x10^-10 m.", "opcoes": ["A. 5,99x10^-15J", "B. 4,99x10^-15J", "C. 3,99x10^-15J", "D. 2,99x10^-15J", "E. 1,99x10^-15J"], "correta": "E", "imagem": None},
        {"id": 49, "pergunta": "Determine a variação de energia de um átomo ao absorver um quantum com comprimento de onda de 198,6 nm.", "opcoes": ["A. 0.25x10^-18J", "B. 0.5x10^-18J", "C. 1x10^-18J", "D. 2x10^-18J", "E. 3x10^-18J"], "correta": "C", "imagem": None},
        {"id": 50, "pergunta": "O efeito fotoeléctrico ocorre devido à interação entre:", "opcoes": ["A. protões e electrões", "B. fotões e electrões", "C. electrões e electrões", "D. fotões e fotões", "E. protões e fotões"], "correta": "B", "imagem": None},
        {"id": 51, "pergunta": "Quantos fotões entram no olho por segundo (comprimento 0,5 micróm., potência 2x10^-17 W)?", "opcoes": ["A. 50", "B. 70", "C. 100", "D. 120", "E. 140"], "correta": "A", "imagem": None},
        {"id": 52, "pergunta": "Número de fotões de diferentes energias que um átomo de hidrogênio emite com electrão na 3ª órbita?", "opcoes": ["A. 1", "B. 2", "C. 3", "D. 4", "E. 5"], "correta": "C", "imagem": None},
        {"id": 53, "pergunta": "Energia cinética adquirida por electrões acelerados por 5000 V (carga 1,6x10^-19 C)?", "opcoes": ["A. 2,0x10^-16J", "B. 4,0x10^-16J", "C. 6,0x10^-16J", "D. 8,0x10^-16J", "E. 10,0x10^-16J"], "correta": "D", "imagem": None},
        {"id": 54, "pergunta": "Tensão (kV) no ânodo de tubo de raios X para frequência máxima de 3x10^19 Hz?", "opcoes": ["A. 124", "B. 130", "C. 132", "D. 140", "E. 142"], "correta": "A", "imagem": None},
        {"id": 55, "pergunta": "Qual transição no diagrama de níveis de energia do Hidrogênio emite fotão com maior momento linear?", "opcoes": ["A. 1", "B. 2", "C. 3", "D. 4", "E. 5"], "correta": "A", "imagem": "niveis_energia.png"}, # 
        {"id": 56, "pergunta": "A radioactividade emitida por substâncias provém de:", "opcoes": ["A. energia térmica", "B. alterações em núcleos de átomos", "C. escape de electrões", "D. rupturas de ligações químicas", "E. reorganização de átomos"], "correta": "B", "imagem": None},
        {"id": 57, "pergunta": "Sobre partículas alfa e beta, é correcto afirmar:", "opcoes": ["A. beta são 2p+2n", "B. alfa são 2p+2e", "C. beta são 2e+2p+2n", "D. alfa são apenas 2p", "E. beta são electrões emitidos pelo núcleo instável"], "correta": "E", "imagem": None},
        {"id": 58, "pergunta": "Quantos neutrões tem o núcleo de 208/83 Bi?", "opcoes": ["A. 83", "B. 125", "C. 208", "D. 291", "E. 308"], "correta": "B", "imagem": None},
        {"id": 59, "pergunta": "A incógnita X na reacção 27/13Al + gama -> 26/12Mg + X representa:", "opcoes": ["A. núcleo de alumínio", "B. núcleo de oxigénio", "C. núcleo de carbono", "D. núcleo de hidrogénio", "E. núcleo de hélio"], "correta": "D", "imagem": None},
        {"id": 60, "pergunta": "Qual radiação atinge o detector no ponto 3 no experimento do Bloco de Chumbo?", "opcoes": ["A. Infravermelha", "B. Ultravioleta", "C. alfa", "D. beta", "E. gama"], "correta": "D", "imagem": "experimento_chumbo.png"}, # [cite: 102]
        {"id": 61, "pergunta": "Qual das reacções representa produção de lixo radioactivo (fissão)?", "opcoes": ["A. N14+H1", "B. H2+H3", "C. C14 decay", "D. U235+n -> Sr95+Xe139", "E. U235 alfa decay"], "correta": "D", "imagem": None},
        {"id": 62, "pergunta": "Passe para a pergunta seguinte (Questão anulada/instrução do PDF)", "opcoes": ["A", "B", "C", "D", "E"], "correta": "A", "imagem": None},
        {"id": 63, "pergunta": "Energia liberada (MeV) em fusão com defeito de massa de 0,02 uma? (1 uma = 931 MeV)", "opcoes": ["A. 14,6", "B. 15,6", "C. 16,6", "D. 17,6", "E. 18.6"], "correta": "E", "imagem": None},
        {"id": 64, "pergunta": "Números atómico e de massa de T na reacção: n + U235 -> Cs144 + T + 2n?", "opcoes": ["A. 27 e 91", "B. 37 e 90", "C. 39 e 92", "D. 43 e 93", "E. 43 e 94"], "correta": "B", "imagem": None},
        {"id": 65, "pergunta": "Tempo para iodo-131 (meia-vida 8 dias) se desintegrar até 1/16 da massa inicial?", "opcoes": ["A. 8 dias", "B. 16 dias", "C. 24 dias", "D. 32 dias", "E. 128 dias"], "correta": "D", "imagem": None},
        {"id": 66, "pergunta": "Relação entre as vazões Q nas secções (1), (2) e (3) de uma tubulação horizontal afunilada?", "opcoes": ["A. Q1<Q2<Q3", "B. Q1>Q2>Q3", "C. Q1=Q2=Q3", "D. Q2>Q1>Q3", "E. Q1=Q2>Q3"], "correta": "C", "imagem": "tubulacao_afunilada.png"}, # [cite: 234]
        {"id": 67, "pergunta": "Velocidade do gás na saída sabendo P1=8atm, v1=10m/s e P2=1atm?", "opcoes": ["A. 52 m/s", "B. 50 m/s", "C. 49 m/s", "D. 51 m/s", "E. 54 m/s"], "correta": "B", "imagem": None},
        {"id": 68, "pergunta": "Velocidade v2 e pressão em tubulação com v1=3m/s, r1=0,1m e r2=0,05m?", "opcoes": ["A. 12 m/s e 67500Pa", "B. 13 m/s e 70000 Pa", "C. 15 m/s e 75000 Pa", "D. 16 m/s e 78000Pa", "E. 18 m/s e 78500Pa"], "correta": "A", "imagem": None},
        {"id": 69, "pergunta": "Vazão (dm³/s) de torneira que enche 12000L em 40 minutos?", "opcoes": ["A. 25", "B. 20", "C. 15", "D. 10", "E. 5"], "correta": "E", "imagem": None},
        {"id": 70, "pergunta": "Força aplicada (N) em prensa hidráulica para levantar carro de 1000kg (áreas 4m² e 0,0025m²)?", "opcoes": ["A. 5,25 N", "B. 6,25", "C. 7,25 N", "D. 8,27 N", "E. 9,25 N"], "correta": "B", "imagem": None},
        {"id": 71, "pergunta": "Velocidade (m/s) para encher piscina (18x10x2m) em 10h com conduto de 25cm²?", "opcoes": ["A. 10", "B. 8", "C. 6", "D. 4", "E. 2"], "correta": "D", "imagem": None},
        {"id": 72, "pergunta": "Número de moléculas em recipiente cúbico (0,5m), P=59760Pa, T=300K, R=8,3?", "opcoes": ["A. 3", "B. 5", "C. 7", "D. 9", "E. 11"], "correta": "B", "imagem": None},
        {"id": 73, "pergunta": "Denominações das etapas (1->2->3 e 3->1) no gráfico V(L) vs T(K)?", "opcoes": ["A. Isobárica, Adiabática", "B. Isovolumétrica, Isobárica e Isotérmica", "C. Isovolumétrica, Isotérmica e Isobárica", "D. Isotérmica, Isobárica e Isovolumétrica", "E. Isovolumétrica, Isobárica e Adiabática"], "correta": "B", "imagem": "grafico_ciclo.png"}, # [cite: 291]
        {"id": 74, "pergunta": "Volume (L) de hidrogênio a 293K (inicial 0,15L a 300K, P constante)?", "opcoes": ["A. 0,38 L", "B. 0,31 L", "C. 0,28 L", "D. 0,21 L", "E. 0,15 L"], "correta": "E", "imagem": None},
        {"id": 75, "pergunta": "Qual representação de gases ideais é FALSA?", "opcoes": ["A", "B", "C", "D", "E"], "correta": "E", "imagem": "graficos_gases.png"}, # [cite: 313]
        {"id": 76, "pergunta": "Variação de energia interna (J) após 2 etapas: (Q1=500, W1=200) e (Q2=-300, W2=-100)?", "opcoes": ["A. 150", "B. 100", "C. 75", "D. 50", "E. 35"], "correta": "B", "imagem": None},
        {"id": 77, "pergunta": "Trabalho realizado por gás em expansão adiabática que recebe 10 kJ?", "opcoes": ["A. 40", "B. 30", "C. 20", "D. 10", "E. 0"], "correta": "D", "imagem": None},
        {"id": 78, "pergunta": "Trabalho total (J) no ciclo XY-YZ-ZX do gráfico p(Pa) vs V(m³)?", "opcoes": ["A. 0", "B. 4,8x10^5", "C. 3,2x10^5", "D. 2,0x10^5", "E. 1,6x10^5"], "correta": "E", "imagem": "grafico_trabalho.png"}, # [cite: 347]
        {"id": 79, "pergunta": "Período e amplitude (SI) de massa 0,2kg, k=0,8pi² N/m, afastada 3cm?", "opcoes": ["A. 0,03 e 1", "B. 2 e 0,03", "C. 0,03 e 1,6", "D. 1 e 0,03", "E. 1,6 e 0,03"], "correta": "D", "imagem": None},
        {"id": 80, "pergunta": "Valor da amplitude de aceleração do corpo no gráfico MHS?", "opcoes": ["A. pi", "B. 2pi", "C. 4pi²", "D. 4pi", "E. 2pi²"], "correta": "E", "imagem": "grafico_mhs.png"}, # [cite: 375]
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

if tempo_restante_global <= 0:
    st.session_state.quiz_finalizado = True

# -------------------------------
# INTERFACE DO QUIZ
# -------------------------------
st.title("📘 Quiz Física I – UEM 2025")
st.caption("Universidade Eduardo Mondlane - Departamento de Admissão")

if not st.session_state.quiz_finalizado and st.session_state.i < len(st.session_state.perguntas):
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.metric("⏳ Tempo Total", f"{tempo_restante_global // 60}m {tempo_restante_global % 60}s")
    with col_t2:
        st.metric("⏱️ Questão", f"{tempo_restante_questao}s")
    
    st.progress(min(tempo_decorrido_total / TEMPO_TOTAL_EXAME, 1.0))

    if tempo_restante_questao <= 0:
        st.warning("Tempo esgotado para esta questão!")
        time.sleep(1)
        st.session_state.i += 1
        st.session_state.inicio_questao = time.time()
        st.rerun()

    st.divider()

    total_q = len(st.session_state.perguntas)
    q_atual = st.session_state.perguntas[st.session_state.i]
    
    st.write(f"### Questão {q_atual['id']} (Progresso: {st.session_state.i + 1}/{total_q})")
    
    # Exibição de Imagem se houver
    if q_atual["imagem"]:
        #st.image(q_atual["imagem"], caption=f"Figura da Questão {q_atual['id']}")
        st.info(f"📌 [Aqui seria exibida a imagem: {q_atual['imagem']}]")
        
    st.markdown(f"**{q_atual['pergunta']}**")
    
    index_salvo = 0
    if st.session_state.i in st.session_state.respostas_usuario:
        letra = st.session_state.respostas_usuario[st.session_state.i]
        for idx, opt in enumerate(q_atual["opcoes"]):
            if opt.startswith(letra):
                index_salvo = idx

    resposta = st.radio("Selecione a alternativa correta:", q_atual["opcoes"], index=index_salvo, key=f"radio_{st.session_state.i}")

    if st.button("✅ RESPONDER E AVANÇAR", use_container_width=True, type="primary"):
        st.session_state.respostas_usuario[st.session_state.i] = resposta[0]
        st.session_state.i += 1
        st.session_state.inicio_questao = time.time()
        st.rerun()

    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("⬅️ VOLTAR", use_container_width=True, disabled=(st.session_state.i == 0)):
            st.session_state.i -= 1
            st.session_state.inicio_questao = time.time()
            st.rerun()
    with col_btn2:
        if st.button("PULAR ➡️", use_container_width=True):
            st.session_state.i += 1
            st.session_state.inicio_questao = time.time()
            st.rerun()

    st.divider()
    if st.button("🚪 FINALIZAR AGORA", use_container_width=True):
        st.session_state.quiz_finalizado = True
        st.rerun()

    time.sleep(1)
    st.rerun()

else:
    st.header("🏁 Resultado do Exame")
    
    acertos = 0
    total = len(st.session_state.perguntas)
    
    for idx, q in enumerate(st.session_state.perguntas):
        resp = st.session_state.respostas_usuario.get(idx, "N/A")
        if resp == q["correta"]:
            acertos += 1
            
    st.metric("Total de Acertos", f"{acertos} de {total}", f"{(acertos/total)*100:.1f}%")
    
    with st.expander("Revisar Correções"):
        for idx, q in enumerate(st.session_state.perguntas):
            resp = st.session_state.respostas_usuario.get(idx, "Não respondida")
            cor = ":green" if resp == q["correta"] else ":red"
            st.write(f"Questão {q['id']}: {q['pergunta']}")
            st.write(f"Sua resposta: {cor}[{resp}] | Correta: :green[{q['correta']}]")
            st.divider()
    
    if st.button("Tentar Novamente", use_container_width=True):
        reiniciar()
