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
        N = Number(line);
    } else {
        lines.push(line.split(" ").map(Number));
    }

    lineCount++;
}).on("close", () => {
    main();
});

function main() {
    for (i = 0; i < N; i++) {
        result = [];
        for (let j = 0; j < lines[i].length; j++) {
            if(lines[i][j] === 1) {
                result.push(j+1);
            }
        }

        console.log(result.join(" "));
    }
}
