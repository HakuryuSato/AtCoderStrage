// テスト用 ---------------------------------------------------------------------------------------------------
// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");
// const { subscribe } = require("diagnostics_channel");

// const file_number= 2
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
lines=[];
rl.on("line", (line) => {
    S=line


    lineCount++;
}).on("close", () => {
    main();
});



function main() {
    // console.log(S)
    substrings = new Set();

    for (let i = 0; i < S.length; i++) {
        for (let j = i + 1; j <= S.length; j++) {
            substrings.add(S.slice(i, j));
        }
    }

    console.log(substrings.size);
}
