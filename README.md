# 🌸 Classificação de Flores Iris com Machine Learning

## 📌 Sobre o projeto

Este projeto foi desenvolvido como atividade prática da disciplina de Linguagem Python, do curso de Engenharia de Software.

O objetivo é construir, treinar e avaliar um modelo de Machine Learning capaz de classificar espécies de flores Iris com base em suas características físicas, utilizando Python, TensorFlow e técnicas de pré-processamento de dados.

O modelo utiliza uma rede neural artificial para identificar três espécies de flores: Iris setosa, Iris versicolor e Iris virginica.

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem de programação utilizada no desenvolvimento.
- **TensorFlow e Keras:** construção, treinamento e avaliação da rede neural.
- **Pandas:** organização e visualização dos dados.
- **NumPy:** manipulação de arrays e resultados das previsões.
- **Scikit-learn:** carregamento do conjunto de dados Iris, divisão dos dados e padronização.
- **VS Code:** ambiente de desenvolvimento.

## 📊 Conjunto de dados

Foi utilizado o conjunto de dados Iris, disponível na biblioteca Scikit-learn.

O dataset contém 150 amostras de flores, divididas entre três espécies. Cada amostra possui quatro características:

- Comprimento da sépala.
- Largura da sépala.
- Comprimento da pétala.
- Largura da pétala.

Essas características são utilizadas pelo modelo para aprender a identificar a espécie de cada flor.

## ⚙️ Etapas do desenvolvimento

### 1. Carregamento dos dados

O conjunto Iris é carregado por meio da função `load_iris()`. Os dados são organizados com Pandas para facilitar a visualização e a análise inicial.

### 2. Pré-processamento

Os dados são divididos em 80% para treinamento e 20% para teste, utilizando a função `train_test_split()`.

Em seguida, é aplicada a padronização com `StandardScaler()`, permitindo que as características sejam utilizadas em escalas comparáveis durante o treinamento.

### 3. Construção da rede neural

O modelo é construído com TensorFlow e Keras, utilizando a arquitetura Sequential.

A rede neural possui:

- Camada de entrada com quatro características.
- Primeira camada oculta com 16 neurônios e ativação ReLU.
- Segunda camada oculta com 8 neurônios e ativação ReLU.
- Camada de saída com 3 neurônios e ativação Softmax.

A camada de saída calcula as probabilidades associadas às três espécies de flores.

### 4. Treinamento

O modelo é compilado com o otimizador Adam, a função de perda Sparse Categorical Crossentropy e a métrica Accuracy.

O treinamento é realizado durante 100 épocas, com lotes de 16 amostras e separação de 20% dos dados de treinamento para validação.

### 5. Avaliação

Após o treinamento, o modelo é avaliado utilizando os dados de teste, que não foram utilizados para ajustar os parâmetros da rede neural.

A avaliação permite verificar a capacidade do modelo de classificar corretamente novas amostras.

### 6. Previsão

Por fim, o modelo recebe as medidas de uma nova flor, realiza a padronização e calcula as probabilidades de pertencimento a cada espécie.

A espécie com a maior probabilidade é apresentada como resultado da classificação.

## 📈 Resultados obtidos

Na execução do projeto, o modelo apresentou os seguintes resultados:

| Métrica | Resultado |
|---|---|
| Épocas de treinamento | 100 |
| Perda nos dados de teste | 0,1407 |
| Precisão nos dados de teste | 96,67% |
| Espécie prevista | Iris setosa |

A precisão de 96,67% demonstra que o modelo classificou corretamente 29 das 30 amostras utilizadas no teste.

Para a nova flor informada, o modelo identificou a espécie Iris setosa, com aproximadamente 99,93% de probabilidade.

Os resultados podem variar entre execuções devido à inicialização aleatória dos parâmetros da rede neural e ao processo de treinamento.

## 🚀 Como executar o projeto

**1. Clone o repositório:**

```bash
git clone URL_DO_SEU_REPOSITORIO
```

**2. Acesse a pasta do projeto:**

```bash
cd classificacao_iris
```

**3. Crie um ambiente virtual:**

```bash
python -m venv .venv
```

**4. Ative o ambiente virtual no Windows:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**5. Instale as dependências:**

```bash
python -m pip install tensorflow pandas numpy scikit-learn
```

**6. Execute o programa:**

```bash
python iris_modelo.py
```

Ao executar o programa, serão apresentados os dados iniciais do conjunto Iris, o processo de treinamento, a precisão obtida nos dados de teste e a previsão da espécie de uma nova flor.

## 🎯 Conclusão

O projeto permitiu aplicar conceitos fundamentais de Machine Learning, incluindo preparação de dados, construção de redes neurais, treinamento supervisionado, avaliação de desempenho e realização de previsões.

A utilização do TensorFlow em conjunto com o Scikit-learn demonstrou como modelos de inteligência artificial podem aprender padrões a partir de dados e realizar tarefas de classificação.

Os resultados obtidos mostram que a rede neural desenvolvida conseguiu identificar as espécies de flores Iris com boa precisão no conjunto de teste utilizado.

## 📚 Referências

- [TensorFlow — Documentação oficial](https://www.tensorflow.org/)
- [Scikit-learn — Documentação oficial](https://scikit-learn.org/)
- [Python — Documentação oficial](https://docs.python.org/3/)
- [Pandas — Documentação oficial](https://pandas.pydata.org/)
