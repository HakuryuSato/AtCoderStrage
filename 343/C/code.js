// テスト用 ---------------------------------------------------------------------------------------------------
const readline = require("readline");
const fs = require("fs");
const path = require("path");

const file_number = 1;
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
lines = [];
rl.on("line", (line) => {
    N = BigInt(line);

    lineCount++;
}).on("close", () => {
    main();
});

function isPalindrome(num) {
    const str = num.toString();
    const len = str.length;
    for (let i = 0; i < len / 2; i++) {
        if (str[i] !== str[len - 1 - i]) {
            return false;
        }
    }
    return true;
}

// 数字が立方数かどうかをバイナリサーチで確認する関数
function isCube(num) {
    let low = 0n, high = num;
    while (low <= high) {
        let mid = (low + high) / 2n;
        let cube = mid ** 3n;
        if (cube === num) {
            return true;
        } else if (cube < num) {
            low = mid + 1n;
        } else {
            high = mid - 1n;
        }
    }
    return false;
}

function findMaxPalindromeCube(N) {
    for (let i = N; i >= 1n; i--) {
        if (isPalindrome(i) && isCube(i)) {
            return i;
        }
    }
    return -1n; // 見つからない場合
}

function main() {
    // x^3=kを満たす
    // nよりも小さく
    console.log(N);

    console.log(findMaxPalindromeCube(N).toString());
}
