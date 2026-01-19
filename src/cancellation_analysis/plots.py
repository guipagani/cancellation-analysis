"""
Módulo de Visualização de Dados.

Este módulo fornece ferramentas gráficas para análise exploratória de dados (EDA),
utilizando bibliotecas de  visualização para identificar padrões de cancelamento 
e correlações entre variáveis.
"""

from typing import List
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Plot:
    """
    Classe responsável pela geração de gráficos analíticos.

    Esta classe encapsula lógicas de visualização utilizando Plotly, 
    Seaborn e Matplotlib.
    """

    def plot_histogram(self, data: pd.DataFrame, colunas: List[str], target: str) -> None:
        """
        Gera histogramas comparativos para variáveis categóricas ou numéricas.

        Args:
            data (pd.DataFrame): O DataFrame contendo os dados.
            colunas (List[str]): Lista de nomes das colunas para gerar os gráficos.
            target (str): Variável alvo para segmentação de cores (ex: 'cancelou').
        """
        for coluna in colunas:
            fig = px.histogram(
                data,
                x=coluna,
                color=target,
                barmode='group',
                text_auto=True,
                title=f'Impacto de {coluna} no Cancelamento',
                color_discrete_map={0: 'blue', 1: 'red'}
            )
     
            fig.update_layout(yaxis_title="Quantidade de Clientes")
            fig.show()
   
    def plot_heatmap(self, data: pd.DataFrame) -> None:
        """
        Gera um mapa de calor (Heatmap) de correlação entre variáveis.

        Args:
            data (pd.DataFrame): O DataFrame contendo apenas variáveis numéricas.
        """
        plt.figure(figsize=(12, 8))
        sns.heatmap(data.corr(), annot=True, cmap='RdBu', fmt='.2f')
        plt.title('Influência das Variáveis no Cancelamento')
        plt.show()

    def plot_stacked_bar(self, data: pd.DataFrame, colunas: List[str], target: str) -> None:
        """
        Gera gráficos de barras empilhadas mostrando a proporção percentual.

        Args:
            data (pd.DataFrame): O DataFrame contendo os dados.
            colunas (List[str]): Colunas críticas para análise de porcentagem.
            target (str): Variável de status (ex: 'cancelou').
        """
        for coluna in colunas:
            df_temp = data.groupby([coluna, target]).size().reset_index(name='contagem')
            
            df_temp['porcentagem'] = (
                df_temp.groupby(coluna)['contagem']
                .transform(lambda x: (x / x.sum()) * 100)
            )

            fig = px.bar(
                df_temp,
                x=coluna,
                y='porcentagem',
                color=target,
                title=f'Porcentagem de Cancelamento por {coluna}',
                text=df_temp['porcentagem'].apply(lambda x: f'{x:.1f}%'),
                barmode='stack',
                color_discrete_map={'0': 'blue', '1': 'red', 0: 'blue', 1: 'red'}
            )
            
            fig.update_layout(
                yaxis_range=[0, 100], 
                yaxis_title="Porcentagem (%)",
                xaxis_title=coluna.capitalize()
            )
            fig.show()
