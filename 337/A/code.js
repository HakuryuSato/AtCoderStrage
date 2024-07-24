const fs = require("fs");
const path = require("path");
const file_number = 3;

function Main(input) {
    input = input.split("\n");
    let N = Number(input[0]);
    let lines = input.slice(1, N + 1);

    lines = lines.map((line) => {
        return line.split(" ").map(Number);
    });

    let A = 0;
    let B = 0;
    for (i = 0; i < N; i++) {
        A += lines[i][0];
        B += lines[i][1];
    }

    if (A === B) {
        console.log("Draw");
    } else if (A > B) {
        console.log("Takahashi");
    } else {
        console.log("Aoki");
    }
}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
