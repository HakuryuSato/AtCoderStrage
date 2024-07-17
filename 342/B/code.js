// テスト用 ---------------------------------------------------------------------------------------------------
// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");

// const file_number = 2;
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
    if (lineCount === 0) {
        N = Number(line);
    } else if (lineCount === 1) {
        P = line.split(" ").map(Number);
    } else if (lineCount === 2) {
        Q = Number(line);
    } else lines.push(line.split(" ").map(Number));

    lineCount++;
}).on("close", () => {
    main();
});

function main() {


    hairetu = []
    // console.log(N, P, Q, lines);
    for (i = 0; i < Q; i++) {
        for (j = 0; j < lines[i].length; j++) {
            lines[i][j]=P.indexOf(lines[i][j])
        }   
    }

    for (i = 0; i < Q; i++) {
        index=Infinity
        for (j = 0; j < lines[i].length; j++) {
            if(lines[i][j] < index){
                index=lines[i][j]
            }
        }   
    
        console.log(P[index])
    }



}
