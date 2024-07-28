const fs = require("fs");
const path = require("path");
const file_number = 3;

function Main(input){
    input = input.split("\n");
    let N = Number(input[0])
    let lines = input.slice(1,input.length-1)

    let flag = false;
    for (let i = 0; i < N - 1; i++) {
        if (i !== N - 2 && lines[i] === "sweet" && lines[i + 1] === "sweet") {
            flag = true;
            break;
        }
    }

    if(flag){
        console.log('No')
    }else{
        console.log('Yes')
    }

}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用