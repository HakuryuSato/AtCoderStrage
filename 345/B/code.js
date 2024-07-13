// テスト用 ---------------------------------------------------------------------------------------------------
// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");

// const file_number = 3;
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
lines = [];

rl.on("line", (line) => {
    X = BigInt(line);

    lineCount++;
}).on("close", () => {
    main();
});

function ceilDiv(x, y) {
    if (x >= 0n) {
      return (x + y - 1n) / y;
    } else {
      return x / y;
    }
  }

function main() {
    // console.log(X);

    result = ceilDiv(X, 10n);

    console.log(result.toString());
}
