# Análise de Vendas – Zé Pequeno Paçocas e Rolhas Ltda

Mini projeto de análise exploratória de dados em Python com Pandas aplicada a uma base de dados de varejo.

Este projeto tem por objetivo analisar uma base de dados com registros reais de compras (datas, clientes, produtos, categorias e valores)

# Objetivos

- Realizar a análise exploratória da base de dados “Varejo” que contém registros reais de compras (datas, clientes, produtos, categorias e valores). 
- Verificar a qualidade, realizar a limpeza e sumarizar os dados. 
- Identificar problemas nos dados, como valores nulos, tipos incorretos e duplicados.
- Realizar o tratamento dos dados com Pandas 
- Gerar estatísticas simples e funções de agrupamento para responder às perguntas operacionais 

---

## Perguntas a serem respondidas

1. Quem compra mais?
2. Quais categorias de produtos vendem mais?
3. Como as vendas variam ao longo do tempo?

---

## Fonte de dados

Os dados foram obtidos a partir da tabela de vendas `BaseVarejoDadosBrutos.csv` contendo 830 mil registros iniciais.

---

## Dicionário de dados

1. DATA: Data da compra; 
2. CO_ID: Identificação do número de compra (número da nota fiscal); 
3. CL_ID: Identificação do cliente (número do cliente); 
4. CL_GENERO: Sexo biológico informado pelo cliente; 
5. CL_EC: Estado civil do cliente: 1: Casado ou união estával; 2: Divorciado; 3: Separado; 4: Solteiro; 
5: Viúvo. 
6. CL_FHL: Número de filhos do cliente; 
7. CL_SEG: Segmentação econômica do cliente (classe A, B ou C); 
8. PR_ID: Código do produto (SKU) adquirido; 
9. PR_CAT: Categoria do produto adquirido; 
10. PR_NOME: Nome do produto adquirido. 

---

## Ferramentas e tecnologias utilizadas

- Visual Studio Code
- Python
- Pandas

---

## Metodologias de análise aplicadas

SALSAÇSLAÇDALÇSD

---

## Resultados e conclusões

KAJSKADLSKDLAKDAL



---

## Estrutura do repositório

```
├── README.MD                        
├── analise_vendas.py                        # script em python com as análises
├── funcoes.py                               # função auxiliar calcular_receita()
├── tabela_vendas_ZePequeno_limpa.csv        # dados de vendas (já tratados)
├── tabela_vendas_ZePequeno_original.xlsx    # dados de vendas brutos(sem tratamento)
└── tratamento_dados.py                      # script em python com as transformações aplicadas aos dados
```
---

## Como executar

1. Instale o Python 3.12 ou superior e o pandas:
```bash
   pip install pandas
```
2. Deixe todos os arquivos na mesma pasta.
3. Rode o script:
```bash
   python analise_vendas.py
```