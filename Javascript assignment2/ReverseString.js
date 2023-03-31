function reverseWords(str) {
  
    let words = str.split(" ");
  
    words = words.reverse();
  
    let reversedStr = words.join(" ");
  
    return reversedStr;
  }
  
  console.log(reverseWords("Hi Varsha")); 
  console.log(reverseWords("The quick brown fox jumps over the lazy dog.")); // Output: "dog. lazy the over jumps fox brown quick The"
  