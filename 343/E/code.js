// テスト用 ---------------------------------------------------------------------------------------------------
const readline = require("readline");
const fs = require("fs");
const path = require("path");

const file_number= 1
const file = `input${file_number}.txt`;

const rl = readline.createInterface({
    input: fs.createReadStream(path.join(__dirname, file)),
    output: process.stdout,
});

// テスト用 ---------------------------------------------------------------------------------------------------

// // 本番用 ---------------------------------------------------------------------------------------------------
// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });
// // 本番用 ---------------------------------------------------------------------------------------------------




lineCount = 0;
lines=[];
rl.on("line", (line) => {



    lineCount++;
}).on("close", () => {
    main();
});



function main() {
    console.log("AAA")
}
