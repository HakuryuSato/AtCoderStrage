// テスト用 ---------------------------------------------------------------------------------------------------
// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");

// const file_number = 2;
// const file = `input${file_number}.txt`;

// const rl = readline.createInterface({
//     input: fs.createReadStream(path.join(__dirname, file)),
//     output: process.stdout,
// });

// テスト用 ---------------------------------------------------------------------------------------------------

// // 本番用 ---------------------------------------------------------------------------------------------------
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
// // 本番用 ---------------------------------------------------------------------------------------------------

lineCount = 0;
let lines = [];
let N, K;
rl.on("line", (line) => {
    if (lineCount === 0) {
        [N, K] = line.split(" ").map(BigInt);
    } else {
        lines = line.split(" ").map(BigInt);
    }

    lineCount++;
}).on("close", () => {
    main();
});

function sumToK(K) {
    return K * (K + 1) / 2;
}

function main() {
    // console.log(N, K, lines);

    const totalSum = K * (K + 1n) / 2n;

    // Aに含まれる値の合計を計算
    const linesSet = new Set(lines);
    let linesSum = 0n;
    for (let num of linesSet) {
        if (num >= 1n && num <= K) {
            linesSum += num;
        }
    }

    // 含まれていない値の合計を計算
    const result = totalSum - linesSum;
    console.log(result.toString());
}

