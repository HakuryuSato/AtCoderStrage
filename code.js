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
    text=line



    lineCount++;
}).on('close', () => {
    main();
});


function convertTextBasedOnCase(text) {
    let upperCount = 0;
    let lowerCount = 0;

    for (let char of text) {
        if (char === char.toUpperCase() && char !== char.toLowerCase()) {
            upperCount++;
        } else if (char === char.toLowerCase() && char !== char.toUpperCase()) {
            lowerCount++;
        }
    }

    if (upperCount > lowerCount) {
        return text.toUpperCase();
    } else {
        return text.toLowerCase();
    }
}



function main() {
    // console.log(text)


    result = convertTextBasedOnCase(text)
    console.log(result)
    

}