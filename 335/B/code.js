const fs = require("fs");
const path = require("path");
const file_number = 2;

function Main(input){
    input = input.split("\n");
    const N=input[0]+'00'
    let Num = N.toString(N)
    let i = '0'.toString(N)
    
   while(Num.toString(N)<=N.toString(N)){
        Num.toString(N)+'1'.toString(N)
        console.log(Num.toString(N))
   }


}

Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
// Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用