import streamlit as st
import time
import streamlit.components.v1 as components

# 1. Configurações da Página
st.set_page_config(page_title="Exame de Física UEM 2025", layout="centered")

# 2. Banco de Dados Completo (Questões 41 a 80)
if "perguntas" not in st.session_state:
    st.session_state.perguntas = [
        {"id": 41, "p": "Um recipiente de vidro está quase cheio com água em temperatura ambiente. Ao colocá-lo sobre uma chama de fogão, a água começa a se aquecer por:", "opts": ["A. Condução", "B. irradiação", "C. convecção", "D. condução e convecção", "E. convecção e irradiação"], "c": "C", "img": None},
        {"id": 42, "p": "Quais são as características capazes de distinguir um tipo de onda electromagnética de outro?", "opts": ["A. intensidade, velocidade, área, comprimento", "B. amplitude, velocidade da propagação, frequência, comprimento de onda", "C. amplitude, polarização, frequência, direcção", "D. altura, intensidade, timbre, velocidade", "E. amplitude, perturbação, propagação"], "c": "B", "img": None},
        {"id": 43, "p": "Um transmissor de rádio de satélite artificial da Terra opera a uma frequência de 20 MHz. Qual é o comprimento de onda do transmissor?", "opts": ["A. 15 m", "B. 25 m", "C. 35 m", "D. 45 m", "E. 55 m"], "c": "A", "img": None},
        {"id": 44, "p": "Um corpo de massa 100 g recebeu 1250 cal ao ser aquecido de 30°C a 80°C. Determine o seu calor específico.", "opts": ["A. 0.025 cal/g.°C", "B. 2.50 cal/g.°C", "C. 2,5 cal/g.°C", "D. 25 cal/g.°C", "E. 0,25 cal/g.°C"], "c": "E", "img": None},
        {"id": 45, "p": "Uma lâmpada incandescente (corpo negro) tem temperatura de filamento T=3000K. Determine o comprimento de onda de emissão máxima (nm). Considere b=2,9x10^-3 mK", "opts": ["A. 966", "B. 765", "C. 438", "D. 350", "E. 320"], "c": "A", "img": None},
        {"id": 46, "p": "O gráfico representa a emissividade de corpos X, Y e Z. Qual dos corpos é o menos quente?", "opts": ["A. Ty=Tx", "B. Ty", "C. Tz", "D. Tz=Ty", "E. Tx"], "c": "B", "img": "Gráfico de intensidade vs comprimento de onda (Leis de Wien)"},
        {"id": 47, "p": "Uma estrela tem área superficial de 1/10 * 10^15 m² e potência de 24,3x10^23 W. Qual a temperatura aproximada (K)?", "opts": ["A. 19000", "B. 24000", "C. 28000", "D. 30000", "E. 34000"], "c": "A", "img": None},
        {"id": 48, "p": "Determine a energia de fotões de raios X com comprimento de onda = 1,0x10^-10 m.", "opts": ["A. 5,99x10^-15J", "B. 4,99x10^-15J", "C. 3,99x10^-15J", "D. 2,99x10^-15J", "E. 1,99x10^-15J"], "c": "E", "img": None},
        {"id": 49, "p": "Determine a variação de energia de um átomo ao absorver um quantum com comprimento de onda de 198,6 nm.", "opts": ["A. 0.25x10^-18J", "B. 0.5x10^-18J", "C. 1x10^-18J", "D. 2x10^-18J", "E. 3x10^-18J"], "c": "C", "img": None},
        {"id": 50, "p": "O efeito fotoeléctrico ocorre devido à interação entre:", "opts": ["A. protões e electrões", "B. fotões e electrões", "C. electrões e electrões", "D. fotões e fotões", "E. protões e fotões"], "c": "B", "img": None},
        {"id": 51, "p": "Quantos fotões entram no olho por segundo (comprimento 0,5 µm, potência 2x10^-17 W)?", "opts": ["A. 50", "B. 70", "C. 100", "D. 120", "E. 140"], "c": "A", "img": None},
        {"id": 52, "p": "Qual é o número de fotões de diferentes energias que um átomo de hidrogênio pode emitir se o electrão se encontra na 3ª órbita?", "opts": ["A. 1", "B. 2", "C. 3", "D. 4", "E. 5"], "c": "C", "img": None},
        {"id": 53, "p": "Qual é a energia cinética adquirida por electrões quando acelerados por uma diferença de potencial de 5000 V?", "opts": ["A. 2,0x10^-16J", "B. 4,0x10^-16J", "C. 6,0x10^-16J", "D. 8,0x10^-16J", "E. 10,0x10^-16J"], "c": "D", "img": None},
        {"id": 54, "p": "Qual deve ser a tensão (kV) no ânodo de um tubo de raios X para que a frequência máxima seja 3x10^19 Hz?", "opts": ["A. 124", "B. 130", "C. 132", "D. 140", "E. 142"], "c": "A", "img": None},
        {"id": 55, "p": "No diagrama de níveis de energia do Hidrogénio, qual transição emite fotão com maior momento linear?", "opts": ["A. 1 (n=inf -> n=1)", "B. 2 (n=3 -> n=2)", "C. 3 (n=4 -> n=2)", "D. 4 (n=2 -> n=1)", "E. 5 (n=3 -> n=1)"], "c": "A", "img": "Diagrama de níveis de energia (Transições eletrônicas)"},
        {"id": 56, "p": "A radioactividade emitida por certas amostras de substâncias é consequência de:", "opts": ["A. energia térmica", "B. alterações no núcleo dos átomos", "C. escape de electrões", "D. rupturas de ligações", "E. reorganização de átomos"], "c": "B", "img": None},
        {"id": 57, "p": "Sobre partículas alfa e beta, é correcto afirmar que:", "opts": ["A. beta são 2p+2n", "B. alfa são 2p+2e", "C. alfa são núcleos de Hélio", "D. alfa são apenas 2p", "E. beta são electrões emitidos pelo núcleo instável"], "c": "E", "img": None},
        {"id": 58, "p": "Quantos neutrões tem o núcleo do isótopo de 208/83 Bi?", "opts": ["A. 83", "B. 125", "C. 208", "D. 291", "E. 308"], "c": "B", "img": None},
        {"id": 59, "p": "Na reacção nuclear 27/13Al + gama -> 26/12Mg + X, a incógnita X representa:", "opts": ["A. alumínio", "B. oxigénio", "C. carbono", "D. hidrogénio (protão)", "E. hélio"], "c": "D", "img": None},
        {"id": 60, "p": "No experimento com bloco de chumbo e campo magnético, qual radiação atinge o ponto 3?", "opts": ["A. Infravermelha", "B. Ultravioleta", "C. alfa", "D. beta", "E. gama"], "c": "D", "img": "Experimento de deflexão de radiações em campo magnético"},
        {"id": 61, "p": "Qual das reacções representa a produção de lixo radioactivo (fissão nuclear)?", "opts": ["A. N14+H1", "B. H2+H3", "C. C14 decay", "D. U235+n -> Sr95+Xe139+3n", "E. U235 alfa decay"], "c": "D", "img": None},
        {"id": 62, "p": "Determine a energia de ligação por nucleão de um núcleo com 20 nucleões e energia de ligação total 160 MeV.", "opts": ["A. 4", "B. 8", "C. 16", "D. 32", "E. 40"], "c": "B", "img": None},
        {"id": 63, "p": "Energia liberada (MeV) em uma fusão com defeito de massa de 0,02 uma? (1 uma = 931 MeV)", "opts": ["A. 14,6", "B. 15,6", "C. 16,6", "D. 17,6", "E. 18,6"], "c": "E", "img": None},
        {"id": 64, "p": "Na reacção: n + U235 -> Cs144 + T + 2n, quais os números atómico e de massa de T?", "opts": ["A. 37 e 90", "B. 38 e 91", "C. 39 e 90", "D. 40 e 91", "E. 41 e 90"], "c": "A", "img": None},
        {"id": 65, "p": "Quanto tempo leva para o iodo-131 (meia-vida 8 dias) se desintegrar até 1/16 da sua massa inicial?", "opts": ["A. 8 dias", "B. 16 dias", "C. 24 dias", "D. 32 dias", "E. 40 dias"], "c": "D", "img": None},
        {"id": 66, "p": "Relação entre as vazões Q nas secções (1), (2) e (3) de uma tubulação horizontal afunilada:", "opts": ["A. Q1<Q2<Q3", "B. Q1>Q2>Q3", "C. Q1=Q2=Q3", "D. Q1+Q2=Q3", "E. Q1=Q2+Q3"], "c": "C", "img": "Equação da continuidade em tubulação de diâmetro variável"},
        {"id": 67, "p": "Velocidade do gás na saída sabendo que na entrada P1=8atm, v1=10m/s e na saída P2=1atm?", "opts": ["A. 40 m/s", "B. 50 m/s", "C. 60 m/s", "D. 70 m/s", "E. 80 m/s"], "c": "B", "img": None},
        {"id": 68, "p": "Velocidade v2 em tubulação com v1=3m/s, r1=0,1m e r2=0,05m (Incompressível):", "opts": ["A. 6 m/s", "B. 9 m/s", "C. 12 m/s", "D. 15 m/s", "E. 18 m/s"], "c": "C", "img": None},
        {"id": 69, "p": "Qual é a vazão (dm³/s) de uma torneira que enche um tanque de 12000L em 40 minutos?", "opts": ["A. 5", "B. 10", "C. 15", "D. 20", "E. 25"], "c": "A", "img": None},
        {"id": 70, "p": "Força aplicada (N) em prensa hidráulica para levantar carro de 1000kg (áreas 4m² e 0,0025m²)?", "opts": ["A. 4,25", "B. 5,25", "C. 6,25", "D. 7,25", "E. 8,25"], "c": "C", "img": None},
        {"id": 71, "p": "Velocidade (m/s) para encher piscina (18x10x2m) em 10h com conduto de 25cm²?", "opts": ["A. 2", "B. 4", "C. 6", "D. 8", "E. 10"], "c": "B", "img": None},
        {"id": 72, "p": "Determine o número de moles em um recipiente cúbico de 0,5m de lado, P=59760Pa, T=300K.", "opts": ["A. 3", "B. 5", "C. 7", "D. 9", "E. 11"], "c": "A", "img": None},
        {"id": 73, "p": "Denominações das etapas (1->2, 2->3, 3->1) no gráfico V(L) vs T(K) apresentado:", "opts": ["A. Isobárica, Isovolumétrica", "B. Isovolumétrica, Isobárica, Isotérmica", "C. Isotérmica, Isobárica", "D. Adiabática", "E. Cíclica"], "c": "B", "img": "Ciclo termodinâmico em diagrama V-T"},
        {"id": 74, "p": "Volume (L) de hidrogênio a 293K (inicial 0,15L a 300K, Pressão constante)?", "opts": ["A. 0,10", "B. 0,12", "C. 0,14", "D. 0,15", "E. 0,16"], "c": "C", "img": None},
        {"id": 75, "p": "Qual representação de processos em gases ideais é FALSA nos gráficos de p, V e T?", "opts": ["A. Gráfico p-V Isotérmico", "B. Gráfico V-T Isobárico", "C. Gráfico p-T Isocórico", "D. Gráfico p-V Isobárico", "E. Todas estão corretas exceto uma"], "c": "E", "img": "Conjunto de gráficos p-V, V-T e p-T"},
        {"id": 76, "p": "Variação de energia interna total após as duas etapas (Q1=500, W1=200; Q2=-300, W2=-100)?", "opts": ["A. 50", "B. 100", "C. 150", "D. 200", "E. 250"], "c": "B", "img": None},
        {"id": 77, "p": "Trabalho realizado por gás em expansão adiabática que recebe 10 kJ?", "opts": ["A. 0", "B. 5", "C. 10", "D. 15", "E. 20"], "c": "C", "img": None},
        {"id": 78, "p": "O trabalho total realizado pelo sistema, em J, no ciclo XY-YZ-ZX do gráfico p(Pa) vs V(m³) é:", "opts": ["A. 1,6x10^5", "B. 2,0x10^5", "C. 3,2x10^5", "D. 4,8x10^5", "E. 0"], "c": "A", "img": "Diagrama p-V com ciclo triangular"},
        {"id": 79, "p": "Período e amplitude de massa 0,2kg, k=0,8pi² N/m, afastada 3cm do equilíbrio?", "opts": ["A. 0,5s e 2cm", "B. 1,0s e 3cm", "C. 1,5s e 4cm", "D. 2,0s e 5cm", "E. 2,5s e 6cm"], "c": "B", "img": None},
        {"id": 80, "p": "Qual é o valor da amplitude de aceleração do corpo no gráfico do Movimento Harmónico Simples?", "opts": ["A. pi²", "B. 2pi²", "C. 3pi²", "D. 4pi²", "E. 5pi²"], "c": "B", "img": "Gráfico de posição vs tempo em MHS"}
    ]

