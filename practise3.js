// map method
// let num = [1, 2, 3];
// let doubled = num.map((bhavesh)=>bhavesh*2);
// console.log(doubled);

// filter method
// let marks = [7, 23, 34, 54];
// let result = marks.filter(marks=>marks>20);
// console.log(result);

// print the message of pass and fail for the students marks

// let marks = [7, 40, 53, 87];
// let result = marks.filter(marks=>{
//     if (marks>=40){
//         console.log("pass", marks);
//     }else{
//             console.log("fail", marks);
//         }
// })

// sum of all elements of an array
let num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let sum = 0;
for (let i=0; i<num.length; i++){
    sum+=num[i];
}
console.log(sum);

// by reduce method
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let res = num.reduce((acc, current)=>acc+current)
console.log(res);