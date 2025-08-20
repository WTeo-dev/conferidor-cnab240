import streamlit as st
import pandas as pd

# === Funções de extração ===
#header ok
def extrair_header_arquivo(linha):
    return {
        "Código do Banco": linha[0:3],
        "Lote de Serviço": linha[3:7],
        "Tipo de Registro": linha[7:8],
        "Exclusivo Febraban": linha[8:17],
        "Tipo de Inscrição": linha[17:18],
        "Número de Inscrição": linha[18:32],
        "Número do Convênio": linha[32:41],
        "Cobrança Cedente": linha[41:45],
        "Carteira": linha[45:47],
        "Variação da Carteira": linha[47:50],
        "Reservado BB": linha[50:52],        
        "Agência": linha[52:57],
        "DV Agência": linha[57:58],
        "Conta": linha[58:70],
        "DV Conta": linha[70:71],
        "DV Agência/Conta": linha[71:72],
        "Nome da Empresa": linha[72:102].strip(),
        "Nome do Banco": linha[102:132].strip(),
        "Exclusivo Febraban": linha[132:142], 
        "Código Remessa": linha[142:143],
        "Data de Geração": linha[143:151],
        "Hora de Geração": linha[151:157],
        "Sequencial do Arquivo": linha[157:163],
        "Versão do Layout": linha[163:166],
        "Densidade de Gravação": linha[166:171],
        "Reservado Banco": linha[171:191].strip(),
        "Reservado Empresa": linha[191:211].strip(),
        "Reservado Febraban": linha[211:240].strip()
    }

#header lote
def extrair_header_lote(linha):
    return {
        "Código do Banco": linha[0:3],
        "Lote de Serviço": linha[3:7],
        "Tipo de Registro": linha[7:8],
        "Tipo de Operação": linha[8:9],#R-remessa T-retorno P-baixa
        "Tipo de Serviço": linha[9:11],
        "Exclusivo Febraban": linha[11:13],
        "Versão do Layout": linha[13:16],
        "Exclusivo Febraban2": linha[16:17],
        "Tipo de Inscrição": linha[17:18],
        "Número de Inscrição": linha[18:33],
        "Convênio": linha[33:42],
        "Cobrança Cedente": linha[42:46],
        "Carteira": linha[46:48],
        "Variação da Carteira": linha[48:51],
        "Se Teste": linha[51:53], #TS-teste
        "Agência": linha[53:58],
        "DV Agência": linha[58:59],
        "Conta": linha[59:71],
        "DV Conta": linha[71:72],
        "DV Agência/Conta": linha[72:73],
        "Nome da Empresa": linha[73:103].strip(),
        "Mensagem 1": linha[103:143].strip(),
        "Mensagem 2": linha[143:183].strip(),
        "Numero Remessa/retorno": linha[183:191],
        "Data de gravação": linha[191:199],
        "Data de Crédito": linha[199:207],
        "Exclusivo Febraban3": linha[207:240],
    }


def extrair_segmento_p(linha):
    return {
        "Código do Banco": linha[0:3],
        "Lote de Serviço": linha[3:7],
        "Tipo de Registro": linha[7:8],
        "Nº Sequencial do Registro": linha[8:13],
        "Código de Segmento": linha[13:14],
        "Exclusivo Febraban": linha[14:15],
        "Tipo de Movimento": linha[15:17], #01-entrada 02-baixa 04-abatimento 06-altera vencimento 09-protestar 10-sustar 12-alterar juros 45-negativação
        "Agencia da Conta": linha[17:22],
        "Digito Agenica": linha[22:23],
        "Número da Conta": linha[22:35],
        "DV Conta": linha[35:36],
        "DV Agência/Conta": linha[36:37],
        "Nosso Numero": linha[37:57], #20 posições
        "Código da Carteira": linha[57:58], #2- vinculada 4- descontada 7- simples 8- premio de seguro
        "Forma de Cadastramento": linha[58:59], #1- registrada 2- sem registro        
        "Tipo de Documento": linha[59:60],        
        "Identificação da emissão": linha[60:61],
        "Identificação da distribuição": linha[61:62].strip(), #1-banco 2-cliente 3-banco envia email P-registra com qrcode pix
        "Numero do documento de cobrança": linha[63:77].strip(),
        "Data de Vencimento": linha[77:85],
        "Valor Nominal": linha[85:100],
        "Agência Cobradora": linha[100:105],
        "Digito Agência Cobradora": linha[105:106],
        "Espécie do Título": linha[107:108],#02-Duplicata mercantilk 04-dup de serviço 20-apolice de seguro
        "Aceite": linha[108:109],#A-sim N-não
        "Data de Emissão": linha[109:117],
        "Código do Juros": linha[117:118],#1-valor por dia 2-taxa mensal 3-isento, pode pegar dados do banco
        "Data do Juros": linha[118:126],
        "Valor do Juros": linha[127:141],#sobrepoe a taxa cadastrada no banco / descontada: desconsidera essa juros e pega o da operação
        "Código de Desconto 1": linha[141:142],
        "Data do Desconto 1": linha[142:150],
        "Valor do Desconto 1": linha[150:165],
        "Valor do IOF": linha[165:180],#seguro premio
        "Valor do Abatimento": linha[181:195],
        "Identificação do Título na Empresa": linha[195:220].strip(), #seu numero
        "Código para Protesto": linha[220:221],#1-protestar dias corridos 2-protestar dias uteis 3-nao protestar / vinculada assumne 3 dias se nao informar
        "Dias para Protesto": linha[221:223],
        "Código para Baixa": linha[223:224],
        "Dias para Baixa": linha[224:227],#maximo 365. Se não informado pega o cadastrado no convenio
        "Código da Moeda": linha[227:229], #02-dolar 14-euro 00-real
        "Número do Contrato": linha[229:239],#não tratado pelo sistema
        "Uso Exclusivo FEBRABAN": linha[239:240]       
    }

