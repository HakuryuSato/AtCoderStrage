const { countReset } = require("console");
const fs = require("fs");
const path = require("path");
const file_number = 3;



function Main(input) {
    input = input.split("\n");
    let S = input[0];
    let S_list = Array.from(input[0]).sort();
    let SList = new Set(S_list);

    let maxWord = "";
    let max = 0;
    

    for (char of SList) {
        let count = 0

        count = S.split(char).length - 1;
        // console.log(count)
        if (count > max) {
            maxWord = char;
            max = count
        }
    }

    console.log(maxWord);
}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
