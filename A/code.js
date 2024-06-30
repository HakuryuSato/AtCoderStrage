// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");

// const rl = readline.createInterface({
//     input: fs.createReadStream(path.join(__dirname, "input0.txt")),
//     output: process.stdout,
// });

// 本番用*************************************************************************
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
// 本番用*************************************************************************

let lineCount = 0;
let lines = [];
rl.on("line", (line) => {
    H = Number(line);

    lineCount++;
}).on("close", () => {
    main();
});

function main() {
    // console.log(H);

    cropHeight = 0;
    i = 0;

    while (H >= cropHeight) {
        cropHeight += Math.pow(2, i);
        // console.log(i, cropHeight);

        i++;
    }

    console.log(i);
}
