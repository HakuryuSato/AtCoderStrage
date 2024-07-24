const fs = require("fs");
const path = require("path");
const file_number = 3;

function check(S) {
    if (S[0] == S[0].toUpperCase() && S.length === 1) return true;
    if (S[0] !== S[0].toUpperCase()) return false;

    for (i = 1; i < S.length; i++) {
        if (S[i] !== S[i].toLowerCase()) {
            return false;
        }
    }
    return true;
}

function Main(input) {
    input = input.split("\n");
    S = input[0];
    if (check(S)) {
        console.log("Yes");
    } else {
        console.log("No");
    }
}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
