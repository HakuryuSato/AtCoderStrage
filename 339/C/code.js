const fs = require("fs");
const path = require("path");
const file_number = 1;

function Main(input) {
    input = input.split("\n");
    let N = BigInt(input[0]);
    let A = input[1].split(" ").map(BigInt);
    console.log(N, A);
    result = 0n
    for(i=0;i<N;i++){
        result+=A[i]
    }
    
    if(result>=0n){
        console.log(result.toString())
    }else{
        console.log("0")
    }
}

Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
// Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
