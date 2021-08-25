from re import T
import streamlit as st
import numpy as np
import pandas as pd
import base64
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
from computer.data_process import *
#from computer.data_front import *
from computer.funcomputer import *
import time

st.image('imagem.png')

# Titulo
#st.write('### 💾 Dados extraídos de:',data_inicial,"  a",data_final)



st.image('imagem2.png')
st.write('### 💾 Dados extraídos de:',data_inicial,"  até",data_final)
# Side bar
## Imagem na side bar
image = Image.open('[LOGO] Eduqo.png')
st.sidebar.image(image,caption='Eduqo - Plataforma QMágico',use_column_width=True)

st.sidebar.markdown('Feito por: Gabriel Philot (Tio Gibbs)')
st.sidebar.write('#### Links associados com o projeto')
st.sidebar.write('####')
st.sidebar.write("##### [Github](https://github.com/GabrielMPhilot/categorias_premiadas)")
st.sidebar.write('####')
st.sidebar.write("##### [G.Slides](https://docs.google.com/presentation/d/1hSyXkuVwCf6QhHEPrmEeFrLOoDUxYwiqK0h_4Ck_azE/edit#slide=id.gacf8bfa375_1_201)")
st.sidebar.write('#')
#st.sidebar.write('#### Resultado da classificação de nosso modelo:',get_table_download_link(lista_resul), unsafe_allow_html=True)



"""

"""


# Categoria 1
# Média de conteúdos estudados caderno

"""
## Categoria 1
### 👩🏽‍🎓 Escola com maior engajamento de alunos
"""
"""

"""
"""
#### 📚 Média de conteúdos estudados (caderno)
"""

"""

"""
expander_cont = st.expander(" (Top 20)  -> (clique aqui 🖱️)")
expander_cont.table(cat_01_m01top20)
expander_cont = st.expander(" Toda a tabela  -> (clique aqui 🖱️)")
expander_cont.dataframe(cat_01_m01)
#st.table(cat_01_m01)

"""
#### 📝 Média de exercícios realizados (A.As e S.Exer)
"""

"""

"""

expander_cont = st.expander(" (Top 20)  -> (clique aqui 🖱️)")
expander_cont.table(cat_01_m02top20)
expander_cont = st.expander(" Toda a tabela  -> (clique aqui 🖱️)")
expander_cont.dataframe(cat_01_m02)

#st.table(cat_01_m02)

"""
#### ⏱️ Tempo médio de estudo (caderno)
"""

"""

"""
expander_cont = st.expander(" (Top 20)  -> (clique aqui 🖱️)")
expander_cont.table(cat_01_m03top20)
expander_cont = st.expander(" Toda a tabela  -> (clique aqui 🖱️)")
expander_cont.dataframe(cat_01_m03)

#st.table(cat_01_m03)

"""
## Categoria 2
### 🏫 Escola com maior engajamento de professores
"""
"""

"""

"""
#### 📝 Média de exercícios selecionados, curados ou criados
"""

"""

"""
expander_cont = st.expander(" (Top 20)  -> (clique aqui 🖱️)")
expander_cont.table(cat02m1top20)
expander_cont = st.expander(" Toda a tabela  -> (clique aqui 🖱️)")
expander_cont.dataframe(cat02m1)

"""
#### Obs sobre esse parâmetro: 
Foi visualizado que esse parâmetro tem um certo problema, escolas como por exemplo:
fundacaobradesco e outras tem poucos professores, baixo engajamento de alunos, sobem um monte de questões que nem
são respondidas durante um bom tempo, para contornar essa pontuação criamos um paramêtro (**Sugestão Data Science**) que envolve criação de exercícios
e a utilização o tempo de correção do segundo parâmetro, assim buscando mediar a criação versus a utilização.
"""
#cat02m1top20
 
#  Tempo economizado com correções automáticas
"""
#### ⏳ Tempo economizado com correções automáticas
"""

"""

"""
expander_cont = st.expander(" (Top 20)  -> (clique aqui 🖱️)")
expander_cont.table(cat02m2top20)
expander_cont = st.expander(" Toda a tabela  -> (clique aqui 🖱️)")
expander_cont.dataframe(cat02m2)
#cat02m2
#cat02m2top20
"""
#### 👩‍💻 Sugestão Data Science 
"""

