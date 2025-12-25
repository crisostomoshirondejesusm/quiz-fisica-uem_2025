import streamlit as st
import time
import streamlit.components.v1 as components
import os

# 1. Configurações da Página
st.set_page_config(page_title="Exame Unificado UEM 2025", layout="centered")

# 2. Banco de Dados Unificado (Extraído do PDF e do seu código)
if "perguntas" not in st.session_state:
    # --- QUESTÕES DE FÍSICA (41 a 80) ---
    f_qs = [
        {"id": 41, "p": "Um recipiente de vidro está quase cheio com água em temperatura ambiente. Ao colocá-lo sobre uma chama de fogão, a água começa a se aquecer por:", "opts": ["A. Condução", "B. irradiação", "C. convecção", "D. condução e convecção", "E. convecção e irradiação"], "c": "C", "img": None},
        {"id": 42, "p": "Quais são as características capazes de distinguir um tipo de onda electromagnética de outro?", "opts": ["A. intensidade, velocidade, área, comprimento", "B. amplitude, velocidade da propagação, frequência, comprimento de onda", "C. amplitude, polarização, frequência, direcção", "D. altura, intensidade, timbre, velocidade", "E. amplitude, perturbação, propagação"], "c": "B", "img": None},
        {"id": 43, "p": "Um transmissor de rádio opera a 20 MHz. Qual é o comprimento de onda do transmissor?", "opts": ["A. 15 m", "B. 25 m", "C. 35 m", "D. 45 m", "E. 55 m"], "c": "A", "img": None},
        {"id": 44, "p": "Um corpo de massa 100 g recebeu 1250 cal ao ser aquecido de 30°C a 80°C. O seu calor específico é:", "opts": ["A. 0.025 cal/g.°C", "B. 2.50 cal/g.°C", "C. 2,5 cal/g.°C", "D. 25 cal/g.°C", "E. 0,25 cal/g.°C"], "c": "E", "img": None},
        {"id": 45, "p": "Uma lâmpada incandescente (corpo negro) tem T=3000K. Determine o comprimento de onda de emissão máxima (nm). (b=2,9x10^-3 mK)", "opts": ["A. 966", "B. 765", "C. 438", "D. 350", "E. 320"], "c": "A", "img": None},
        {"id": 46, "p": "O gráfico representa a emissividade de corpos X, Y e Z. Qual dos corpos é o menos quente?", "opts": ["A. Ty=Tx", "B. Ty", "C. Tz", "D. Tz=Ty", "E. Tx"], "c": "B", "img": "q46.png"},
        {"id": 47, "p": "Uma estrela tem área de 1/10 * 10^15 m² e potência de 24,3x10^23 W. Qual a temperatura (K)?", "opts": ["A. 19000", "B. 24000", "C. 28000", "D. 30000", "E. 34000"], "c": "A", "img": None},
        {"id": 48, "p": "Determine a energia de fotões de raios X com comprimento de onda de 1,0x10^-10 m.", "opts": ["A. 5,99x10^-15J", "B. 4,99x10^-15J", "C. 3,99x10^-15J", "D. 2,99x10^-15J", "E. 1,99x10^-15J"], "c": "E", "img": None},
        {"id": 49, "p": "Variação de energia de um átomo ao absorver um quantum com comprimento de onda de 198,6 nm.", "opts": ["A. 0.25x10^-18J", "B. 0.5x10^-18J", "C. 1x10^-18J", "D. 2x10^-18J", "E. 3x10^-18J"], "c": "C", "img": None},
        {"id": 50, "p": "O efeito fotoeléctrico ocorre devido à interação entre:", "opts": ["A. protões e electrões", "B. fotões e electrões", "C. electrões e electrões", "D. fotões e fotões", "E. protões e fotões"], "c": "B", "img": None},
        {"id": 51, "p": "Quantos fotões entram no olho por segundo (comprimento 0,5 µm, potência 2x10^-17 W)?", "opts": ["A. 50", "B. 70", "C. 100", "D. 120", "E. 140"], "c": "A", "img": None},
        {"id": 52, "p": "Número de fotões de diferentes energias que um átomo de hidrogênio emite com electrão na 3ª órbita?", "opts": ["A. 1", "B. 2", "C. 3", "D. 4", "E. 5"], "c": "C", "img": None},
        {"id": 53, "p": "Energia cinética adquirida por electrões acelerados por 5000 V?", "opts": ["A. 2,0x10^-16J", "B. 4,0x10^-16J", "C. 6,0x10^-16J", "D. 8,0x10^-16J", "E. 10,0x10^-16J"], "c": "D", "img": None},
        {"id": 54, "p": "Tensão (kV) no ânodo de tubo de raios X para frequência máxima de 3x10^19 Hz?", "opts": ["A. 124", "B. 130", "C. 132", "D. 140", "E. 142"], "c": "A", "img": None},
        {"id": 55, "p": "No diagrama de níveis de energia, qual transição emite fotão com maior momento linear?", "opts": ["A. 1", "B. 2", "C. 3", "D. 4", "E. 5"], "c": "A", "img": "q55.png"},
        {"id": 56, "p": "A radioactividade é consequência de:", "opts": ["A. energia térmica", "B. alterações no núcleo dos átomos", "C. escape de electrões", "D. rupturas químicas", "E. reorganização de átomos"], "c": "B", "img": None},
        {"id": 57, "p": "Sobre partículas alfa e beta, é correcto dizer que:", "opts": ["A. beta são 2p+2n", "B. alfa são 2p+2e", "C. alfa são núcleos de hélio", "D. alfa são apenas 2p", "E. beta são electrões do núcleo"], "c": "E", "img": None},
        {"id": 58, "p": "Quantos neutrões tem o núcleo de 208/83 Bi?", "opts": ["A. 83", "B. 125", "C. 208", "D. 291", "E. 308"], "c": "B", "img": None},
        {"id": 59, "p": "Na reacção 27/13Al + gama -> 26/12Mg + X, a incógnita X representa:", "opts": ["A. alumínio", "B. oxigénio", "C. carbono", "D. hidrogénio", "E. hélio"], "c": "D", "img": None},
        {"id": 60, "p": "Radiação que atinge o ponto 3 no experimento do Bloco de Chumbo:", "opts": ["A. Infravermelha", "B. Ultravioleta", "C. alfa", "D. beta", "E. gama"], "c": "D", "img": "q60.png"},
        {"id": 61, "p": "Reacção que representa a produção de lixo radioactivo (fissão):", "opts": ["A. Fusão solar", "B. Decaimento beta", "C. Reacção em cadeia U-235", "D. Emissão gama", "E. Fusão de Hidrogênio"], "c": "C", "img": None},
        {"id": 62, "p": "Energia de ligação por nucleão de um núcleo com 20 nucleões e energia total 160 MeV?", "opts": ["A. 4", "B. 8", "C. 16", "D. 32", "E. 40"], "c": "B", "img": None},
        {"id": 63, "p": "Energia liberada (MeV) em fusão com defeito de massa de 0,02 uma? (1 uma = 931 MeV)", "opts": ["A. 14,6", "B. 15,6", "C. 16,6", "D. 17,6", "E. 18,6"], "c": "E", "img": None},
        {"id": 64, "p": "Na reacção: n + U235 -> Cs144 + T + 2n, quais os números de T?", "opts": ["A. 37 e 90", "B. 38 e 91", "C. 39 e 90", "D. 40 e 91", "E. 41 e 90"], "c": "A", "img": None},
        {"id": 65, "p": "Tempo para iodo-131 (meia-vida 8 dias) chegar a 1/16 da massa inicial?", "opts": ["A. 8 dias", "B. 16 dias", "C. 24 dias", "D. 32 dias", "E. 40 dias"], "c": "D", "img": None},
        {"id": 66, "p": "Relação entre as vazões Q nas secções (1), (2) e (3) de uma tubulação?", "opts": ["A. Q1<Q2<Q3", "B. Q1>Q2>Q3", "C. Q1=Q2=Q3", "D. Q1+Q2=Q3", "E. Q1=Q2+Q3"], "c": "C", "img": "q66.png"},
        {"id": 67, "p": "Velocidade do gás na saída sabendo P1=8atm, v1=10m/s e P2=1atm?", "opts": ["A. 40 m/s", "B. 50 m/s", "C. 60 m/s", "D. 70 m/s", "E. 80 m/s"], "c": "B", "img": None},
        {"id": 68, "p": "Velocidade v2 em tubulação com v1=3m/s, r1=0,1m e r2=0,05m?", "opts": ["A. 6 m/s", "B. 9 m/s", "C. 12 m/s", "D. 15 m/s", "E. 18 m/s"], "c": "C", "img": None},
        {"id": 69, "p": "Vazão (dm³/s) de torneira que enche 12000L em 40 minutos?", "opts": ["A. 5", "B. 10", "C. 15", "D. 20", "E. 25"], "c": "A", "img": None},
        {"id": 70, "p": "Força (N) em prensa hidráulica para levantar 1000kg (áreas 4m² e 0,0025m²)?", "opts": ["A. 4,25", "B. 5,25", "C. 6,25", "D. 7,25", "E. 8,25"], "c": "C", "img": None},
        {"id": 71, "p": "Velocidade (m/s) para encher piscina (18x10x2m) em 10h com conduto de 25cm²?", "opts": ["A. 2", "B. 4", "C. 6", "D. 8", "E. 10"], "c": "B", "img": None},
        {"id": 72, "p": "Número de moles em recipiente cúbico (0,5m), P=59760Pa, T=300K?", "opts": ["A. 3", "B. 5", "C. 7", "D. 9", "E. 11"], "c": "A", "img": None},
        {"id": 73, "p": "Denominações das etapas (1->2, 2->3, 3->1) no gráfico V vs T?", "opts": ["A. Isobárica, Isovolumétrica", "B. Isovolumétrica, Isobárica, Isotérmica", "C. Isotérmica, Isobárica", "D. Adiabática", "E. Cíclica"], "c": "B", "img": "q73.png"},
        {"id": 74, "p": "Volume (L) de hidrogênio a 293K (inicial 0,15L a 300K, P constante)?", "opts": ["A. 0,10", "B. 0,12", "C. 0,14", "D. 0,15", "E. 0,16"], "c": "C", "img": None},
        {"id": 75, "p": "Qual representação de processos em gases ideais é FALSA?", "opts": ["A", "B", "C", "D", "E"], "c": "E", "img": "q75.png"},
        {"id": 76, "p": "Variação de energia interna total após as duas etapas (Q1=500, W1=200; Q2=-300, W2=-100)?", "opts": ["A. 50", "B. 100", "C. 150", "D. 200", "E. 250"], "c": "B", "img": None},
        {"id": 77, "p": "Trabalho realizado por gás em expansão adiabática que recebe 10 kJ?", "opts": ["A. 0", "B. 5", "C. 10", "D. 15", "E. 20"], "c": "C", "img": None},
        {"id": 78, "p": "Trabalho total (J) no ciclo XY-YZ-ZX do gráfico p vs V?", "opts": ["A. 1,6x10^5", "B. 2,0x10^5", "C. 3,2x10^5", "D. 4,8x10^5", "E. 0"], "c": "A", "img": "q78.png"},
        {"id": 79, "p": "Período e amplitude de massa 0,2kg, k=0,8pi² N/m, afastada 3cm?", "opts": ["A. 0,5s e 2cm", "B. 1,0s e 3cm", "C. 1,5s e 4cm", "D. 2,0s e 5cm", "E. 2,5s e 6cm"], "c": "B", "img": None},
        {"id": 80, "p": "Valor da amplitude de aceleração do corpo no gráfico MHS?", "opts": ["A. pi²", "B. 2pi²", "C. 3pi²", "D. 4pi²", "E. 5pi²"], "c": "B", "img": "q80.png"}
    ]

    # --- QUESTÕES DE MATEMÁTICA (1 a 40) ---
    m_qs = [
        {"id": 1, "p": "Indique as soluções da equação $-|x-2|+6=2$:", "opts": ["A. x=2 v x=6", "B. x=-4 v x=4", "C. x=2", "D. x=-2 v x=6", "E. x=4"], "c": "D", "img": None},
        {"id": 2, "p": "Dizemos que $|x|>3$ se:", "opts": ["A. x ∈ ]-∞,-3[ ∪ ]3,+∞[", "B. x ∈ R", "C. x ∈ ]-3,3[", "D. x ∈ ]-∞,-3] ∪ [3,+∞[", "E. x ∈ ]3,+∞["], "c": "A", "img": None},
        {"id": 3, "p": "O conjunto dos números reais que se encontra a uma distância igual ou inferior a 3/2 de π é:", "opts": ["A. x - 3/2 = π", "B. |x - π| ≤ 3/2", "C. |x - 3/2| ≤ π", "D. x + 3/2 ≥ π", "E. x ≤ 3/2"], "c": "B", "img": None},
        {"id": 4, "p": "A função $y=|ax^2+bx+c|, (a≠0)$ é uma função:", "opts": ["A. Positiva", "B. Positiva se x≥0", "C. Par", "D. Ímpar", "E. Nenhuma delas"], "c": "E", "img": None},
        {"id": 5, "p": "Para que valores de x é válida a equação $|x+\pi|=-(x+\pi)$?", "opts": ["A. x ≥ 0", "B. x = -π", "C. x ≥ π", "D. x ≤ 0", "E. x ≤ -π"], "c": "E", "img": None},
        {"id": 6, "p": "Qual a intersecção das funções $f(x)=-|x|+4$ e $g(x)=|x+1|$?", "opts": ["A. x=-3 v x=3", "B. x=-1 v x=4", "C. x=0", "D. x=-x", "E. x=-1 v x=3/2"], "c": "E", "img": None},
        {"id": 7, "p": "Escolhendo ao acaso um divisor de 60, qual a probabilidade de ser um número primo?", "opts": ["A. 0,25", "B. 0,3", "C. 1,2", "D. 0,6", "E. 0,75"], "c": "A", "img": None},
        {"id": 8, "p": "A solução da equação $C_2^n=6$ é:", "opts": ["A. n=4 v n=-3", "B. n=-4 v n=3", "C. n=3", "D. n=4", "E. n=6"], "c": "D", "img": None},
        {"id": 9, "p": "Quantos códigos numéricos de quatro dígitos existem?", "opts": ["A. 40", "B. 400", "C. 10000", "D. 8000", "E. 40000"], "c": "C", "img": None},
        {"id": 10, "p": "Anagramas de LÁPIS que terminam em 3 consoantes:", "opts": ["A. 6", "B. 5!", "C. 2! x 3!", "D. 12", "E. 10"], "c": "D", "img": None},
        {"id": 11, "p": "Formas de sentar 5 pessoas em 8 lugares:", "opts": ["A. 5^8", "B. A(8,5)x3", "C. C(8,5)x3!", "D. A(6,5)xA(8,3)", "E. C(8,5)x5!"], "c": "E", "img": None},
        {"id": 12, "p": "Numa caixa há bolas amarelas e azuis. Azuis=14. P(azul)=2/3. Quantas amarelas?", "opts": ["A. 7", "B. 28", "C. 3", "D. 10", "E. 9"], "c": "A", "img": None},
        {"id": 13, "p": "Triângulo Pascal (linha 15): Escolhidos 2 elementos, P(ser 105):", "opts": ["A. 3/21", "B. 2/3", "C. 1/15", "D. 1/5", "E. 1/8"], "c": "E", "img": None},
        {"id": 14, "p": "Domínio de $f(x)=\sqrt{x-1} \cdot \ln(1-x^2)$:", "opts": ["A. R", "B. ]-1,1[", "C. [1,+∞[", "D. {1}", "E. ∅"], "c": "E", "img": None},
        {"id": 15, "p": "Imagem de $f(x)=5\cos(2x)+1$:", "opts": ["A. [-1,1]", "B. [-5,5]", "C. [-4,6]", "D. [0,1]", "E. Nenhuma"], "c": "C", "img": None},
        {"id": 16, "p": "Função afim com zero em 3 e $g(-2)=-5$:", "opts": ["A. g(x)=-x+3", "B. g(x)=-x+7", "C. g(x)=x^2-9", "D. g(x)=x-3", "E. g(x)=3x+1"], "c": "D", "img": None},
        {"id": 17, "p": "Sobre $f(x)=-x^2+4$, é verdade que:", "opts": ["A. É monótona", "B. Domínio é R", "C. É injectiva", "D. Um só zero", "E. Tem mínimo"], "c": "B", "img": None},
        {"id": 18, "p": "Assímptotas verticais $x=-2, x=3$ e horizontal $y=2$:", "opts": ["A. (x-3)/(x-5)", "B. (-2x+3)/(x^2-x-6)", "C. x/(-2x^2-x-3)", "D. 2x/(-x+4)", "E. (2x^2+7)/(x^2-x-6)"], "c": "E", "img": None},
        {"id": 19, "p": "Se $f(x)=2^x-2$ e $g(x)=f(x+k)$ passa em (-4, -3/2), qual o k?", "opts": ["A. 3", "B. -3", "C. 4", "D. -4", "E. 0"], "c": "A", "img": None},
        {"id": 20, "p": "Zeros de $(f \circ g^{-1})(x)$ para $f(x)=x^2-9, g(x)=2x+4$:", "opts": ["A. {-2, 10}", "B. {-3, 2, 3}", "C. {-3, 0}", "D. {0}", "E. {1, 3}"], "c": "A", "img": None},
        {"id": 21, "p": "P.A.: $u_5+u_6=31$ e $u_7+u_9=46$. Termos:", "opts": ["A. u1=1, r=3", "B. u1=-2, r=2", "C. u1=2, r=3", "D. u1=3, r=4", "E. u1=3, r=2"], "c": "C", "img": None},
        {"id": 22, "p": "P.G.: $v_5=4$ e $v_8=108$. Valor de $v_6$:", "opts": ["A. 6", "B. 12", "C. 51", "D. 76", "E. 98"], "c": "B", "img": None},
        {"id": 23, "p": "Sucessão $u_n = \log_{1/2}(3^n)$:", "opts": ["A. P.A. cresc.", "B. P.A. decr.", "C. P.G. cresc.", "D. P.G. decr.", "E. Nenhuma"], "c": "B", "img": None},
        {"id": 24, "p": "Qual é convergente?", "opts": ["A. (-1)^n * n", "B. (-1)^n + n", "C. (-1)^n - n", "D. (-1)^n / n", "E. (-1)^n * n!"], "c": "D", "img": None},
        {"id": 25, "p": "Sobre $v_n$ (n se n<10, 1+1/n se n≥10):", "opts": ["A. ilimitada", "B. decrescente", "C. crescente", "D. divergente", "E. limitada"], "c": "E", "img": None},
        {"id": 26, "p": "Limite de $(2n^2+3n+4)/(n^2+4)$:", "opts": ["A. 0", "B. 1", "C. 2", "D. 3", "E. ∞"], "c": "C", "img": None},
        {"id": 27, "p": "Limite de $(1 + 1/n)^{2n}$:", "opts": ["A. 1", "B. 2e", "C. e^2", "D. -∞", "E. +∞"], "c": "C", "img": None},
        {"id": 28, "p": "Para que 'a' a função (2-x se x<a, x^2+2 se x≥a) é contínua?", "opts": ["A. -5", "B. -4", "C. -3/2", "D. -1", "E. -1/2"], "c": "D", "img": None},
        {"id": 29, "p": "Se $y=3x-5$ é assímptota de $g(x)$, então:", "opts": ["A. lim[g+3x]=-5", "B. lim[g+3x]=5", "C. lim[g+3x-5]=0", "D. lim[g-3x+5]=0", "E. lim[g-3x+5]=∞"], "c": "D", "img": None},
        {"id": 30, "p": "Analise o gráfico em x=2:", "opts": ["A. lim x->2- = f(2)", "B. lim x->2 não existe", "C. lim x->2 = 2", "D. lim x->2+ ≠ f(2)", "E. Nenhuma"], "c": "B", "img": "q30_mat.png"},
        {"id": 31, "p": "Limite de $\sin(2x)/x$ quando x->0:", "opts": ["A. -1", "B. 0", "C. 1/2", "D. 1", "E. 2"], "c": "E", "img": None},
        {"id": 32, "p": "Limite x->∞ de $(5x-2)/x - (4x^2+2x+1)/(2x^2+1)$:", "opts": ["A. -∞", "B. 0", "C. 3", "D. 9", "E. ∞"], "c": "C", "img": None},
        {"id": 33, "p": "Derivada de $f(x) = \ln(2x^2/3 + 2)$:", "opts": ["A. 2x^2/3+2", "B. 4x/3", "C. (2x^2+3)/4x", "D. 4x/(2x^2+6)", "E. e^f(x)"], "c": "D", "img": None},
        {"id": 34, "p": "Se $g(x) = g'(x)$, então:", "opts": ["A. g(x)=5", "B. g(x)=3e^x", "C. g(x)=2cos(x)", "D. g(x)=x^2+1", "E. g(x)=√x"], "c": "B", "img": None},
        {"id": 35, "p": "Declive da tangente em x=2 de $kx^2+10x+1$ é 2. k é:", "opts": ["A. 2", "B. -3", "C. 1/2", "D. -2", "E. 1/3"], "c": "D", "img": None},
        {"id": 36, "p": "Recta tangente a $\sin(\pi x)$ em x=1:", "opts": ["A. y=1", "B. y=1-x", "C. y=-πx", "D. y=π-πx", "E. y=πx-1"], "c": "D", "img": None},
        {"id": 37, "p": "Sobre $f(x)=x^3-3x^2-24x+1$:", "opts": ["A. Mín x=4, Máx x=-2", "B. 2 Máximos", "C. Mín x=2", "D. Mín x=0, Máx x=2", "E. Sem extremos"], "c": "A", "img": None},
        {"id": 38, "p": "Concavidade de $f'(x)=2xe^{1-x^2}$ voltada para cima em:", "opts": ["A. ]-∞,-1[U]1,∞[", "B. ]-√2/2, √2/2[", "C. ]-∞, -√2/2[U]√2/2, ∞[", "D. ]-∞,0[", "E. ]-∞,-2[U]2,∞["], "c": "B", "img": None},
        {"id": 39, "p": "Primitiva de $e^x + 1$:", "opts": ["A. 2e^x", "B. e^(x^2)/2", "C. e^x/2 + x", "D. xe^(x-1)+x", "E. e^x + x"], "c": "E", "img": None},
        {"id": 40, "p": "Resultado de $(3 - 2i) \cdot (-4 + i)$:", "opts": ["A. 10+2i", "B. 11i", "C. -12-2i", "D. -10+11i", "E. -10"], "c": "D", "img": None}
    ]

    # Intercalar: 1 Matemática, 1 Física
    intercaladas = []
    for m, f in zip(m_qs, f_qs):
        intercaladas.append(m)
        intercaladas.append(f)
    
    st.session_state.perguntas = intercaladas

