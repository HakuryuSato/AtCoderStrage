// // テスト用 ---------------------------------------------------------------------------------------------------
// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");

// const file_number = 2
// const file = `input${file_number}.txt`;

// const rl = readline.createInterface({
//     input: fs.createReadStream(path.join(__dirname, file)),
//     output: process.stdout,
// });

// // テスト用 ---------------------------------------------------------------------------------------------------

// 本番用 ---------------------------------------------------------------------------------------------------
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
// 本番用 ---------------------------------------------------------------------------------------------------

lineCount = 0;
lines = [];
rl.on("line", (line) => {
    if (lineCount === 0) {
        N = parseInt(line);
    } else {
        lines = line.split(" ").map(Number);
    }

    lineCount++;
}).on("close", () => {
    main();
});


function findLastPersonPoints(N, A) {
    // N-1人の持ち点の合計を計算
    let sum = 0;
    for (let i = 0; i < N - 1; i++) {
        sum += A[i];
    }
    // N人目の持ち点は -sum。ただし、-0の場合は0にする
    const result = -sum === 0 ? 0 : -sum;
    console.log(result);
}

function main() {
    // console.log(N, lines);
    findLastPersonPoints(N, lines);
}
