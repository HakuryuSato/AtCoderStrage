// // テスト用 ---------------------------------------------------------------------------------------------------
// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");
// const { escape } = require("querystring");

// const file_number= 0
// const file = `input${file_number}.txt`;

// const rl = readline.createInterface({
//     input: fs.createReadStream(path.join(__dirname, file)),
//     output: process.stdout,
// });

// テスト用 ---------------------------------------------------------------------------------------------------
<<<<<<< HEAD
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



=======

// 本番用 ---------------------------------------------------------------------------------------------------
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
// 本番用 ---------------------------------------------------------------------------------------------------
>>>>>>> 69a46a0590f1d73fd614f2c9a932633b40fdc161

lineCount = 0;
lines=[];
rl.on("line", (line) => {
<<<<<<< HEAD
    if(lineCount===0){
        N=Number(line);
    }else{
        lines.push(line.split(" ").map(Number));
=======
    if (lineCount === 0) {
        S = line.split("");
    } else {
        T = line.toLowerCase().split("");
>>>>>>> 69a46a0590f1d73fd614f2c9a932633b40fdc161
    }



    lineCount++;
}).on("close", () => {
    main();
});

<<<<<<< HEAD
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

    
=======
function main() {
    // console.log(S,T)
    successCount = 0;
    result = "";
    formerIndex = -1;

    // 文字が含まれているかを判定
    for (let t of T) {
        charIndex = S.indexOf(t); // T文字のインデックスを取得

        if (charIndex === -1) { // 文字が含まれていないなら終了
            result = "No";
            break;
        } else if (charIndex > formerIndex) { // 前のインデックスより後になっているか
            formerIndex = charIndex; // 今のインデックスを代入
            successCount++;
        }
    }

    if (T[2] == "x" || successCount >= 2) {
        result = "Yes";
    } else if (successCount === T.length) {
        result = "Yes";
    } else {
        result = "No";
    }

    console.log(result);
>>>>>>> 69a46a0590f1d73fd614f2c9a932633b40fdc161
}
