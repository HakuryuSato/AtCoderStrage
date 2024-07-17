// テスト用 ---------------------------------------------------------------------------------------------------
// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");

// const file_number = 3;
// const file = `input${file_number}.txt`;

// const rl = readline.createInterface({
//     input: fs.createReadStream(path.join(__dirname, file)),
//     output: process.stdout,
// });

// // 本番用 ---------------------------------------------------------------------------------------------------
// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

lineCount = 0;
lines = [];
rl.on("line", (line) => {
    if (lineCount === 0) {
        N = Number(line);
    } else if (lineCount === 1) {
        S = line;
    } else if (lineCount === 2) {
        Q = Number(line);
    } else {
        lines.push(line.split(" "));
    }

    lineCount++;
}).on("close", () => {
    main();
});

function main() {
    // console.log(N, S, Q, lines);
    lines = new Set(lines.map(pair => pair.join(',')));

    for (i = 0; i < Q; i++) {
        // console.log(i)

        S = S.replace(new RegExp(lines[i][0], 'g'), lines[i][1]);
    }
    console.log(S);
}
