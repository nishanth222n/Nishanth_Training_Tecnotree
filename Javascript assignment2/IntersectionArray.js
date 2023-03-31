function arrayIntersection(arr1, arr2) {

  const obj = {};
  const intersection = [];

  for (let i = 0; i < arr1.length; i++) {
    obj[arr1[i]] = true;
  }

  for (let j = 0; j < arr2.length; j++) {
    if (obj[arr2[j]]) {
      intersection.push(arr2[j]);
    }
  }

  return intersection;
}

const arr1 = [1, 2, 3, 4];
const arr2 = [3, 4, 5, 6];
const intersection = arrayIntersection(arr1, arr2);
console.log(intersection); 

