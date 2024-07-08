const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let text = '';

rl.on('line', (line) => {
    text = line;
}).on('close', () => {
    main();
});

function main() {
    const a = Number(text.split('ABC')[1]);
    
    if (a === 316 || a >= 350 || a===0) {
        console.log('No');
    } else {
        console.log('Yes');
    }
}
