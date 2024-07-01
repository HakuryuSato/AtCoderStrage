// const readline = require('readline');
// const fs = require('fs');
// const path = require('path');

// const rl = readline.createInterface({
//     input: fs.createReadStream(path.join(__dirname, 'input2.txt')),
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
    if(lineCount === 0){
        N = Number(line);
    }else{
        H = line.split(' ').map(Number);
    }


    lineCount++;
}).on('close', () => {
    main();
});

function check(H) {
    let max = H[0];
    for (let i = 0; i < H.length; i++) {
        let h = H[i];
        // console.log(h, max);
        if (h > max) {
            return i+1;
        }
    }
    return -1;
}



function main() {
    // console.log(N,H)
    result = check(H)
    console.log(result)

    

}