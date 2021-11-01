function convertToRoman(num) {
 function ones(number){
   if (num === 0){  return ''; }
   else if (number < 4){ return "I".repeat(number); }
   else if (number === 4){ return "IV"; }
   else if (number === 5){ return "V"; }
   else if (number < 9) { return "V" + ("I".repeat((number - 5)));}
  else { return "IX"; }
 }

 function tens(number){
   if (number === 0){ return '';}
   else if (number < 40){ return 'X'.repeat(Math.floor    (number/10));}
   else if (number === 40){ return 'XL'; }
   else if (number === 50){ return 'L'; }
   else if (number < 90) { return 'L' + 'X'.repeat(Math.floor((number-50)/10)); }
   else{ return 'XC'; }
  }

function hundreds(number){
  if (number === 0){ return ''; }
  else if (number < 400){ return 'C'.repeat(Math.floor(number/100)); }
  else if (number === 400) { return 'CD'; }
  else if (number === 500) {return 'D';}
  else if (number < 900) { return 'D' + 'C'.repeat(Math.floor((number-500)/ 100));}
  else{ return 'CM';}
  }
function thousands(number){
  if (number === 0) {return '';}
  else if (number < 4000) {return 'M'.repeat(Math.floor(number/1000))}
  
}


  if (num < 10){
    return ones(num);
  }
  else if (num < 100){
    return tens(num - (num%10)) + ones(num%10);
  }
  else if (num < 1000){
    return hundreds(num - (num%100)) + tens ((num%100) - (num%10)) + ones(num%10);
  }
  else{
    return thousands(num-(num%1000)) + hundreds((num%1000) - (num%100)) + tens ((num%100) - (num%10)) + ones(num%10);
  }
}

convertToRoman(36);
