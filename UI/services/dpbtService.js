function lcsWithDPBT(dataOne, dataTwo) {
  const lenOne = dataOne.length;
  const lenTwo = dataTwo.length;
  const dp = Array.from({ length: lenOne + 1 }, () => Array(lenTwo + 1).fill(0));
  const steps = [];

  // Construção da tabela DP
  for (let i = 0; i < lenOne; i++) {
    for (let j = 0; j < lenTwo; j++) {
      if (dataOne[i] === dataTwo[j]) {
        dp[i + 1][j + 1] = dp[i][j] + 1;
        steps.push(`dp[${i + 1}][${j + 1}] = dp[${i}][${j}] + 1 (${dp[i][j]} + 1)`);
      } else {
        dp[i + 1][j + 1] = Math.max(dp[i][j + 1], dp[i + 1][j]);
        steps.push(`dp[${i + 1}][${j + 1}] = max(dp[${i}][${j + 1}], dp[${i + 1}][${j}])`);
      }
    }
  }

  const memo = new Map();
  const allPaths = [];

  // Backtracking com rastreamento de caminhos
  function backtrack(i, j, path = [], current = '') {
    const key = `${i},${j},${current}`;
    if (memo.has(key)) return memo.get(key);

    let result = new Set();

    if (i === 0 || j === 0) {
      result.add('');
      if (current) {
        allPaths.push({ sequence: current.split('').reverse().join(''), path: [...path] });
      }
    } else if (dataOne[i - 1] === dataTwo[j - 1]) {
      const newPath = [...path, { i, j, match: true, char: dataOne[i - 1] }];
      for (const s of backtrack(i - 1, j - 1, newPath, dataOne[i - 1] + current)) {
        result.add(s + dataOne[i - 1]);
      }
    } else {
      if (dp[i - 1][j] >= dp[i][j - 1]) {
        const newPath = [...path, { i, j, match: false }];
        for (const s of backtrack(i - 1, j, newPath, current)) {
          result.add(s);
        }
      }
      if (dp[i][j - 1] >= dp[i - 1][j]) {
        const newPath = [...path, { i, j, match: false }];
        for (const s of backtrack(i, j - 1, newPath, current)) {
          result.add(s);
        }
      }
    }

    memo.set(key, result);
    return result;
  }

  const sequences = [...backtrack(lenOne, lenTwo)];
  const maxLen = dp[lenOne][lenTwo];
  const filtered = sequences.filter(seq => seq.length === maxLen).sort();

  return { dp, sequences: filtered, steps, allPaths };
}


module.exports = lcsWithDPBT;