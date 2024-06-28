// const readline = require('readline');
// const fs = require('fs');
// const rl = readline.createInterface({
//     input: fs.createReadStream('input1.txt'),
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
        [N,M] = line.split(' ').map(Number);
    }else if(lineCount === 1){
        A=line.split(' ').map(Number);
    }else{
        lines.push(line.split(' ').map(Number));   
    }




    lineCount++;
}).on('close', () => {
    main();
});


function sumColumnsReduce(arr) {
    return arr[0].map((_, colIndex) => // 列を指定
      arr.reduce((sum, row) => sum + row[colIndex], 0)
    );
  }


function main() {
    // console.log(N,M,A,lines);
    sumArray = sumColumnsReduce(lines);
    // console.log(sumArray);
    
    calculated=A.map((val,index)=>{
        if(val <= sumArray[index]){
            return true
        }else{
            return false
        }
    });

    result=calculated.every(val => val === true)
    if(result){
        console.log("Yes")
    }else{
        console.log("No")
    }
    

}