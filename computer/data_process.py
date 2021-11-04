# Aqui iremos receber / unir os dataframes, fazer copias para front
# e fazer alguns ajustes nos dataframes

import numpy as np
import pandas as pd

from computer.funcomputer import *

# Intervalo de datas
datas=pd.read_csv("./csvs/interval_datas.csv")
del datas['Unnamed: 0']
datas=datas.replace(np.inf, 0)
datas_list=datas["0"].tolist()
data_inicial = datas_list[0]
data_final = datas_list[1]

# Recebendo as Tabelas e dataframes independentes (caso da tabela da categoria 4)

t_catego_01=pd.read_csv("./csvs/tab_01.csv")
del t_catego_01['Unnamed: 0']
t_catego_01=t_catego_01.replace(np.inf, 0)

t_catego_02=pd.read_csv("./csvs/tab_02.csv")
del t_catego_02['Unnamed: 0']
t_catego_02=t_catego_02.replace(np.inf, 0)

t_catego_03=pd.read_csv("./csvs/tab_03.csv")
del t_catego_03['Unnamed: 0']
t_catego_03=t_catego_03.replace(np.inf, 0)
# N° questões -> Número de questões corrigidas automaticamente
# created -> Número de exércicios selecionados do banco

# Tabela categoria 4 

# media_mes_questoes
t_catego_04_01=pd.read_csv("./csvs/media_mes_questoes.csv")
del t_catego_04_01['Unnamed: 0']
t_catego_04_01=t_catego_04_01.replace(np.inf, 0)

# conteudos_media_mes
t_catego_04_02=pd.read_csv("./csvs/conteudos_media_mes.csv")
del t_catego_04_02['Unnamed: 0']
t_catego_04_02=t_catego_04_02.replace(np.inf, 0)

# variacao_conteudos
t_catego_04_03=pd.read_csv("./csvs/variacao_conteudos.csv")
del t_catego_04_03['Unnamed: 0']
t_catego_04_03=t_catego_04_03.replace(np.inf, 0)

# interacoes_alunos
t_catego_04_04=pd.read_csv("./csvs/interacoes_alunos.csv")
del t_catego_04_04['Unnamed: 0']
t_catego_04_04=t_catego_04_04.replace(np.inf, 0)
# type-> Interações com alunos


# Retirando/ordenando/arrumando métricas

### Categoria 1

# Média de conteúdos estudados
var_01=t_catego_01.columns.values.tolist()
cat_01_m01=t_catego_01.iloc[:,:2]
cat_01_m01[var_01[1]]=((cat_01_m01[var_01[1]]).astype(float)).round(2)
cat_01_m01=cat_01_m01.sort_values(var_01[1], ascending=False, inplace=False).reset_index(drop=True)
cat_01_m01top20=cat_01_m01.head(20).reset_index(drop=True)

# média de exercícios realizados
cat_01_m02 = reorder_columns(t_catego_01, var_01[2], 1).iloc[:,:2]
cat_01_m02 = cat_01_m02.sort_values(var_01[2], ascending=False, inplace=False).reset_index(drop=True)
cat_01_m02top20 = cat_01_m02.head(20).reset_index(drop=True)

# Tempo médio de estudo caderno
cat_01_m03 = reorder_columns(t_catego_01, var_01[3], 1).iloc[:,:2]
cat_01_m03[var_01[3]]=(cat_01_m03[var_01[3]]/3600).round(2)
cat_01_m03 = cat_01_m03.sort_values(var_01[3], ascending=False, inplace=False).reset_index(drop=True)
cat_01_m03top20 = cat_01_m03.head(20).reset_index(drop=True)

### Categoria 2

catego2 = t_catego_02.copy()
var_aux_02= t_catego_02.columns.values.tolist()
catego2["M.Ex * Tempo"]=(catego2[var_aux_02[1]]*catego2[var_aux_02[2]]).round(2)
var_02 = catego2.columns.values.tolist()

#  Média de exercícios selecionados, curados ou criados
cat02m1 = catego2.iloc[:,:2]
cat02m1 = cat02m1.sort_values(var_02[1], ascending=False, inplace=False).reset_index(drop=True)
cat02m1top20= cat02m1.head(20).reset_index(drop=True)

