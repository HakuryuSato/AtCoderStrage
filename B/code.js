// // テスト用 ---------------------------------------------------------------------------------------------------
// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");
// const { count } = require("console");

// const file_number = 2;
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
        [N, Q] = line.split(" ").map(Number);
    } else {
        lines = line.split(" ").map(Number);
    }

    lineCount++;
}).on("close", () => {
    main();
});

function main() {
    let teeth = {};
    for (let i = 1; i <= N; i++) {
        teeth[i] = true;
    }

    // console.log(N, Q, lines);
    lines.map((line) => {
        const key = line.toString();
        if (teeth.hasOwnProperty(key)) {
            teeth[key] = !teeth[key];
        }
    });

    let count = 0;

    Object.values(teeth).map((value) => {
        if (value) {
            count++;
        }
    });

    // console.log(teeth);
    console.log(count);
}
