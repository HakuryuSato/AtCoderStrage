// テスト用 ---------------------------------------------------------------------------------------------------
const readline = require("readline");
const fs = require("fs");
const path = require("path");

const file_number = 0;
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
lines = [];
rl.on("line", (line) => {
    [w, b] = line.split(" ").map(Number);

    lineCount++;
}).on("close", () => {
    main();
});

function main() {
    const t = "wbwbwwbwbwbw";
    console.log(w,b)

    let found = false;

    for (let i = 0; i < t.length; i++) {
        let nw = 0, nb = 0;
        for (let j = 0; j < w + b; j++) {
            if (t[(i + j) % t.length] === 'w') nw++;
            else nb++;
        }
        if (w === nw && b === nb) {
            found = true;
            break;
        }
    }
    
    if (found) {
        console.log("Yes");
    } else {
        console.log("No");
    }
}