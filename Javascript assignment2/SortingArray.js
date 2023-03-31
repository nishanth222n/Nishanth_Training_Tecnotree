function sortArrayOfObjects(arr, prop) {

    arr.sort(function(a, b) {
      if (a[prop] < b[prop]) {
        return -1;
      }
      if (a[prop] > b[prop]) {
        return 1;
      }
      return 0;
    });
  
  
    return arr;
  }
  const people = [
    { name: 'Harsha', age: 18 },
    { name: 'Varsha', age: 50 },
    { name: 'Kruthik', age: 20 },
    { name: 'Rahul', age: 19 }
  ];
  
  const sortedPeople = sortArrayOfObjects(people, 'age');
  console.log(sortedPeople);
 