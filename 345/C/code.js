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


// // 本番用 ---------------------------------------------------------------------------------------------------
// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });




lineCount = 0;
lines=[];
rl.on("line", (line) => {
    S=line


    lineCount++;
}).on("close", () => {
    main();
});

function ikuzo(){
    // 整数の組 1<= i<j <=N
    
    // 全て同じ文字なら1種類なので終了
    
    // i,jが同じなら1
    


    }


function main() {
    // console.log(S)
    // 同じ文字列で良い？
    // 次の操作をちょうど1回行った後の文字列としてあり得るものがいくつあるか
    // Sの長さをNとする、1<=i<j<=Nを満たす整数の組(i,j)を選び、Sのi文字目とj文字目を入れ替える
    // console.log()

    N=S.length
    console.log(S,N)


}
