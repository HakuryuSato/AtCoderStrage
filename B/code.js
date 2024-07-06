const readline = require("readline");
const fs = require("fs");
const path = require("path");

const rl = readline.createInterface({
    input: fs.createReadStream(path.join(__dirname, "input2.txt")),
    output: process.stdout,
});



let lineCount = 0;
let lines = [];
rl.on("line", (line) => {
    if (lineCount === 0) {
        S = line.split("");
    } else {
        T = line.split("");
    }

    lineCount++;
}).on("close", () => {
    main();
});

function main() {
    // console.log(S, T);
    let startIndex = 0;
    const indices = S.map(element => {
      const index = T.indexOf(element, startIndex);
      startIndex = index + 1;
      return index;
    });

    const incrementedIndices = indices.map(element => element + 1)
    console.log(incrementedIndices.join(" "));
}
