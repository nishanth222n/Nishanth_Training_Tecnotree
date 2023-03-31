function binarySearch(arr, target) {
    let low = 0;
    let high = arr.length - 1;
  
    while (low <= high) {
      let mid = Math.floor((low + high) / 2);
      if (arr[mid] === target) {
        return mid;
      } else if (arr[mid] < target) {
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }
  
    return -1;
  }

const numbers = [1, 2, 3, 4, 5];
const target = 4;
const index = binarySearch(numbers, target);
console.log(index); // Output: 3
