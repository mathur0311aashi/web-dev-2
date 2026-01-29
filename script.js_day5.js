// let user = {
//     fullname:"S.P.Acharya",
//     address:"Gurugram",
//     mobile:123456789,
//     favcolor:["black", "white", "blue"],
    
    
// }

// console.log(user.fullname)

// let user = {
//     fullname:"S.P.Acharya",
//     address:{
//         city:"Gurugram",
//         state:"Haryana"
//     },
//     mobile:123456789,
//     favcolor:["black", "white", "blue"],
//     demo:function (){
//         return "demo function";
//     }
    
    
// }

// console.log(user.fullname, user.mobile, user.favcolor[i], user.demo(), user.address.city);

//return statement itself works as break statement
//object.keys in form of arrays return case

// console.log(object.entries)
//2-D array in entries key value form return case
//interview question
//[["x", "o","x"],
// ["o", "x", "o"],
// ["x", "o", "x"]]
// winner is x bcoz diagonally jo same hota h that is the answer

// o o x
// o x o
// o o x 
// o is the winner bcoz of column same h 




//object freeze and seal method
// const car = {
//     make: "Mahindra",
//     mdoe: "Thar"
// };
// car.color = "Black";
// console.log(car);


// const car = {
//     make: "Mahindra",
//     mdoe: "Thar"
// };
// object.seal(car);
// car.model = "XUV700";
// car.color = "Black";
// console.log(car);
//in this the we  cant add a new key and value pair but we can change or update existing values

const car = {
    make: "Mahindra",
    mdoe: "Thar"
};
Object.freeze(car);
car.color = "Black";
console.log(car);
//we cant add a new key and value pair also cant change or update existing values.