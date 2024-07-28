const fs = require("fs");
const path = require("path");
const file_number = 3;

function Main(input) {
    input = input.split("\n");
    let [N, S, M, L] = input[0].split(" ").map(Number);

    let ans = Infinity;
    for (let a = 0; a <= 100; a++) {
        for (let b = 0; b <= 100; b++) {
            for (let c = 0; c <= 100; c++) {
                if (a * 6 + b * 8 + c * 12 >= N) { // N個以上を満たす全ての組み合わせ
                    ans = Math.min(ans, a * S + b * M + c * L); // ansと、満たす条件比較して低いほうを代入
                }
            }
        }
    }

    console.log(ans);
}

Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
// Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
