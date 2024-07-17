const fs = require("fs");
const path = require("path");
const file_number = 3;

function Main(input){
    input = input.split("\n");
    const N = Number(input[0]);
    const result = '1'+ '01'.repeat(N)
    console.log(result)


}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用