# 3. Gestão de Estado da Sessão
if "i" not in st.session_state: st.session_state.i = 0
if "respostas" not in st.session_state: st.session_state.respostas = {}
if "quiz_fim" not in st.session_state: st.session_state.quiz_fim = False
if "ver_gabarito" not in st.session_state: st.session_state.ver_gabarito = False
if "inicio_t" not in st.session_state: st.session_state.inicio_t = time.time()

def reiniciar_total():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# 4. Interface Principal
st.title("📝 Exame de Admissão Física I - UEM 2025")

if not st.session_state.quiz_fim:
    # --- TEMPO NO TOPO ---
    t_restante = max(0, 5400 - int(time.time() - st.session_state.inicio_t))
    c_t1, c_t2 = st.columns(2)
    c_t1.metric("⏳ Tempo Restante", f"{t_restante//60}m {t_restante%60}s")
    c_t2.metric("📊 Questão", f"{st.session_state.i + 1} / 40")
    
    st.divider()

    idx = st.session_state.i
    quest = st.session_state.perguntas[idx]
    
    # --- MOSTRAR FIGURAS (Placeholder descritivo) ---
    if quest["img"]:
        st.warning(f"🖼️ FIGURA DA QUESTÃO {quest['id']}:")
        st.write(f"*{quest['img']}*")
        
        # Inserindo tags de busca de diagramas contextuais para ajudar o estudante
        if quest["id"] == 46:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Wiens_law.svg/300px-Wiens_law.svg.png", caption="Exemplo de gráfico de Wien")
        elif quest["id"] == 55:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Bohr_atom_model.svg/300px-Bohr_atom_model.svg.png", caption="Níveis de energia de Bohr")
        elif quest["id"] == 78:
            

    st.markdown(f"#### {quest['p']}")
    
    marcada = st.session_state.respostas.get(idx, None)
    id_radio = 0
    if marcada:
        for i_opt, txt in enumerate(quest["opts"]):
            if txt.startswith(marcada): id_radio = i_opt

    escolha = st.radio("Escolha a sua resposta:", quest["opts"], index=id_radio, key=f"r{idx}")

    # --- NAVEGAÇÃO ---
    if st.button("✅ RESPONDER E AVANÇAR", use_container_width=True, type="primary"):
        st.session_state.respostas[idx] = escolha[0]
        if idx + 1 < 40:
            st.session_state.i += 1
        else:
            st.session_state.quiz_fim = True
        st.rerun()

    c_b1, c_b2 = st.columns(2)
    with c_b1:
        if st.button("⬅️ VOLTAR", use_container_width=True, disabled=(idx==0)):
            st.session_state.i -= 1
            st.rerun()
    with c_b2:
        if st.button("PULAR ➡️", use_container_width=True):
            if idx + 1 < 40:
                st.session_state.i += 1
            else:
                st.session_state.quiz_fim = True
            st.rerun()

    time.sleep(1)
    st.rerun()

