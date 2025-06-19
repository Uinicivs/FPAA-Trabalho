from typing import List, Set, Tuple


def lcs_sequences(data_one: str, data_two: str) -> List[str]:
    len_one, len_two = len(data_one), len(data_two)

    """
    INICIALIZAÇÃO DA MATRIZ

        • Cria-se uma matriz dp com dimensões:
            ([tamanho da primeira string]+1)x([tamanho da segunda string]+1) (um extra para lidar com prefixos vazios).

        • Inicializa-se todas as células com 0.
    """
    dp = [[0] * (len_two + 1) for _ in range(len_one + 1)]

    """
    PREENCHIMENTO DA MATRIZ

        • O preenchimento da matriz dp na célula dp[i+1][j+1] ocorre da seguinte forma:
            • Se o caractere i da primeira string e o caractere j da segunda string forem iguais:
                Estende-se a subsequência comum. O novo valor é 1 a mais que a LCS dos prefixos anteriores.

            • Se são diferentes, o maior valor possível vindo da célula acima (dp[i][j+1]) ou à
            esquerda (dp[i+1][j]) é utilizado:
                Isso significa que o caractere atual não contribui para a LCS.
    """
    for i in range(len_one):
        for j in range(len_two):
            if data_one[i] == data_two[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    """
    ENCONTRAR AS MAIORES SUBSEQUÊNCIAS USANDO BACKTRACKING

        • Define-se uma função recursiva com cache manual utilizando uma hashtable (dicionário). Essa função
        percorre a matriz dp de baixo para cima, reconstruindo as subsequências que levaram ao valor máximo da LCS.
        Ela retorna um conjunto (set) de strings contendo todas as subsequências parciais ou completas que podem ser
        formadas até a posição (i, j) da matriz.

        • O funcionamento da função se dá da seguinte forma:

            • Caso base:
                Se o início de qualquer string é atingido, retorna-se um conjunto (set) com uma string vazia

            • Caso de igualdade:
                Quando os caracteres coincidem, um caractere que pertence à LCS foi encontrado! Recua-se uma posição
                em cada string e esse caractere é concatenado a todas as subsquências retornadas.

            • Caso de diferença:
                Quando os caracteres são diferentes, seguimos os caminhos na tabela dp que preservam o
                comprimento máximo da LCS até o ponto atual:
                    • Se o valor acima (dp[i-1][j]) for maior ou igual ao da esquerda (dp[i][j-1]), segue-se para cima.
                    • Se o valor da esquerda for maior ou igual ao de cima, segue-se para a esquerda.
                    • Se forem iguais, ambos os caminhos são explorados. Isso permite encontrar todas as variações
                    possíveis da LCS.
    """
    cache: dict[Tuple[int, int], Set[str]] = {}

    def backtrack(i: int, j: int) -> Set[str]:
        if (i, j) in cache:
            return cache[(i, j)]

        if i == 0 or j == 0:
            return {""}

        if data_one[i - 1] == data_two[j - 1]:
            return {s + data_one[i - 1] for s in backtrack(i - 1, j - 1)}

        result = set()
        if dp[i - 1][j] >= dp[i][j - 1]:
            result |= backtrack(i - 1, j)

        if dp[i][j - 1] >= dp[i - 1][j]:
            result |= backtrack(i, j - 1)

        cache[(i, j)] = result
        return result

    sequences = backtrack(len_one, len_two)

    """
    FINALIZAÇÃO

        Após encontrar TODAS as subsequências utilizando backtracking, a coleção é filtrada a fim de obter
        apenas as maiores. Em seguida, o conjunto é ordenado alfabeticamente.
    """
    max_len = dp[len_one][len_two]
    return sorted(seq for seq in sequences if len(seq) == max_len)


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
