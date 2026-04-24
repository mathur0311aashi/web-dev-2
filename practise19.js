// alert("alert box");
// console.log("Hello");   to show the alert in panel as log

arr = [1, 5, 8, 2, 9]
for (let i = 0; i < arr.length; i++) {
    while (arr[i] < arr[i + 1]) {
        let temp = arr[i + 1];
        arr[i + 1] = arr[i];
        arr[i] = temp;
    }
}
print(arr)