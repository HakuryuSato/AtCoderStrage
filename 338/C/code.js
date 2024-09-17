const fs = require("fs");
const path = require("path");
const file_number = 1;


function maxDishes(q, a, b) {
    function helper(q) {
        if ((q[0] < a[0] || q[1] < a[1]) && (q[0] < b[0] || q[1] < b[1])) {
            return 0;
        }

        let maxCount = 0;

        if (q[0] >= a[0] && q[1] >= a[1]) {
            const newQ = [q[0] - a[0], q[1] - a[1]];
            maxCount = Math.max(maxCount, 1 + helper(newQ));
        }

        if (q[0] >= b[0] && q[1] >= b[1]) {
            const newQ = [q[0] - b[0], q[1] - b[1]];
            maxCount = Math.max(maxCount, 1 + helper(newQ));
        }

        return maxCount;
    }

    return helper(q);
}

function Main(input) {
    input = input.split("\n");
    const n = Number(input[0]);
    const q = input[1].split(" ").map(Number);
    const a = input[2].split(" ").map(Number);
    const b = input[3].split(" ").map(Number);

    console.log(maxDishes(q,a,b))
}

// Main(fs.readFileSync(path.join(__dirname, `input${file_number}.txt`), "utf8")); // テスト用
Main(require("fs").readFileSync("/dev/stdin", "utf8")); // 本番用
