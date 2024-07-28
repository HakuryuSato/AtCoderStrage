const fs = require("fs");
const path = require("path");
const file_number = 1;

function Main(input){
    input = input.split("\n");
    let [N,Q]=input[0].split(" ").map(BigInt)
    let A=input[1].split(" ").map(BigInt)
    let BK=input.slice(2,input.length-1)//.split(" ").map(BigInt)
    BK.forEach((pair, index) => {
        BK[index] = pair.split(' ').map(BigInt);
      });

}

Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
// Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用