def extrair_segmento_q(linha):
    return {
        "Código do Banco": linha[0:3],
        "Lote de Serviço": linha[3:7],
        "Tipo de Registro": linha[7:8],
        "Nº Sequencial do Registro": linha[8:13],
        "Código de Segmento": linha[13:14],
        "Uso Exclusivo FEBRABAN": linha[14:15],
        "Tipo de Inscrição Sacado": linha[17:18],
        "Número de Inscrição Sacado": linha[18:33],
        "Nome do Sacado": linha[34:73].strip(),
        "Endereço": linha[73:113].strip(),
        "Bairro": linha[113:128].strip(),
        "CEP": linha[128:133],
        "Sufixo do CEP": linha[134:136],
        "Cidade": linha[137:151].strip(),
        "UF": linha[151:153],
        "Tipo de Inscrição Sacador": linha[153:154],
        "Número de Inscrição Sacador": linha[154:169],
        "Nome do Sacador/Avalista": linha[169:209].strip(),
        "Cod Bco Corresp Compe": linha[209:212],
        "Nosso numero Bco correspondente": linha[212:232],
        "Uso Exclusivo FEBRABAN": linha[233:240].strip()
    }

def extrair_trailer_lote(linha):
    return {
        "Código do Banco": linha[0:3],
        "Lote de Serviço": linha[3:7],
        "Tipo de Registro": linha[7:8],
        "Uso Exclusivo FEBRABAN": linha[8:17],
        "Quantidade de Registros do Lote": linha[17:23],
        "Somatória dos Valores": linha[23:41],
        "Somatória de Quantidade de Moeda": linha[41:59],
        "Aviso aos Sacados": linha[59:60],
        "Uso Exclusivo FEBRABAN": linha[60:240].strip()
    }

def extrair_trailer_arquivo(linha):
    return {
        "Código do Banco": linha[0:3],
        "Lote de Serviço": linha[3:7],
        "Tipo de Registro": linha[7:8],
        "Uso Exclusivo FEBRABAN": linha[8:17],
        "Quantidade de Lotes": linha[17:23],
        "Quantidade de Registros": linha[23:29],
        "Qtde de Contas p conc lotes": linha[29:35],
        "Uso Exclusivo FEBRABAN": linha[35:240].strip()
    }


# === Interface ===
st.set_page_config(page_title="Conferidor CNAB240", layout="wide")

# Título principal
st.title("📄 Conferidor CNAB240")


# Lembretes úteis
with st.expander("📌 Lembretes para conferência"):
    st.markdown("""
    **🔄 Tipo de Movimento**  
    - `01` → Entrada  
    - `02` → Baixa  

    **💼 Código da Carteira**  
    - `2` → Vinculada  
    - `4` → Descontada  
    - `7` → Simples  
    - `8` → Prêmio de Seguro  

    **💰 Código de Juros**  
    - `1` → Valor por dia  
    - `2` → Taxa mensal  
    - `3` → Isento (pegar dados cadastrados do banco)

    **📣 Código de Protesto**  
    - `1` → Protestar dias corridos  
    - `2` → Protestar dias úteis  
    - `3` → Não protestar  
    """)

# Upload do arquivo .REM ou .TXT
uploaded_file = st.file_uploader("📤 Envie o arquivo CNAB240 (.REM ou .TXT)", type=["txt", "rem"])

if uploaded_file:
    linhas = uploaded_file.read().decode("utf-8").splitlines()

    # Inicializa listas
    header_arquivo = []
    segmentos_p = []

    # Processa cada linha
    for linha in linhas:
        if len(linha) < 240:
            linha = linha.ljust(240)

        tipo = linha[7:8]
        segmento = linha[13:14]

        if tipo == '0':
            header_arquivo.append(extrair_header_arquivo(linha))
        elif tipo == '3' and segmento == 'P':
            segmentos_p.append(extrair_segmento_p(linha))

    # Cria DataFrames
    df_header = pd.DataFrame(header_arquivo)
    df_segmento_p = pd.DataFrame(segmentos_p)

    # === Destaques ===
    st.subheader("🔍 Header do Arquivo")
    campos_header = [
        "Número do Convênio", "Carteira", "Variação da Carteira",
        "Agência", "DV Agência", "Conta", "DV Conta"
    ]
    st.dataframe(df_header[campos_header])

    st.subheader("📌 Segmento P - Títulos")
    campos_segmento_p = [
        "Nosso Numero", "Tipo de Movimento", "Código da Carteira", "Data de Vencimento",
        "Valor Nominal", "Código do Juros", "Data do Juros",
        "Valor do Juros", "Código para Protesto", "Dias para Protesto"
    ]
    st.dataframe(df_segmento_p[campos_segmento_p])

    # === Exporta Excel ===
    with pd.ExcelWriter("cnab240modelo_completo.xlsx", engine="openpyxl") as writer:
        df_header.to_excel(writer, sheet_name="Header", index=False)
        df_segmento_p.to_excel(writer, sheet_name="Segmento P", index=False)

    with open("cnab240modelo_completo.xlsx", "rb") as f:
        st.download_button(
            label="📥 Baixar Excel Final",
            data=f,
            file_name="cnab240modelo_completo.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )


#para rodar no terminal: streamlit run app.py --logger.level debug

st.markdown("""
<hr style="border:1px solid #ccc" />

<div style='text-align: center; font-size: 14px; color: gray;'>
    Desenvolvido por <strong> W.Teo </strong> · @ <a href='mailto:wesley.john@gmail.com'>wesley.john@gmail.com</a>
</div>
""", unsafe_allow_html=True)
