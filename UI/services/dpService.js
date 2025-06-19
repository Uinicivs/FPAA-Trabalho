function getSubseqLength(set) {
  for (const s of set) return s.length;
  return 0;
}

function lcsWithDP(s1, s2) {
  const n = s1.length;
  const m = s2.length;

  // dp[i][j] = conjunto de subsequências comuns mais longas até os prefixos s1[0:i] e s2[0:j]
  const dp = Array.from({ length: n + 1 }, () =>
    Array.from({ length: m + 1 }, () => new Set([""]))
  );

  // dpLen[i][j] = matriz de inteiros com os tamanhos máximos das subsequências em cada célula
  const dpLen = Array.from({ length: n + 1 }, () =>
    Array.from({ length: m + 1 }, () => 0)
  );

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (s1[i] === s2[j]) {
        // Caso os caracteres combinem, adiciona s1[i] às subsequências anteriores
        for (const seq of dp[i][j]) {
          dp[i + 1][j + 1].add(seq + s1[i]);
        }
      } else {
        // Caso contrário, compara os caminhos da esquerda e de cima
        const left = getSubseqLength(dp[i + 1][j]);
        const up = getSubseqLength(dp[i][j + 1]);

        if (left > up) {
          dp[i + 1][j + 1] = new Set(dp[i + 1][j]);
        } else if (up > left) {
          dp[i + 1][j + 1] = new Set(dp[i][j + 1]);
        } else {
          dp[i + 1][j + 1] = new Set([...dp[i + 1][j], ...dp[i][j + 1]]);
        }
      }

      // Atualiza a matriz numérica com o comprimento máximo encontrado
      const maxLen = Math.max(
        ...Array.from(dp[i + 1][j + 1]).map((s) => s.length),
        0
      );
      dpLen[i + 1][j + 1] = maxLen;
    }
  }

  // Extrai as subsequências com maior comprimento
  const result = Array.from(dp[n][m]);
  const maxLength = Math.max(...result.map((s) => s.length));
  const longest = result.filter((s) => s.length === maxLength).sort();
  const dpOut = dp.map((row, i) =>
    row.map((set, j) => ({
        len: dpLen[i][j],
        set: Array.from(set).filter(s => s.length === dpLen[i][j])
    }))
    );

  return { sequences: longest, dp: dpOut, maxLength };
}


module.exports = lcsWithDP;