#  Tempo economizado com correções automáticas
cat02m2 = reorder_columns(catego2, var_02[2],1).iloc[:,:2]
cat02m2 = cat02m2.sort_values(var_02[2], ascending=False, inplace=False).reset_index(drop=True)
cat02m2top20 = cat02m2.head(20).reset_index(drop=True)

# Sugestão Data Science 
cat02m3 = reorder_columns(catego2, var_02[3], 1).iloc[:,:2]
cat02m3 = cat02m3.sort_values(var_02[3], ascending=False, inplace=False).reset_index(drop=True)
cat02m3top20= cat02m3.head(20).reset_index(drop=True)

### Categoria 3
var_03=t_catego_03.columns.values.tolist()

# Economia de tempo
cat03m1 = reorder_columns(t_catego_03, var_03[1],1).iloc[:,:2]
cat03m1 = cat03m1.sort_values(var_03[1], ascending=False, inplace=False).reset_index(drop=True)
cat03m1top20 = cat03m1.head(20).reset_index(drop=True)

# Economia de papel
cat03m2 = reorder_columns(t_catego_03, var_03[2],1).iloc[:,:2]
cat03m2 = cat03m2.sort_values(var_03[2], ascending=False, inplace=False).reset_index(drop=True)
cat03m2top20 = cat03m2.head(20).reset_index(drop=True)

# Economia de dinheiro
cat03m3 = reorder_columns(t_catego_03, var_03[3],1).iloc[:,:2]
cat03m3 = cat03m3.sort_values(var_03[3], ascending=False, inplace=False).reset_index(drop=True)
cat03m3top20 = cat03m3.head(20).reset_index(drop=True)

# Número de exercícios selecionados do banco
cat03m4 = reorder_columns(t_catego_03, var_03[5],1).iloc[:,:2]
cat03m4 = cat03m4.rename(columns={var_03[5]: "N° de questões do Banco"}).reset_index(drop=True)
cat03m4 = cat03m4.sort_values("N° de questões do Banco", ascending=False, inplace=False).reset_index(drop=True)
cat03m4top20 = cat03m4.head(20).reset_index(drop=True)

# Número de questões corrigidas automaticamente
cat03m5 = reorder_columns(t_catego_03, var_03[4],1).iloc[:,:2]
cat03m5 = cat03m5.rename(columns={var_03[4]: "N° de questoes corrigidas auto"}).reset_index(drop=True)
cat03m5 = cat03m5.sort_values("N° de questoes corrigidas auto", ascending=False, inplace=False).reset_index(drop=True)
cat03m5top20 = cat03m5.head(20).reset_index(drop=True)


### Categoria 4


# Média de exercícios selecionados, curados ou criados por mês
catego4m01=t_catego_04_01.copy()
var_04_01 = catego4m01.columns.values.tolist()
catego4m01 = catego4m01.sort_values(var_04_01[2], ascending=False, inplace=False).reset_index(drop=True)
catego4m01top20  = catego4m01.head(20).reset_index(drop=True)

# Média de  conteúdos, curados ou criados por mês
catego4m02 = t_catego_04_02.copy()
var_04_02 = catego4m02.columns.values.tolist()
catego4m02 = catego4m02.sort_values(var_04_02[2], ascending=False, inplace=False).reset_index(drop=True)
catego4m02top20 = catego4m02.head(20).reset_index(drop=True)

# Variação de conteúdos
catego4m03 = t_catego_04_03.copy()
var_04_03 = catego4m03.columns.values.tolist()
catego4m03 = catego4m03.sort_values(var_04_03[2], ascending=False, inplace=False).reset_index(drop=True)
catego4m03top20 = catego4m03.head(20).reset_index(drop=True)


# Interação com alunos
catego4m04 = t_catego_04_04.copy()
var_04_04 = catego4m04.columns.values.tolist()
catego4m04 = catego4m04.rename(columns={var_04_04[2]: "N° de Interações com alunos"}).reset_index(drop=True)
catego4m04 = catego4m04.sort_values("N° de Interações com alunos", ascending=False, inplace=False).reset_index(drop=True)
catego4m04top20 = catego4m04.head(20).reset_index(drop=True)


