const fs = require("fs");
const path = require("path");
const file_number = 3;

function Main(input){
    input = input.split("\n");
    let S = input[0]
    let splittedS = S.split(".")
    console.log(splittedS[splittedS.length-1])
    






}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用

Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用