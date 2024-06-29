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

    [a,b] = line.split(' ').map(Number);

    lineCount++;
}).on('close', () => {
    main();
});


function main() {
    // console.log(num)
    result=0
    if(a===b){
        result =  -1
    }else{
        result = 6 - a - b;
    }
    
    console.log(result)
    
}