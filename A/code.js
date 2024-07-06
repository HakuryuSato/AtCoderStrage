// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");

// const rl = readline.createInterface({
//     input: fs.createReadStream(path.join(__dirname, "input2.txt")),
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
    [N, X, Y, Z] = line.split(" ").map(Number);

    lineCount++;
}).on("close", () => {
    main();
});

function contains(X,Y,Z) {
    let start = Math.min(X,Y);
    let end = Math.max(X,Y);
    return start <= Z && Z <= end;
}

function main() {
    // console.log(N,X,Y,Z)
    if(contains(X,Y,Z)){
        console.log("Yes")
    }else{
        console.log("No")
    }
}
