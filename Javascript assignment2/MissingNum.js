function findMissingNumber(arr) {
    let n = arr.length + 1;
    let sum = (n * (n + 1)) / 2;
    let arrSum = arr.reduce((a, b) => a + b, 0);
    return sum - arrSum;
  }

 let arr = [1, 2, 4, 5, 6];
console.log(findMissingNumber(arr)); 
