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

// 本番用 ---------------------------------------------------------------------------------------------------
const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
// 本番用 ---------------------------------------------------------------------------------------------------

lineCount = 0;
lines = [];
rl.on("line", (line) => {
    if (lineCount === 0) {
        S = line.split("");
    } else {
        T = line.toLowerCase().split("");
    }

    lineCount++;
}).on("close", () => {
    main();
});

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
}
