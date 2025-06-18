# Communication JS to Py

## Introdução / Introduction

### 🇧🇷 Português

Este projeto integra **Node.js** com **Python** para simular a **probabilidade de conversão (prospecção) de um lead**, com base em **quatro interações** classificadas como: `good` (bom), `neutral` (neutro) ou `bad` (ruim).

A integração entre as tecnologias é realizada por meio do módulo `child_process` do Node.js, que permite a execução de scripts Python diretamente do ambiente JavaScript. Essa abordagem evita a reimplementação de soluções já consolidadas em Python, promovendo maior eficiência e reaproveitamento de código.

No lado Python, é utilizada a biblioteca **scikit-learn (sklearn)** com um modelo de **regressão logística**, que aplica técnicas de **machine learning** para calcular a probabilidade de um cliente vir a converter com base nas interações analisadas.

#### Benefícios

- ✅ Reutilização de modelos e algoritmos já existentes em Python  
- 🔁 Integração eficiente entre tecnologias distintas  
- 🧪 Exemplo prático de interoperabilidade entre Node.js e Python usando processos filhos

### 🌐 English

This project integrates **Node.js** with **Python** to simulate the **conversion probability (prospecting) of a lead**, based on **four interactions** classified as: `good`, `neutral`, or `bad`.

The integration between the technologies is done using Node.js’s `child_process` module, which allows Python scripts to be executed directly from the JavaScript environment. This approach avoids reimplementing well-established solutions in Python, promoting greater efficiency and code reuse.

On the Python side, the **scikit-learn (sklearn)** library is used with a **logistic regression** model, which applies **machine learning** techniques to calculate the probability of a lead converting based on the analyzed interactions.

#### Benefits

- ✅ Reuse of existing models and algorithms implemented in Python  
- 🔁 Efficient integration between distinct technologies  
- 🧪 Practical example of interoperability between Node.js and Python using child processes


---

## 🧠 Tecnologias e Conceitos Utilizados

- **`spawn` do módulo `child_process`**: Utiliza-se o método `spawn` do módulo `child_process` do Node.js para executar scripts Python como subprocessos. Esse método permite passar comandos e argumentos diretamente pela linha de comando, facilitando a integração entre linguagens.

- **Python e scikit-learn**: O Python é uma linguagem amplamente utilizada em ciência de dados e machine learning. A biblioteca **scikit-learn** é empregada para a criação e treinamento do modelo. Internamente, ela utiliza **Cython**, que compila partes do código Python para C, resultando em maior desempenho durante a execução de algoritmos.

- **Regressão Logística**: Trata-se de um algoritmo de classificação usado em machine learning para estimar a probabilidade de ocorrência de um determinado evento. Durante o treinamento, o modelo ajusta **pesos** e **viéses** com base nos dados de entrada, permitindo prever a probabilidade de conversão (prospecção) de um lead com base nas interações fornecidas.

## 🧠 Technologies and Concepts Used

- **`spawn` from the `child_process` module**: The `spawn` method from Node.js’s `child_process` module is used to run Python scripts as subprocesses. This method allows commands and arguments to be passed directly via the command line, making cross-language integration straightforward.

- **Python and scikit-learn**: Python is a widely used language in data science and machine learning. The **scikit-learn** library is used to create and train the model. Under the hood, it uses **Cython**, which compiles parts of the Python code into C, resulting in improved performance when executing algorithms.

- **Logistic Regression**: This is a classification algorithm used in machine learning to estimate the probability of a given event. During training, the model adjusts **weights** and **biases** based on input data, enabling it to predict the **conversion probability (prospecting)** of a lead based on the provided interactions.


---

## 🚀 Principais pontos do Projeto

- **Comunicação E/S entre linguagens distintas**
- **Reutilização de soluções simples**
- **Machine Learning**

## 🚀 Key Highlights of the Project

- **Input/Output communication between different programming languages**
- **Reuse of simple and effective solutions**
- **Machine Learning**

---

## ⚙️ Processo e Child Process
Um **processo** é uma instância de um programa em execução. Ele funciona de forma independente, pois possui seu próprio **contexto de execução**, incluindo memória alocada, processamento, cache e outros recursos. Criar e manter processos é uma tarefa relativamente **custosa** para o sistema operacional, já que envolve a alocação de recursos dedicados, gerenciamento de estado e controle de todo o seu ciclo de vida.

No contexto do Node.js, é possível criar **subprocessos** (ou **processos filhos**) utilizando o módulo child_process. Esses subprocessos são executados em paralelo ao processo principal (pai), permitindo que tarefas mais pesadas ou demoradas sejam executadas em segundo plano sem bloquear o event loop do Node.js.

A utilização de subprocessos é especialmente recomendada para **operações de E/S (Entrada/Saída)** — ou **I/O (Input/Output)** — que exigem alto consumo de recursos, como chamadas a APIs externas, leitura ou escrita em arquivos grandes, processamento de dados pesados, entre outros. Isso garante que o desempenho da aplicação principal não seja comprometido.

## ⚙️ Process and Child Process

