const fs = require("fs");
const path = require("path");
const file_number = 2;

function Main(input) {
    input = input.split("\n");
    let N = Number(input[0]);
    let A = input[1].split(" ").map(Number);

    for (i = 0; i < N; i++) {


        sum=0;
        A.map((a)=>{
            if(a>A[i]){
                sum+=a
            }
        })

        console.log(sum)
    }
}

Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
// Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