# 5. ECRÃ DE RESULTADOS
else:
    st.success("🏁 EXAME TERMINADO!")
    
    acertos = sum(1 for i, q in enumerate(st.session_state.perguntas) if st.session_state.respostas.get(i) == q["c"])
    
    st.markdown("### 📊 Resultado")
    res_c1, res_c2 = st.columns(2)
    res_c1.metric("Pontuação", f"{acertos} / 40")
    res_c2.metric("Nota (0-20)", f"{(acertos/40)*20:.1f}")

    if st.button("📸 CAPTURAR RESULTADOS (PDF/PRINT)", use_container_width=True, type="primary"):
        components.html("<script>window.print();</script>", height=0)

    st.divider()

    # --- GABARITO ---
    if not st.session_state.ver_gabarito:
        if st.button("🔍 MOSTRAR CORRECÇÃO", use_container_width=True):
            st.session_state.ver_gabarito = True
            st.rerun()
    else:
        for i, q in enumerate(st.session_state.perguntas):
            sua = st.session_state.respostas.get(i, "N/A")
            cor = "✅" if sua == q["c"] else "❌"
            with st.expander(f"Questão {q['id']}: {cor}"):
                st.write(f"**Pergunta:** {q['p']}")
                st.write(f"Sua Resposta: {sua} | Correcta: {q['c']}")
        
        if st.button("⬆️ ESCONDER CORRECÇÃO", use_container_width=True):
            st.session_state.ver_gabarito = False
            st.rerun()

    # --- REINICIAR ---
    if st.button("🔄 REINICIAR TESTE (LIMPAR TUDO)", use_container_width=True):
        reiniciar_total()
