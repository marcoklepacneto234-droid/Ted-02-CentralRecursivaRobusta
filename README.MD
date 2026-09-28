# Central Recursiva Robusta

## Integrantes

* Marco Antonio Klepac Neto
* Thulio Augusto Sousa Barros

## Descrição

O projeto Central Recursiva Robusta é uma aplicação desenvolvida em Python para realizar operações matemáticas utilizando funções recursivas.

A aplicação possui duas operações principais:

* `M`: cálculo do Máximo Divisor Comum (MDC);
* `S`: soma dos dígitos de um número.

O projeto utiliza módulos, pacote Python, validação de entradas, exceções personalizadas e algoritmos recursivos.

## Estrutura do projeto

```text
CentralRecursivaRobusta/
│
├── main.py
├── README.md
│
└── central_recursiva/
    ├── __init__.py
    ├── operacoes.py
    ├── excecoes.py
    └── validacoes.py
```

## Execução

Para executar o programa, abra o terminal na pasta do projeto e utilize:

```bash
python main.py
```

Depois, informe a quantidade de operações e as operações desejadas.

Exemplo:

```text
7
S 12345
M 72 30
M 17 19
S 0
M 0 25
S -50
X 10 20
```

Saída:

```text
SOMA = 15
MDC = 6
MDC = 1
SOMA = 0
ERRO: EntradaInvalida
ERRO: EntradaInvalida
ERRO: OperacaoInvalida
```

## Módulos

### `operacoes.py`

Contém os dois algoritmos recursivos utilizados no projeto:

* `calcular_mdc()`: calcula o MDC utilizando o algoritmo recursivo de Euclides.
* `somar_digitos()`: calcula recursivamente a soma dos dígitos de um número.

### `validacoes.py`

Responsável por verificar se os valores recebidos são válidos para cada operação.

* Para a operação `M`, os valores devem ser positivos.
* Para a operação `S`, o número deve ser não negativo.

### `excecoes.py`

Contém duas exceções personalizadas:

* `EntradaInvalida`: utilizada quando os valores fornecidos não atendem às regras da operação.
* `OperacaoInvalida`: utilizada quando a operação informada não é `M` ou `S`.

### `main.py`

Responsável por receber as entradas, processar as operações, chamar as funções dos módulos e tratar as exceções.

## Algoritmos recursivos

### Cálculo do MDC

O cálculo do Máximo Divisor Comum utiliza o algoritmo de Euclides de forma recursiva.

A função recebe dois números. Enquanto o segundo número for
