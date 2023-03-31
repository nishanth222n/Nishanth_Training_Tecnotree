function arraySum(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
      if (typeof arr[i] === 'number') {
        sum += arr[i];
      }
    }
    return sum;
  }

  const numbers = [1, 2, 3, 4, 5];
const sum = arraySum(numbers);
console.log(sum); // Output: 15
