const fs = require("fs");
const path = require("path");
const file_number = 2;

function calc_length(P, ST) {
    let S = P.indexOf(ST[0]);
    let T = P.indexOf(ST[1]);
    let directDist = Math.abs(S - T);
    let wrapDist = P.length - directDist;
    return Math.min(directDist, wrapDist);
}

function Main(input) {
    input = input.split("\n");
    s = input[0].split("");
    t = input[1].split("");

    P = ["A", "B", "C", "D", "E"];

    if (calc_length(P, s) === calc_length(P, t) || s === t) {
        console.log("Yes");
    } else {
        console.log("No");
    }
}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
