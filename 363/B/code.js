const fs = require("fs");
const path = require("path");
const file_number = 3;

function check(T, P, lines) {
    let count = 0;
    lines.map((line) => {
        if (line >= T) {
            count++;
        }
    });

    if (count >= P) {
        return true;
    } else {
        return false;
    }
}

function add(lines) {
    let newLines = lines.map((line) => {
        return line + 1;
    });

    return newLines
}

function check_main(T, P, lines) {
    if (check(T, P, lines)) {
        return 0;
    }

    let dayCount = 0;
    while (true) {
        if (check(T, P, lines)) {
            break;
        } else {
            lines = add(lines);
            dayCount++;
        }
    }

    return dayCount;
}

function Main(input) {
    input = input.split("\n");
    let [N, T, P] = input[0].split(" ").map(Number);
    let lines = input[1].split(" ").map(Number);
    console.log(check_main(T, P, lines));
}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
