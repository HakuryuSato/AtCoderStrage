const fs = require("fs");
const path = require("path");
const file_number = 1;

function Main(input){
    input = input.split("\n");
    let [N,L]= input[0].split(" ").map(Number)
    let A = input[1].split(" ").map(Number)
    
    let count =0;
    A.map((a)=>{
        if(a>=L){
            count++
        }
    })

    console.log(count)




}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用