"""

"""
expander_cont = st.expander(" (Top 20)  -> (clique aqui 🖱️)")
expander_cont.table(cat02m3top20)
expander_cont = st.expander(" Toda a tabela  -> (clique aqui 🖱️)")
expander_cont.dataframe(cat02m3)
# Sugestão Data Science 
#cat02m3
#cat02m3top20

"""
## Categoria 3
### 💻 Escola com maior eficiência digital
"""

"""

"""

"""
#### ⏳ Economia de tempo
Tempo desde imprimir a folha até o final do fluxo da mesma (estimativa 5s por folha)

"""

expander_cont = st.expander(" (Top 20)  -> (clique aqui 🖱️)")
expander_cont.table(cat03m1top20)
expander_cont = st.expander(" Toda a tabela  -> (clique aqui 🖱️)")
expander_cont.dataframe(cat03m1)
#cat03m1
#cat03m1top20

"""
#### 🌴 Economia de papel (N° folhas)


"""
"""

"""
expander_cont = st.expander(" (Top 20)  -> (clique aqui 🖱️)")
expander_cont.table(cat03m2top20)
expander_cont = st.expander(" Toda a tabela  -> (clique aqui 🖱️)")
expander_cont.dataframe(cat03m2)
#cat03m2
#cat03m2top20 
"""
#### 💰 Economia de dinheiro (reais->estimativa 10centavos p/folha)


"""
"""

"""
expander_cont = st.expander(" (Top 20)  -> (clique aqui 🖱️)")
expander_cont.table(cat03m3top20)
expander_cont = st.expander(" Toda a tabela  -> (clique aqui 🖱️)")
expander_cont.dataframe(cat03m3)
#cat03m3
#cat03m3top20
"""
#### 📁 Número de exercícios selecionados do banco


"""
"""

"""
expander_cont = st.expander(" (Top 20)  -> (clique aqui 🖱️)")
expander_cont.table(cat03m4top20)
expander_cont = st.expander(" Toda a tabela  -> (clique aqui 🖱️)")
expander_cont.dataframe(cat03m4)
#cat03m4
#cat03m4top20
"""
#### 🤖 Número de questões corrigidas automaticamente


"""
"""

"""
expander_cont = st.expander(" (Top 20)  -> (clique aqui 🖱️)")
expander_cont.table(cat03m5top20)
expander_cont = st.expander(" Toda a tabela  -> (clique aqui 🖱️)")
expander_cont.dataframe(cat03m5)
#cat03m5
#cat03m5top20


"""
## Categoria 4
### 👩🏾‍🏫 Professores mais engajados
"""

"""

"""

"""
#### ✍️ Média de exercícios selecionados, curados ou criados por mês

"""
"""

"""

expander_cont = st.expander(" (Top 20)  -> (clique aqui 🖱️)")
expander_cont.table(catego4m01top20)
expander_cont = st.expander(" Toda a tabela  -> (clique aqui 🖱️)")
expander_cont.dataframe(catego4m01)
#catego4m01
#catego4m01top20
"""
#### 📚 Média de  conteúdos, curados ou criados por mês


"""
"""

"""
expander_cont = st.expander(" (Top 20)  -> (clique aqui 🖱️)")
expander_cont.table(catego4m02top20)
expander_cont = st.expander(" Toda a tabela  -> (clique aqui 🖱️)")
expander_cont.dataframe(catego4m02)
#catego4m02
#catego4m02top20
"""
#### 💎 Variação de conteúdos (Cadernos)


"""
"""

"""
expander_cont = st.expander(" (Top 20)  -> (clique aqui 🖱️)")
expander_cont.table(catego4m03top20)
expander_cont = st.expander(" Toda a tabela  -> (clique aqui 🖱️)")
expander_cont.dataframe(catego4m03)
#catego4m03
#catego4m03top20
"""
#### 💬 Interação com alunos


"""
"""

"""
expander_cont = st.expander(" (Top 20)  -> (clique aqui 🖱️)")
expander_cont.table(catego4m04top20)
expander_cont = st.expander(" Toda a tabela  -> (clique aqui 🖱️)")
expander_cont.dataframe(catego4m04)
#catego4m04
#catego4m04top20
