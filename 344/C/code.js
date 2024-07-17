// テスト用 ---------------------------------------------------------------------------------------------------
// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");

// const file_number= 1
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
    if(lineCount%2===1){
        lines.push(line.split(" ").map(Number));
    }


    lineCount++;
}).on("close", () => {
    main();
});



function main() {
    // console.log(lines)
    A=lines[0]
    B=lines[1]
    C=lines[2]
    X=lines[3]

    // console.log(A,B,C)
    set = new Set()    
    for (const a of A) {
        for (const b of B) {
            for (const c of C) {
                set.add(a + b + c);
            }
        }
    }
    // console.log(set)

    for ( const x of X){
        if(set.has(x)){
            console.log("Yes")
        }else{
            console.log("No")
        }
    }

}
