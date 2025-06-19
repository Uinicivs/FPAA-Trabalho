def lcs_sequences(data_one: str, data_two: str):
    len_one, len_two = len(data_one), len(data_two)

    """
    INICIALIZAÇÃO DA MATRIZ

        • Cria-se uma matriz dp com dimensões:
            ([tamanho da primeira string]+1) x (tamanho da segunda string+1) (um extra para lidar com prefixos vazios).

        • Inicializa-se todas as células com um conjunto ('set' em python) contendo uma string vazia. Um conjunto é uma
        coleção que não é ordenada, imutável e não indexada.
    """
    dp = [[{""} for _ in range(len_one + 1)] for _ in range(len_two + 1)]

    """
    PREENCHIMENTO DA MATRIZ

        • O preenchimento da matriz dp na célula dp[i+1][j+1] ocorre da seguinte forma:
            • Se o caractere i da primeira string e o caractere j da segunda string forem iguais:
                Para cada conjunto em dp[i][j], adiciona-se o caractere comum ao final.

            • Se são diferentes, buscamos herdar o com as subsequências mais longas entre dp[i+1][j] (esquerda)
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
    for i in range(len_one):
        for j in range(len_two):
            if data_one[i] == data_two[j]:
                for seq in dp[i][j]:
                    dp[i + 1][j + 1].add(seq + data_one[i])
            else:
                left = len(next(iter(dp[i + 1][j]), ""))
                upper = len(next(iter(dp[i][j + 1]), ""))

                if left > upper:
                    dp[i + 1][j + 1] = dp[i + 1][j].copy()
                elif left < upper:
                    dp[i + 1][j + 1] = dp[i][j + 1].copy()
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j].union(dp[i][j + 1])

    """
    ENCONTRAR AS MAIORES SUBSEQUÊNCIAS

        • Com o preenchimento acima, a última posição da matriz (dp[len_one][len_two] / final_seqs) contém
        todas as subsequências comuns possíveis.

        • Assim, o conjunto é filtrado para manter apenas as subsequências com o maior comprimento e, em seguida,
        ordenado em ordem alfabética.
    """
    final_seqs = dp[len_one][len_two]
    max_len = max(len(seq) for seq in final_seqs)
    result = sorted({seq for seq in final_seqs if len(seq) == max_len})
    return result


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
