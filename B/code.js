// const readline = require("readline");
// const fs = require("fs");
// const path = require("path");

// const rl = readline.createInterface({
//     input: fs.createReadStream(path.join(__dirname, "input1.txt")),
//     output: process.stdout,
// });

// 本番用*************************************************************************
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
// 本番用*************************************************************************

let lineCount = 0;
let obj = {};

rl.on("line", (line) => {
    if (lineCount === 0) {
        N = Number(line);
        // console.log(N);
    } else {
        const [key, value] = line.split(" ");
        obj[key] = parseInt(value, 10);
    }

    lineCount++;
}).on("close", () => {
    main();
});

function main() {
    // console.log(N, obj);
    const sum = Object.values(obj).reduce((acc, value) => acc + value, 0);
    mod = sum % N;
    let foundKey;

    const sortedObj = Object.keys(obj) // 昇順
        .sort()
        .reduce((acc, key) => {
            acc[key] = obj[key];
            return acc;
        }, {});


        let keys = Object.keys(sortedObj);

        for (let i = 0; i < keys.length; i++) {
        //   console.log(keys[i], obj[keys[i]]);
          if(i===mod){
            result = keys[i];
          }
        }

    // console.log(sum, mod);
    // console.log(obj[mod]);
    console.log(result);
}
