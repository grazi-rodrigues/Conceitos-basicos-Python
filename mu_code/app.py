# Importando as bibliotecas

import streamlit as st
import pandas as pd

# Importando apenas a biblioteca express (mais rápida), que permite faça as coisas mais simplificada
import plotly.express as px

# Método set_page_config para configuração de layout

st.set_page_config(layout="wide")

# Criando as váriaveis e buscando os arquivos com o método read_csv

df_reviews = pd.read_csv("datasets\customer reviews.csv")
df_top100_books = pd.read_csv("datasets\Top-100 Trending Books.csv")

# Criando o primeiro componente
# Método .max() busca todos os valores da coluna e devolve apenas um único valor

price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

# st.sidebar = adiciona o componete a esquerda

max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)

# Passando uma condição para ele filtrar
# E "[]" vai permitir que ele aplique o filtro, dateframe final

df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books # Chamando a váriavel para o streamlit entender que precisa print na tela

# Criando Gráficos

fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

# Função st.columns() devolve duas váriaies ao mesmo tempo

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
