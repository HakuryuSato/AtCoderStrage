const fs = require("fs");
const path = require("path");
const file_number = 3;

function Main(input){
    input = input.split("\n");
    let S=input[0].toString()
    S=S.slice(0,-1) + '4'


    console.log(S)


}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用