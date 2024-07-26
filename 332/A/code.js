const fs = require("fs");
const path = require("path");
const { allowedNodeEnvironmentFlags } = require("process");
const file_number = 3;

function Main(input) {
    input = input.split("\n");
    const [n, s, k] = input[0].split(" ").map(Number);
    let lines = input.slice(1, input.length - 1);

    let sum = 0;

    lines.map((line) => {
        let subTotal = 0;
        let P = Number(line.split(" ")[0]);
        let Q = Number(line.split(" ")[1]);

        subTotal = P * Q;
        sum += subTotal;
    });

    if(sum < s){
        sum += k
    }

    console.log(sum)
}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
