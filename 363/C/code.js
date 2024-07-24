const fs = require("fs");
const path = require("path");
const file_number = 3;

function factorial(n) {
    return n ? n * factorial(n - 1) : 1;
  }

  function permute(S) {
    if (S.length <= 1) {
      return new Set([S]);
    }
  
    let permutations = new Set();
    for (let i = 0; i < S.length; i++) {
      let char = S[i];
      let remainingChars = S.slice(0, i) + S.slice(i + 1);
      let subPermutations = permute(remainingChars);
      for (let perm of subPermutations) {
        permutations.add(char + perm);
      }
    }
  
    return permutations;
  }
  

  

function Main(input){
    input = input.split("\n");
    let [N,K] = input[0].split(" ").map(Number)
    let S = input[1]

    // 組み合わせは何通り？ -> 最大100万なので10^7
    // let facNum = factorial(10)

    // 全ての組み合わせをset型で作る
    // let permutations = permute(S)

    // 組み合わせに長さKの回文を部分文字列として含むか


    



}

Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
// Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用