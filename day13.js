// //1. synchronous code will execute first then asynchronous code
console.log("a");
setTimeout(() => {
    console.log("b");
}, 5000)
setTimeout(() => {
    console.log("c");
}, 1000)
setTimeout(() => { 
    console.log("d");
}, 2000)
console.log("e");
// isme according to time jiska kam time h pehle wo print hoga and then uske baad in increasing order jaise jaise time limit increase hoti jayegi usi order me printing of output will also take place
// iska output h
// a, e, c, d, b

// function sample(callback)
// in this function now ek ek krke a, b, c, d, e print honge one after another bcoz time limit sbki same h 
// setTimeout(() => {
//     console.log("a");
//     setTimeout(() => {
//         console.log("b");
//         setTimeout(() => {
//             console.log("c");
//             setTimeout(() => {
//                 console.log("d");
//                 setTimeout(() => {
//                     console.log("e");
//                 }, 1000)
//             },1000)
//         }, 1000)
//     }, 1000)
// }, 1000)
    