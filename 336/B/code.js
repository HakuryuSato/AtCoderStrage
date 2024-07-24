const fs = require("fs");
const path = require("path");
const file_number = 3;


function ctz(N){
    return (N & -N).toString(2).length -1


}

function Main(input){
    input = input.split("\n");
    let N=Number(input[0])
    console.log(ctz(N))

}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用