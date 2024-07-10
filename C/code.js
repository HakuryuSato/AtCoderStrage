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
    if(lineCount===0){
        N=Number(line);
    }else{
        lines.push(line.split(" ").map(Number));
    }



    lineCount++;
}).on("close", () => {
    main();
});

function getMaxOfMinValues(lines) {
    let result = [];

    lines.forEach(line => { // 最小値を求める
        let value = line[0];
        let key = line[1];

        if (!result[key] || value < result[key]) {
            result[key] = value;
        }
    });

    // 最小値リストの中から最大値を求める
    let maxValue = Math.max(...Object.values(result));
    return maxValue;
}

function main() {
    // console.log(N,lines)

    console.log(getMaxOfMinValues(lines))

    
}
