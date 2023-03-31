function findNthLargest(arr, n) {
    // Sort the array in descending order
    arr.sort(function(a, b) {
      return b - a;
    });
  
    // Return the nth largest element
    return arr[n - 1];
  }

const numbers = [3, 2, 8, 5, 1, 4];
const nthLargest = findNthLargest(numbers, 3);
console.log(nthLargest); // Output: 4
