## 📌 1. Como a programação dinâmica foi aplicada na solução?

A **programação dinâmica** foi aplicada através da construção de uma matriz `dp` que armazena os **comprimentos das subsequências comuns mais longas (LCS)** entre os prefixos das duas strings de entrada.

* `dp[i][j]` representa o comprimento da LCS entre os prefixos `data_one[0..i]` e `data_two[0..j]`.
* Se os caracteres atuais forem iguais:
  `dp[i][j] = dp[i-1][j-1] + 1`
* Caso contrário:
  `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

A variação está no conteúdo da `dp`: ela pode armazenar **apenas comprimentos** (com reconstrução posterior via backtracking) ou **conjuntos de subsequências diretamente**.

---

## 🔍 2. Por que o uso de *backtracking* é necessário neste problema?

O backtracking se torna necessário quando a matriz `dp` armazena apenas os **comprimentos** das subsequências comuns.

Esse é o caso nas implementações `lcsWithDPBT` e `dynamic-programming_backtracking/main.py`. Após o preenchimento da matriz `dp`, o backtracking é usado para **reconstruir todas as LCSs possíveis** que resultaram no valor máximo da matriz.

---

## ⚠️ 3. Houve desafios na implementação? Quais? Como foram superados?

### ✅ Principais Desafios e Soluções:

* **Manipulação incomum da tabela DP:**
  → Superado armazenando **conjuntos de strings** em cada célula da `dp`, permitindo coletar todas as subsequências durante o preenchimento, evitando a fase de reconstrução.

* **Complexidade das funções embutidas:**
  → Otimizado com:

  * **Design eficiente da DP**: usando apenas comprimentos para ganho de desempenho (tempo constante por célula).
  * **Memorização no backtracking**: uso de cache para evitar recomputações de estados repetidos, especialmente quando há múltiplas LCSs.

---

## 🧠 4. Qual é a complexidade da solução proposta?

A seguir, a análise **detalhada** da complexidade da solução para as duas abordagens:

---

### a) 📊 Apenas Programação Dinâmica

#### Trechos relevantes:

```python
dp = [[{""} for _ in range(len_one + 1)] for _ in range(len_two + 1)]
```

* Criação da matriz: `(len_two + 1) × (len_one + 1)` células.
* Cada célula armazena um conjunto (`set`) contendo pelo menos uma string.
* Custo: **O(N x M)** alocação inicial (onde N = len(data_one), M = len(data_two))

---

```python
for i in range(len_one):
    for j in range(len_two):
        ...
```

Esse bloco percorre toda a matriz `dp`, totalizando **N × M** iterações.

##### 1. Se os caracteres forem iguais:

```python
for seq in dp[i][j]:
    dp[i + 1][j + 1].add(seq + data_one[i])
```

* Em cada célula, percorre-se um conjunto com até **S** subsequências.
* Cada `add(seq + ...)` tem custo **O(L)** (L = tamanho da LCS).
* Total por célula: **O(S × L)**
* Total geral: **O(M × N × S × L)**

##### 2. Se forem diferentes:

```python
left = len(next(iter(dp[i + 1][j]), ""))
upper = len(next(iter(dp[i][j + 1]), ""))
```

* O `len()` e `iter()` são **O(1)**, mas servem apenas para comparar.

```python
dp[i + 1][j + 1] = dp[i + 1][j].copy()
```

ou

```python
dp[i + 1][j + 1] = dp[i][j + 1].copy()
```

ou

```python
dp[i + 1][j + 1] = dp[i + 1][j].union(dp[i][j + 1])
```

* `.copy()` e `.union()` operam em conjuntos com até **S** strings de comprimento **L**, custo: **O(S × L)** por célula.

---

#### 🧮 Complexidade final (versão com DP apenas):

| Cenário    | Complexidade                       | Justificativa                              |
| ---------- | ---------------------------------- | ------------------------------------------ |
| **Médio**  | `O(N × M × S × L)`                 | S subsequências de L caracteres por célula |
| **Melhor** | `O(N × M)`                         | Poucas subsequências ou strings curtas     |
| **Pior**   | `O(N × M × 2^min(M,N) × min(M,N))` | Explosão combinatória de subsequências     |

---

### b) 🔁 Programação Dinâmica + Backtracking

#### Trechos relevantes:

```python
dp = [[0] * (len_two + 1) for _ in range(len_one + 1)]
```

* Inicialização da matriz com inteiros → custo: **O(N × M)**

---

```python
for i in range(len_one):
    for j in range(len_two):
        ...
```

* Preenchimento simples com `+1` ou `max()` → custo: **O(1)** por célula
* Total: **O(N × M)**

---

```python
def backtrack(i, j): ...
```

A função `backtrack(i, j)` é chamada no máximo uma vez para cada par (i, j) **de forma memoizada**:

##### Casos:

* **Base:** `i == 0 or j == 0` → retorna `{""}` → O(1)
* **Caracteres iguais:**

  ```python
  return {s + data_one[i - 1] for s in backtrack(i - 1, j - 1)}
  ```

  * Pode concatenar até **K** subsequências → custo **O(K × L)** no total
* **Caracteres diferentes:**

  ```python
  result |= backtrack(i - 1, j)
  result |= backtrack(i, j - 1)
  ```

  * É possível visitar o mesmo estado por múltiplos caminhos, mas o cache evita recomputações.
  * O número de subsequências distintas geradas é **K**, cada com comprimento até **L**.

---

#### 🧮 Complexidade final (DP + Backtracking):

| Cenário    | Complexidade                       | Justificativa                                      |
| ---------- | ---------------------------------- | -------------------------------------------------- |
| **Médio**  | `O(N × M + K × L)`                 | Preenchimento da `dp` + geração de K subsequências |
| **Melhor** | `O(N × M + L)`                     | Apenas uma LCS gerada                              |
| **Pior**   | `O(N × M + 2^min(M,N) × min(M,N))` | Múltiplas LCSs geradas via backtracking            |

---

### ✅ Comparativo final

| Abordagem                   | Melhor Caso    | Caso Médio         | Pior Caso                          |
| --------------------------- | -------------- | ------------------ | ---------------------------------- |
| Apenas Programação Dinâmica | `O(M × N)`     | `O(M × N × S × L)` | `O(M × N × 2^min(M,N) × min(M,N))` |
| DP + Backtracking           | `O(M × N + L)` | `O(M × N + K × L)` | `O(M × N + 2^min(M,N) × min(M,N))` |

---

## 📚 5. O que o grupo aprendeu ao resolver esse problema?

### 🧠 Conceitos Técnicos e Práticos:

* **Programação Dinâmica:**
  Aplicação para resolver problemas de otimização, reduzindo recomputações.

* **Backtracking com Memorização:**
  Essencial para reconstrução de todas as soluções possíveis, evitando explosões combinatórias.

* **Análise de Complexidade:**
  Avaliação detalhada dos cenários médio, melhor e pior caso, relacionando com estruturas de dados utilizadas.

* **Boas Práticas de Engenharia de Software:**
  Organização, validação, clareza e documentação do código.

* **Aplicabilidade no mundo real:**
  O problema de LCS exemplifica a importância da **análise de padrões em dados sequenciais**, aplicável em bioinformática, comparação de textos, sincronização de arquivos e muito mais.