A **process** is an instance of a program in execution. It operates independently, as it has its own **execution context**, including allocated memory, processing power, cache, and other resources. Creating and managing processes is a relatively **costly** task for the operating system, since it involves allocating dedicated resources, managing state, and controlling the entire lifecycle of the process.

In the context of Node.js, it's possible to create **subprocesses** (or **child processes**) using the `child_process` module. These subprocesses run in parallel with the main (parent) process, allowing heavier or time-consuming tasks to be handled in the background without blocking Node.js’s event loop.

Using subprocesses is especially recommended for **I/O (Input/Output) operations** that are resource-intensive, such as external API calls, reading or writing large files, heavy data processing, and more. This ensures that the performance of the main application remains unaffected.

### 🧱 **Exemplo prático no projeto:**
```js
import { spawn } from 'child_process'

// File that contains the code in python
const pythonFile = "bot.py"

// Command in python
const pythonCommand = "python"

// Function to call python
export async function callPython(interactions) {

    // 'Spawn' calls the command that runs python with a list of arguments to be passed
    const py = spawn(pythonCommand, [
        pythonFile,
        interactions
    ])

    const dataString = []

    // 'stdout' outputs data asynchronously through a 'stream', using 'for await' waits for the data to return synchronously and adds the list of data
    for await(const log of py.stdout){
        dataString.push(log.toString())
    }

    // returns the concatenated data after execution
    return dataString.join('')
}
```
---

## 👨‍💻 *Machine Learning (Aprendizado de Máquina)*
**Machine Learning** é um processo dentro da Inteligência Artificial no qual sistemas computacionais simulam o aprendizado humano. A máquina recebe dados de entrada e, a partir deles, identifica padrões, avalia a melhor forma de tomar decisões e ajusta seus **pesos e vieses** durante uma etapa de treinamento, com o objetivo de aplicar esse conhecimento em situações futuras.

Neste projeto, foi utilizado o algoritmo de **Regressão Logística** com **aprendizado supervisionado**. Esse tipo de algoritmo é amplamente usado para **classificação**, estimando a probabilidade de ocorrência de determinado evento com base em variáveis de entrada.

O aprendizado é chamado de supervisionado porque os dados fornecidos à máquina já contêm os resultados esperados (rótulos). Assim, o algoritmo consegue aprender a relação entre as variáveis de entrada e a saída esperada, ajustando seus **pesos** e **viés** para maximizar a precisão nas previsões futuras.

No código, o modelo define automaticamente os pesos de cada interação com base nas seguintes regras:

- A **primeira interação** é considerada a mais importante;
- A **evolução das interações** influencia diretamente a chance de conversão (ou fechamento).

Com isso, a **Regressão Logística** gera um valor entre `0` e `1`, que representa a **probabilidade de conversão de um prospecto**, permitindo análises preditivas com base nos dados históricos.

## 👨‍💻 *Machine Learning*

**Machine Learning** is a process within Artificial Intelligence in which computer systems simulate human learning. The machine receives input data and, from it, identifies patterns, evaluates the best way to make decisions, and adjusts its **weights and biases** during a training phase, with the goal of applying this knowledge to future situations.

In this project, a **Logistic Regression** algorithm with **supervised learning** was used. This type of algorithm is widely used for **classification**, estimating the probability of a certain event occurring based on input variables.

The learning is called supervised because the data provided to the machine already contains the expected outcomes (labels). This allows the algorithm to learn the relationship between the input variables and the expected output, adjusting its **weights** and **bias** to maximize prediction accuracy.

In the code, the model automatically defines the weights of each interaction based on the following rules:

- The **first interaction** is considered the most important;  
- The **evolution of interactions** directly influences the likelihood of conversion (or closing a deal).

As a result, **Logistic Regression** generates a value between `0` and `1`, representing the **probability of a lead converting**, enabling predictive analysis based on historical data.


![Grafico Regressão Logistica](assets\graficoRegressaoLogistica.png)

---

## 🚀 Inicializar
### Passo 1: Abrir o projeto
- Abra o projeto no terminal

### Passo 2: Inicializar
- digite `npm run start` no terminal

### Passo 3: Acessar
- pesquise `http://localhost:3333/?interactions=["good","bad","good","good"]` no navegador (exemplo)

## 🚀 Getting Started

### Step 1: Open the project
- Open the project in the terminal

### Step 2: Start the application
- Type `npm run start` in the terminal

### Step 3: Access the application
- Visit `http://localhost:3333/?interactions=["good","bad","good","good"]` in your browser (example)


---

## 🔗 **Links Úteis / Useful Links**
- [spawn child_process](https://nodejs.org/api/child_process.html#child_processspawncommand-args-options)
- [Regressão Logística / Logistic Regression](https://www.ibm.com/br-pt/think/topics/logistic-regression)
- [Machine Learning](https://blog.dsacademy.com.br/conceitos-fundamentais-de-machine-learning-parte-1/#:~:text=Machine%20Learning%20%C3%A9%20um%20ramo,de%20processamento%20matem%C3%A1tico%20e%20estat%C3%ADstico.)
- [Python](https://docs.python.org/3/)
- [scikit-learn](https://scikit-learn.org/stable/documentation.html)

