// const readline = require('readline');
// const fs = require('fs');
// const rl = readline.createInterface({
//     input: fs.createReadStream('input2.txt'),
//     output: process.stdout
// });



// 本番用*************************************************************************
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin, 
    output: process.stdout
}); 
// 本番用*************************************************************************



let lineCount = 0;
let lines = []
rl.on('line', (line) => {
    // console.log(line)

    if (lineCount == 0) {
        [N, M] = line.split(" ").map(Number);
    } else {
        lines = (line.split(" ").map(Number));
    }



    lineCount++;
}).on('close', () => {
    main();
});


function main() {
    // console.log(N, M, lines)

    ailianCount = 0

    for (i = 0; i < N; i++) {
        M = M - lines[i]
        // console.log(M, lines[i])

        if (M < 0) {
            break
        } else {
            ailianCount++
        }
    }

    console.log(ailianCount)




}