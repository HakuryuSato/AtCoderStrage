const fs = require("fs");
const path = require("path");
const file_number = 1;

function Main(input){
    input = input.split("\n");
    let [N,X]=input[0].split(" ").map(Number)
    let S = input[1].split(" ").map(Number)

    sum=0
    S.map((s)=>{
        if(s<=X){
            sum+=s
        }
    })

    console.log(sum)



}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用