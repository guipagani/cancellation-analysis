import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

class Plot:
    def plot_histogram(self, data, colunas, target):  
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
    
    def plot_heatmap(self, data):
        plt.figure(figsize=(12, 8))

        sns.heatmap(data.corr(), annot=True, cmap='RdBu', fmt='.2f')
        plt.title('Influência das Variáveis no Cancelamento')

        plt.show()

    # add plot stacked bar
    