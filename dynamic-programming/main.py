from typing import List

"""
    AUTORES: Augusto Amaral, Guilherme Siqueira, Henrique Borelli, Julio Santos, Otávio Gonçalves, Pedro Ribeiro,
             Vinicius Alves, Walyson Moises

    VERSÃO: V1.0

    DATA: 19/06/2025
"""

def lcs_sequences(data_one: str, data_two: str) -> List[str]:
    len_one, len_two = len(data_one), len(data_two)

    """
    INICIALIZAÇÃO DA MATRIZ

        • Cria-se uma matriz dp com dimensões:
            ([tamanho da primeira string]+1)x([tamanho da segunda string]+1) (um extra para lidar com prefixos vazios).

        • Inicializa-se todas as células com um conjunto ('set' em python) contendo uma string vazia. Um conjunto é uma
        coleção que não é ordenada, imutável e não indexada.
    """
    dp = [[{""} for _ in range(len_one + 1)] for _ in range(len_two + 1)] # O(n × m)

    """
    PREENCHIMENTO DA MATRIZ

        • O preenchimento da matriz dp na célula dp[i+1][j+1] ocorre da seguinte forma:
            • Se o caractere i da primeira string e o caractere j da segunda string forem iguais:
                Para cada conjunto em dp[i][j], adiciona-se o caractere comum ao final.

            • Se são diferentes, busca-se herdar o com as subsequências mais longas entre dp[i+1][j] (esquerda)
            e dp[i][j+1] (acima):
                    | dp[i + 1][j]: célula à esquerda da atual
                    | dp[i][j + 1]: célula acima da atual

                    Essas células contêm sets com várias subsequências, como exemplo: {"ab", "ac", "ba"}. Como
                    conjuntos não têm ordem, usamos next(iter(...)) para obter arbitrariamente um dos elementos
                    e medir seu comprimento — apenas para fins de comparação.

                    O comprimento das subsequências é comparado:
                        • Se um lado for maior, herda-se apenas ele, usando o copy() para herdar o valor e não
                        a referência
                        • Se forem iguais, é feita a união de ambos
    """
    # O(n × m)
    for i in range(len_one):
        for j in range(len_two):
            if data_one[i] == data_two[j]:
                for seq in dp[i][j]:    # O(S), considerando S como o número de subsequências em dp[i][j]
                    dp[i + 1][j + 1].add(seq + data_one[i]) # O(L), onde L é o comprimento da subsequência
            else:
                left = len(next(iter(dp[i + 1][j]), ""))    # O(1)
                upper = len(next(iter(dp[i][j + 1]), ""))   # O(1)

                if left > upper:
                    dp[i + 1][j + 1] = dp[i + 1][j].copy()  # O(S × L)
                elif left < upper:
                    dp[i + 1][j + 1] = dp[i][j + 1].copy()  # O(S × L)
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j].union(dp[i][j + 1]) # O(S × L)

    """
    ENCONTRAR AS MAIORES SUBSEQUÊNCIAS

        • Com o preenchimento acima, a última posição da matriz (dp[len_one][len_two] / final_seqs) contém
        todas as subsequências comuns possíveis.

        • Assim, o conjunto é filtrado para manter apenas as subsequências com o maior comprimento e, em seguida,
        ordenado em ordem alfabética.
    """
    final_seqs = dp[len_one][len_two]
    max_len = max(len(seq) for seq in final_seqs)   # O(S × L)
    result = sorted({seq for seq in final_seqs if len(seq) == max_len}) # O(S × L × log(S))
    return result

# Análise assintótica total:
# Melhor caso: O(n × m) - strings muito diferentes
# Caso médio: O(n × m × S × L) - S = número médio de subsequências, L = comprimento médio
# Pior caso: O(n × m × 2^min(n,m) × min(n,m)) - strings similares com caracteres repetidos

def main():
    D = int(input("Número de pares de conjuntos de dados: "))

    if D > 10:
        return

    for d in range(D):
        print(f"Par {d+1} de {D}\n")

        data_one = input("Primeiro conjunto: ").strip()
        if len(data_one) > 80 or len(data_one) < 1:
            return

        data_two = input("Segundo conjunto: ").strip()
        if len(data_two) > 80 or len(data_two) < 1:
            return

        for seq in lcs_sequences(data_one, data_two):
            print(seq)
        if d < D - 1:
            print()


if __name__ == "__main__":
    main()
