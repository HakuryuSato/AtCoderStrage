const fs = require("fs");
const path = require("path");
const file_number = 2;

function Main(input){
    input = input.split("\n");
    // console.log(input)
    const [A,B,D] = input[0].split(" ").map(Number)
    // console.log(A,B,D)

    list = []
    for(i=A;i<=B;i+=D){
        list.push(i)
    }

    console.log(list.join(' '))






}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用

Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用