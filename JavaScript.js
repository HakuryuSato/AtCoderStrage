// const readline = require("readline");
// const fs = require("fs");
// const rl = readline.createInterface({
//     input: fs.createReadStream("input2.txt"),
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
    if (lineCount === 0) {
        [N, M] = line.split(" ").map(Number);
    } else {
        lines.push(line.split(" ").map(Number));
    }

    lineCount++;
}).on("close", () => {
    main();
});

function createConsec(arr) {
    consecList = [];
    // console.log(arr)

    for (let i = 0; i < arr.length - 1; i++) {
        // console.log(arr[i] + 1)
        if (arr[i] + 1 === arr[i + 1]) {
            // console.log(arr[i], arr[i + 1])
            consecList.push(arr[i], arr[i + 1]);
        }
    }

    return consecList;
}
function main() {
    const A = lines[0]
    const B = lines[1]
    
    const combined = A.concat(B).sort((a, b) => a - b);
    
    for (let i = 0; i < combined.length - 1; i++) {
        if (A.includes(combined[i]) && A.includes(combined[i + 1])) {
            console.log("Yes");
            return;
        }
    }
    console.log("No");
}
