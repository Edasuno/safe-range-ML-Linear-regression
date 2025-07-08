import streamlit as st
import numpy as np
from joblib import load
from math import ceil 

modelo = load('./model_range.joblib')

fator_seguranca = 0.85 #85% para considerar margens de erro

def calculoautonomia(distancia_total , battery_capacity):
    entrada = np.array([[battery_capacity]]) #Reshape pra os dados entrar iguais quando criado o modelo 
    autonomia_prevista = modelo.predict(entrada)[0] #Retornar um array então acessando o index 0 
    total_seg = autonomia_prevista * fator_seguranca
    postos_necessarios = ceil(distancia_total / total_seg)

    return postos_necessarios


st.title('SafeRange')

st.caption("Calculando quantas paradas em postos de carregamento vão ser necessárias para sua viagem")


distancia_total  = st.number_input('Digite a distância em Km que você irá percorrer', min_value=0.0)

st.caption("Caso não saiba a distância do trajeto use a opção abaixo para verificar")

st.write("[Abrir Google Maps](https://www.google.com/maps/dir/)")


battery_capacity = st.number_input('Capacidade da bateria (kWh)', max_value=500.0, min_value=10.0 )


if st.button("Calcular"):
    postos = calculoautonomia(distancia_total, battery_capacity)
    if distancia_total <= 20:
        st.markdown(
    '<p style="color:#38b000; font-size:24px; font-weight:bold;">Fique tranquilo(a), a distância é curta. Não será necessário parar para recarregar!</p>',
    unsafe_allow_html=True
)
    else: 
        st.markdown(f'<p style="color:#38b000; font-size:24px; font-weight:bold;">É estimado um total de {postos} paradas para recarregar durante a viagem.</p>', unsafe_allow_html=True)


st.markdown("---")

st.markdown('<p style="text-align: center; font-weight: bold;  "> FAQ </p>', unsafe_allow_html=True)

with st.expander("Como a aplicação funciona?"):
    st.write("Funciona a partir de um modelo de aprendizado de máquina (Regressão Linear) e um cálculo para a quantidade de paradas para recarregar.")

with st.expander("Por que a aplicação não calcula a distância entre duas cidades?"):
    st.write("Optei por não incluir o uso de API na demonstração por motivos de segurança e praticidade assim evitando quebrar o limite gratuito, evitando possível vazamento da chave e ainda mantendo o projeto funcional em deploy público.")
 
with st.expander("Qual é a precisão da estimativa de paradas? Eu posso confiar?"):
    st.write("O modelo de regressão linear foi treinado com dados reais de veículos elétricos e atingiu um coeficiente de determinação (R²) de **0,80**. Isso significa que ele explica cerca de **80% da variação** nos dados de autonomia com base na capacidade da bateria. Outros fatores como relevo, temperatura e estilo de direção também afetam a autonomia por isso a aplicação usa uma margem de segurança que garante uma maior confiabilidade.")


with st.expander("É possível usar o modelo em outras aplicações?"):
    st.write("Sim! É totalmente possível utilizar um modelo de aprendizado de máquina em uma API para seu projeto e integrar com outras aplicações Web, mobile e desktop.")