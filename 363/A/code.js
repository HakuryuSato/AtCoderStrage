const fs = require("fs");
const path = require("path");
const file_number = 2;

function Main(input){
    input = input.split("\n");
    let R = Number(input[0])
    const result = Math.abs(R % 100 -100)

    console.log(result)




}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用