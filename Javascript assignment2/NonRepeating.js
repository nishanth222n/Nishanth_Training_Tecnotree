function findFirstNonRepeatingChar(str) {
    let charMap = {};
    for (let char of str) {
      if (!charMap[char]) {
        charMap[char] = 1;
      } else {
        charMap[char]++;
      }
    }
    for (let char of str) {
      if (charMap[char] === 1) {
        return char;
      }
    }
    return null;
  }

 let str = "aabbcddc";
console.log(findFirstNonRepeatingChar(str)); 
