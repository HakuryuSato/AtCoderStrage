// テスト用 ---------------------------------------------------------------------------------------------------
// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");

// const file_number = 3;
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
lines = [];
rl.on("line", (line) => {
    if (lineCount === 0) {
        N = BigInt(line);
    } else {
        lines.push(line.split(" ").map(BigInt));
    }

    lineCount++;
}).on("close", () => {
    main();
});

function calc(N, lines) {
    let X = new Array(N).fill(0n);
    let sumL = 0n;
    let sumR = 0n;

    // RとLの合計から0を調整可能か
    for (let i = 0; i < N; i++) {
        sumL += lines[i][0];
        sumR += lines[i][1];
    }

    // 0の範囲に収まるか
    if (sumL <= 0n && 0n <= sumR) {
        let sum = sumL;

        for (let i = 0; i < N; i++) {
            X[i] = lines[i][0];
        }


        for (let i = 0; i < N && sum !== 0n; i++) {
            let L = lines[i][0];
            let R = lines[i][1];
            let adjustment = 0n;

            if (sum > 0n) { // sumが0より大きいなら減らして調整
                adjustment = -sum;
                if (L + adjustment < L) {
                    adjustment = L - L;
                }
            } else { // 0より小さいなら増やして調整
                adjustment = R - L;
                if (adjustment > -sum) {
                    adjustment = -sum;
                }
            }

            if (L + adjustment <= R) { // 調整値がLRの範囲内か？
                X[i] = L + adjustment;
                sum += adjustment;
            }
        }

        return X.map((x) => x.toString());
    } else {
        return null;
    }
}
function main() {
    result = calc(N, lines);
    if (result === null) {
        console.log("No");
    } else {
        console.log("Yes");
        console.log(result.join(" "));
    }
}
