const fs = require("fs");
const path = require("path");
const file_number = 1;

function Main(input) {
    input = input.split("\n");

    lines = [];
    for (i = 1; i < input.length - 1; i++) {
        query = input[i].split(" ");
        if (query[0] == 1) {
            lines.push(query[1]);
        } else {
            console.log(lines[lines.length - query[1]]);
        }
    }
}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
