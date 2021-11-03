function countdown(startNum, endNum){
  if (startNum === endNum){
      return [startNum]
  }
  else if (startNum > endNum){
  	return reverseCountArray
  } else {
    var count = countdown(startNum, endNum - 1);
    count.push(endNum)
    return count
  }
}
