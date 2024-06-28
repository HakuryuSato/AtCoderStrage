// const readline = require('readline');
// const fs = require('fs');
// const rl = readline.createInterface({
//     input: fs.createReadStream('input0.txt'),
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

        [N, L, R] = line.split(' ').map(Number);




    lineCount++;
}).on('close', () => {
    main();
});


function reverseSubArray(arr, start, end) {
    let subArray = arr.slice(start, end + 1).reverse();
    
    return [...arr.slice(0, start), ...subArray, ...arr.slice(end + 1)];
  }

function createList(N){
    return Array.from({ length: N }, (v, i) => i + 1);
}

function main() {


    list=createList(N);

    
    result=reverseSubArray(list, L-1, R-1);
    text = result.join(' ')

    console.log(text)
    

}