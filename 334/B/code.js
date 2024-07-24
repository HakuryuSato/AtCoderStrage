const fs = require("fs");
const path = require("path");
const file_number = 1;

function Main(input) {
    input = input.split("\n");
    let [A, M, L, R] = input[0].split(" ").map(BigInt);

    // AからMmおきにツリーを立てる
    // LRの間に建てられるツリー数

    let sabun = (L-A) - (R-A);
    let sabunAbs = sabun < 0 ? -sabun : sabun;
    let result = sabunAbs / M

    console.log(result);
}

Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
// Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
