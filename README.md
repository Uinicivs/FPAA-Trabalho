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

## 📈 4. Qual é a complexidade da solução proposta?

### 🧮 a) Versão com **apenas programação dinâmica**

| Caso       | Complexidade                       | Observações                                                    |
| ---------- | ---------------------------------- | -------------------------------------------------------------- |
| **Médio**  | `O(M × N × S × L)`                 | Operações com conjuntos de subsequências por célula            |
| **Melhor** | `O(M × N)`                         | Poucas ou nenhuma subsequência comum                           |
| **Pior**   | `O(M × N × 2^min(M,N) × min(M,N))` | Explosão exponencial de subsequências (ex: `aaaaa` vs `aaaaa`) |

* `M`, `N`: tamanhos das strings
* `S`: número de subsequências
* `L`: comprimento das subsequências

---

### 🔄 b) Versão com **DP + Backtracking**

| Caso       | Complexidade                       | Observações                                 |
| ---------- | ---------------------------------- | ------------------------------------------- |
| **Médio**  | `O(M × N + K × L)`                 | `K`: número de LCSs, `L`: comprimento médio |
| **Melhor** | `O(M × N + L)`                     | Apenas uma LCS                              |
| **Pior**   | `O(M × N + 2^min(M,N) × min(M,N))` | Múltiplas LCSs com caminhos diferentes      |

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
