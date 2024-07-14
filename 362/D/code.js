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

// テスト用 ---------------------------------------------------------------------------------------------------

// // 本番用 ---------------------------------------------------------------------------------------------------
// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });
// // 本番用 ---------------------------------------------------------------------------------------------------




lineCount = 0;
U=[];
rl.on("line", (line) => {
    if(lineCount===0){
        [N,M]=line.split(" ").map(BigInt);
    }else if(lineCount===1){
        A=line.split(" ").map(BigInt);
    }else{
        U.push(line.split(" ").map(BigInt));
    }


    lineCount++;
}).on("close", () => {
    main();
});




function main() {
    console.log(N,M,A,U)

    // キューを作成

    // 隣接ノードの重みを計算

    // キューを更新

}
