import streamlit as st
import pandas as pd

# Carregar os dados
data = pd.read_csv('Previsor-Precos-Pilates/precos-pilates.csv')

# Função para calcular o preço baseado nas regras
def calcular_preco(modalidade, horario, dias_semana, plano, forma_pagamento):
    filtro = (data['modalidade'] == modalidade) & \
             (data['horario'] == horario) & \
             (data['dias_semana'] == str(dias_semana)) & \
             (data['plano'] == plano) & \
             (data['forma_pagamento'] == forma_pagamento)
    
    preco = data[filtro]['preco']
    
    if not preco.empty:
        return preco.values[0]
    else:
        return 'Preço não encontrado para as combinações fornecidas'

# Função para calcular o preço avulso
def calcular_preco_avulso(modalidade, horario):
    filtro = (data['modalidade'] == modalidade) & \
             (data['horario'] == horario) & \
             (data['dias_semana'] == 'avulso') & \
             (data['plano'] == 'avulso') & \
             (data['forma_pagamento'] == 'À vista')
    
    preco = data[filtro]['preco']
    
    if not preco.empty:
        return preco.values[0]
    else:
        return 'Preço avulso não encontrado para as combinações fornecidas'

# Configurar a interface do usuário com Streamlit
st.set_page_config(page_title="Previsor de Preços de Pilates", page_icon=":guardsman:", layout="centered")

# Adicionar CSS personalizado
st.markdown(
    """
    <style>
    .main {
        background-color: #f5e0e3;
    }
    .sidebar .sidebar-content {
        background-color: #6f1f3c;
    }
    .css-18e3th9 {
        color: #6f1f3c;
        font-size: 50px;
    }
    .css-1v3fvcr {
        color: #6f1f3c;
        font-size: 50px;
    }
    .stSelectbox > div > div > div {
        background-color: #6f1f3c;
        color: #f5e0e3;
    }

    </style>
    """,
    unsafe_allow_html=True
)




st.title('Previsor de Preços de Pilates')

# Pergunta sobre valor avulso
valor_avulso = st.radio(
    'Você deseja um valor avulso?', 
    ['Não', 'Sim'],
)

if valor_avulso == 'Sim':
    # Exibir perguntas adicionais para valor avulso
    st.write("Para valores avulsos, por favor, forneça mais informações:")
    modalidade = st.selectbox(
        'Qual a modalidade?', 
        ['presencial', 'online'],
        format_func=lambda x: x.capitalize()
    )
    horario = st.selectbox(
        'Qual horário?', 
        ['manhã', 'tarde', 'noite'],
        format_func=lambda x: x.capitalize()
    )
    # Verificar se existe um preço avulso no CSV para a combinação fornecida
    preco = calcular_preco_avulso(modalidade, horario)
else:
    # Perguntas para valor normal
    modalidade = st.selectbox(
        'Qual a modalidade?', 
        ['presencial', 'online'],
        format_func=lambda x: x.capitalize()
    )
    horario = st.selectbox(
        'Qual horário?', 
        ['manhã', 'tarde', 'noite'],
        format_func=lambda x: x.capitalize()
    )
    dias_semana = st.slider(
        'Quantos dias na semana?', 
        1, 3, 1
    )
    plano = st.selectbox(
        'Qual o plano?', 
        ['mensal', 'trimestral', 'semestral'],
        format_func=lambda x: x.capitalize()
    )
    pagamento = st.selectbox(
        'Qual forma de pagamento?', 
        ['À vista', 'cartão'],
        format_func=lambda x: x.capitalize()
    )
    preco = calcular_preco(modalidade, horario, dias_semana, plano, pagamento)

# Mostrar o preço calculado
st.write(f'O preço estimado é: R${preco}')

# Adicionar logo da marca
st.image("Previsor-Precos-Pilates/logo.png", width=250)  

# Configurar o título e o ícone da página
st.set_page_config(
    page_title="Previsor de Preços de Pilates",  # Título da página
    page_icon="🧘‍♂️",  # Emoji ou imagem para o ícone
)
