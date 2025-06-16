from typing import List, Set, Tuple
from functools import lru_cache


def lcs_sequences(data_one: str, data_two: str) -> List[str]:
    len_one, len_two = len(data_one), len(data_two)

    #
    dp = [[0] * (len_two + 1) for _ in range(len_one + 1)]

    for i in range(len_one):
        for j in range(len_two):
            if data_one[i] == data_two[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    # Passo 2: Backtrack para reconstruir todas as subsequências
    @lru_cache(maxsize=None)
    def backtrack(i: int, j: int) -> Set[str]:
        if i == 0 or j == 0:
            return {""}
        elif data_one[i - 1] == data_two[j - 1]:
            return {s + data_one[i - 1] for s in backtrack(i - 1, j - 1)}
        else:
            result = set()
            if dp[i - 1][j] >= dp[i][j - 1]:
                result |= backtrack(i - 1, j)
            if dp[i][j - 1] >= dp[i - 1][j]:
                result |= backtrack(i, j - 1)
            return result

    sequences = backtrack(len_one, len_two)
    max_len = dp[len_one][len_two]

    # Reverter sequências (pois foram construídas de trás pra frente) e filtrar as maiores
    return sorted(seq for seq in sequences if len(seq) == max_len)


def get_inputs() -> List[Tuple[str, str]]:
    datasets = []
    num_inputs = int(input('how many dataset pairs? '))
    for i in range(num_inputs):
        print(f'Pair n° {i+1}')
        data_one = input('first dataset: ').strip()
        data_two = input('second dataset: ').strip()
        datasets.append((data_one, data_two))
    return datasets


def main():
    datasets = get_inputs()
    # datasets = [('ijkijkii', 'ikjikji')]

    for i, (data_one, data_two) in enumerate(datasets):
        results = lcs_sequences(data_one, data_two)
        for seq in results:
            print(seq)
        if i < len(datasets) - 1:
            print()


if __name__ == "__main__":
    main()
