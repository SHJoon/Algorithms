// PopFront
// Given an array, remove and return the value at
// the beginning of the array. Do this without using
// any built-in array methods except pop().

function popFront(arr){
    for(var i = 0; i < arr.length - 1; i++) {
        arr[i] = arr[i + 1];
    }
    arr.pop();
}

myArr = [0,1,2,3];
popFront(myArr);
console.log(myArr);