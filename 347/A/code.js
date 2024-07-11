// // テスト用 ---------------------------------------------------------------------------------------------------
// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");

// const file_number = 0;
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
        [N, K] = line.split(" ").map(Number);
    } else {
        lines=line.split(" ").map(Number);
    }

    lineCount++;
}).on("close", () => {
    main();
});

function main() {
    // console.log(N, K, lines);
    result=[]

    for (i = 0; i < N; i++) {
        if(lines[i]%K===0){

            result.push(lines[i]/K);
        }
    }

    console.log(result.join(" "))
}
