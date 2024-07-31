const fs = require("fs");
const path = require("path");
const file_number = 3;

function zorome(number) {
    const str_count = new Set(number.toString()).size;
    return str_count === 1;
}

function Main(input) {
    input = input.split("\n");
    let N = Number(input[0]);
    let D = input[1].split(" ").map(Number);

    count = 0;
    for (i = 1; i <= N; i++) {
        for (j = 1; j <= D[i - 1]; j++) {
            if (zorome(`${i}${j}`)) {
                count++;
            }
        }
    }

    console.log(count);
}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
