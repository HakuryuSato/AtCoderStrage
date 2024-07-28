const fs = require("fs");
const path = require("path");
const file_number = 3;

function counter(A,X){
    sum=0n
    count=0

    for (const a of A) {
        sum += a;
        count++;
        if (sum > X) {
            break;
        }
    }

    return count;
}


function Main(input){
    input = input.split("\n");
    let [N,X,Y] = input[0].split(" ").map(BigInt)
    let A = input[1].split(" ").map(BigInt).sort((a, b) => (a > b ? -1 : 1));
    let B = input[2].split(" ").map(BigInt).sort((a, b) => (a > b ? -1 : 1));
    
    Acount=counter(A,X)
    Bcount=counter(B,Y)

    if(Acount<=Bcount){
        console.log(Acount)
    }else{
        console.log(Bcount)
    }



}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用