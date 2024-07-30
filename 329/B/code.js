const fs = require("fs");
const path = require("path");
const file_number = 3;

function Main(input){
    input = input.split("\n");
    A=new Set(input[1].split(" ").map(Number))
    let sortedA= Array.from(A).sort((a, b) => b - a);
    console.log(sortedA[1])




}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用