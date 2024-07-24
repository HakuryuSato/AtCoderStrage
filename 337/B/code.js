const fs = require("fs");
const path = require("path");
const file_number = 5;

function Main(input) {
    input = input.split("\n");
    S = input[0];

    sortedS = S.split('').sort().join('');
    if(S===sortedS){
        console.log('Yes')
    }else{
        console.log('No')
    }


}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
