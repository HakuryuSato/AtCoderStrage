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
        [R, G, B] = line.split(" ").map(Number);
    } else {
        C = line;
    }

    lineCount++;
}).on("close", () => {
    main();
});

function yasui(R, G, B, C) {
    if (C === "Red") {
        if (G <= B) {
            return G;
        } else {
            return B;
        }
    }
    if (C === "Blue") {
        if (R <= G) {
            return R;
        } else {
            return G;
        }
    }
    if (C === "Green") {
        if (R <= B) {
            return R;
        } else {
            return B;
        }
    }
}

function main() {
    // console.log(R, G, B, C);
    console.log(yasui(R, G, B, C))
}
