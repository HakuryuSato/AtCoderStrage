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

// // 本番用 ---------------------------------------------------------------------------------------------------
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

lineCount = 0;
lines = [];
rl.on("line", (line) => {
    S = line;

    lineCount++;
}).on("close", () => {
    main();
});

function countOccurrences(str, char) {
    return str.split(char).length - 1;
}

function main() {
    set = new Set(S);
    for (const char of set) {
        if (countOccurrences(S, char) === 1) {
            console.log(S.indexOf(char) + 1);
            break;
        }
    }
}
