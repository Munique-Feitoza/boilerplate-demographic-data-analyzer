# Demographic Data Analyzer

Este projeto analisa dados demográficos com base no censo de 1994, utilizando a biblioteca Pandas em Python. Ele faz parte do curso de **Análise de Dados com Python** da [freeCodeCamp](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/demographic-data-analyzer).

## 📊 Objetivo

Responder a perguntas estatísticas sobre os dados demográficos, como:

- Quantas pessoas de cada raça estão representadas no conjunto de dados?
- Qual é a idade média dos homens?
- Qual porcentagem das pessoas possui diploma de Bacharelado?
- Qual porcentagem de pessoas com ou sem ensino superior ganha mais de 50K?
- Qual é o número mínimo de horas que uma pessoa trabalha por semana?
- Qual o país com a maior porcentagem de pessoas que ganham mais de 50K?
- Qual a ocupação mais comum entre os que ganham mais de 50K na Índia?

## 📁 Estrutura do Projeto

```
📦 demographic-data-analyzer/
├── demographic_data_analyzer.py   # Arquivo principal com os cálculos
├── main.py                        # Script de teste
├── test_module.py                 # Testes unitários
├── adult.data.csv                 # Conjunto de dados
└── README.md                      # Este arquivo
```

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone <url-do-seu-repositório>
   cd demographic-data-analyzer
   ```

2. Instale as dependências (se necessário):
   ```bash
   pip install pandas
   ```

3. Execute o script de teste:
   ```bash
   python main.py
   ```

## ✅ Requisitos

- Python 3.x
- pandas

## 🧪 Testes

Os testes são executados automaticamente ao rodar o `main.py`, que importa as funções de `test_module.py`.

## 📚 Fonte dos Dados

Dua, D. e Graff, C. (2019). UCI Machine Learning Repository. Irvine, CA: University of California, School of Information and Computer Science.

---

Projeto baseado no curso gratuito da [freeCodeCamp](https://www.freecodecamp.org/).
