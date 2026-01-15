# Análise de Cancelamento de Planos

## Descrição do Projeto

Este projeto consiste numa análise de dados focada em compreender os motivos de cancelamento de planos de uma empresa. O objetivo é identificar padrões de comportamento dos clientes e gerar *insights* para estratégias de retenção. A gestão do projeto, dependências e ambiente virtual é realizada integralmente com o uv, garantindo rapidez e reprodutibilidade. 

O projeto foi proposto pela **jornada python**, semana de aprendizado realizado pela escola online de programação brasileira **Hashtag Programação**. 

🔗 Referência: [https://www.youtube.com/watch?v=0c2AfijcWb0]

---

## Tecnologias e Dependências

* **Linguagem:** Python 3.13+
* **Gerenciador de Ambiente:** `uv`

* **Bibliotecas:**

  * `Pandas` (leitura e tratamento de DataFrames)
  * `Matplotlib` (visualização da base de dados)

---

## Estrutura de Diretórios

A organização do projeto segue a estrutura detectada no ambiente de desenvolvimento:

```plaintext
cancellation-analysis/
├── .venv/               # ambiente de execução gerenciado pelo uv
├── data/
│   ├── raw/             # Coloque aqui o CSV original do Google Drive (ex: cancelamentos.csv)
│   └── processed/       # Para salvar dados limpos/tratados futuramente
├── notebooks/           # Relatório em Jupyter Notebook
├── src/                 # Scripts Python com funções reutilizáveis
├── pyproject.toml       # dependências
├── uv.lock              # versões exatas
└── README.md            # Documentação do projeto
```

---


## Procedimentos de Configuração (Ambiente `uv`)

### Instalação e Sincronização

Para preparar o ambiente e instalar as dependências declaradas no `pyproject.toml`:

```bash
uv sync
```
