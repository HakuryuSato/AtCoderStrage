const fs = require("fs");
const path = require("path");
const file_number = 3;

function Main(input) {
    input = input.split("\n");
    let [M, D] = input[0].split(" ").map(Number);
    let [y, m, d] = input[1].split(" ").map(Number);

    if (d + 1 <= D) {
        console.log(y, m, d + 1);
    } else if (m + 1 <= M) {
        console.log(y, m + 1, 1);
    } else {
        console.log(y + 1, 1, 1);
    }
}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
