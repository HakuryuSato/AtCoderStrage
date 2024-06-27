const readline = require('readline');
const fs = require('fs');
const rl = readline.createInterface({
    input: fs.createReadStream('input0.txt'),
    output: process.stdout
});



// // 本番用*************************************************************************
// const readline = require('readline');
// const rl = readline.createInterface({
//     input: process.stdin, 
//     output: process.stdout
// }); 
// // 本番用*************************************************************************



let lineCount = 0;
let lines = []
rl.on('line', (line) => {



    lineCount++;
}).on('close', () => {
    main();
});


function main() {


    

}