const readline = require("readline");
const fs = require("fs");
const path = require("path");

// // 本番用 ---------------------------------------------------------------------------------------------------
// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });
// // 本番用 ---------------------------------------------------------------------------------------------------

// テスト用 ---------------------------------------------------------------------------------------------------
for (let i = 0; i <= 2; i++) {
    const file = `input${i}.txt`;

    const rl = readline.createInterface({
        input: fs.createReadStream(path.join(__dirname, file)),
        output: process.stdout,
    });

    lineCount = 0;
    lines=[];
    rl.on("line", (line) => {
        lineCount++;






    }).on("close", () => {
        main();
    });
}
// テスト用 ---------------------------------------------------------------------------------------------------

function main() {

}