# 3. Gestão de Estado (Controle de fluxo)
if "i" not in st.session_state: st.session_state.i = 0
if "respostas" not in st.session_state: st.session_state.respostas = {}
if "quiz_fim" not in st.session_state: st.session_state.quiz_fim = False
if "ver_gabarito" not in st.session_state: st.session_state.ver_gabarito = False
if "inicio_t" not in st.session_state: st.session_state.inicio_t = time.time()
if "quest_t" not in st.session_state: st.session_state.quest_t = time.time()

def reiniciar_total():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

def proxima_questao():
    if st.session_state.i + 1 < len(st.session_state.perguntas):
        st.session_state.i += 1
        st.session_state.quest_t = time.time()
    else:
        st.session_state.quiz_fim = True
    st.rerun()

# 4. Interface
st.title("🎓 Preparação UEM 2025")
st.subheader("Exame Integrado: Matemática e Física")

if not st.session_state.quiz_fim:
    # Cronômetro
    t_global = max(0, 7200 - int(time.time() - st.session_state.inicio_t)) # 2 horas total
    t_quest = max(0, 180 - int(time.time() - st.session_state.quest_t)) # 3 min por questão
    
    if t_quest <= 0: proxima_questao()

    c1, c2, c3 = st.columns(3)
    c1.metric("⏳ Total", f"{t_global//60}m")
    c2.metric("⏱️ Questão", f"{t_quest}s")
    c3.metric("📊 Progresso", f"{st.session_state.i + 1}/80")
    
    st.divider()

    # Mostrar questão
    q = st.session_state.perguntas[st.session_state.i]
    materia = "📐 MATEMÁTICA" if q['id'] <= 40 else "🍎 FÍSICA"
    st.info(f"Matéria: {materia}")

    if q["img"]:
        caminho = f"imagens/{q['img']}"
        if os.path.exists(caminho):
            st.image(caminho, use_container_width=True)
        else:
            st.warning(f"Figura necessária: {q['img']}")

    st.markdown(f"### Questão {q['id']}")
    st.markdown(q['p'])

    # Resposta
    id_radio = 0
    atual = st.session_state.respostas.get(st.session_state.i, None)
    if atual:
        for idx_opt, txt in enumerate(q["opts"]):
            if txt.startswith(atual): id_radio = idx_opt

    escolha = st.radio("Sua resposta:", q["opts"], index=id_radio, key=f"q{st.session_state.i}")

    if st.button("✅ AVANÇAR", use_container_width=True, type="primary"):
        st.session_state.respostas[st.session_state.i] = escolha[0]
        proxima_questao()

    # Navegação
    col_v, col_p = st.columns(2)
    with col_v:
        if st.button("⬅️ VOLTAR", use_container_width=True, disabled=(st.session_state.i==0)):
            st.session_state.i -= 1
            st.rerun()
    with col_p:
        if st.button("PULAR ➡️", use_container_width=True):
            proxima_questao()

    time.sleep(1)
    st.rerun()

else:
    st.success("🏁 EXAME FINALIZADO!")
    total = len(st.session_state.perguntas)
    acertos = sum(1 for i, q in enumerate(st.session_state.perguntas) if st.session_state.respostas.get(i) == q["c"])
    
    st.metric("Sua Nota (0-20)", f"{(acertos/total)*20:.1f}")
    
    if st.button("🔄 REINICIAR", use_container_width=True):
        reiniciar_total()

    st.divider()
    if st.button("🔍 MOSTRAR GABARITO", use_container_width=True):
        st.session_state.ver_gabarito = not st.session_state.ver_gabarito

    if st.session_state.ver_gabarito:
        for i, q in enumerate(st.session_state.perguntas):
            resp = st.session_state.respostas.get(i, "-")
            status = "✅" if resp == q["c"] else "❌"
            with st.expander(f"Q{q['id']} - {status}"):
                st.write(f"Sua: {resp} | Correta: {q['c']}")
