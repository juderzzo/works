// Connor Oh and Jude Rizzo
// SoftDev1 pd9
// K#27 -- Sequential Progression
// 2019-12-11
var fibonacci = function(n){
  if(n==1) return 1;
  else if (n==2) return 1;
  else return (fibonacci(n-2) + fibonacci(n-1));
};

var max = function(x,y){
  if(x > y) return x;
  else return y;
};

var min = function(x,y){
  if(x > y) return y;
  else return x;
};

var gcd = function(a,b){
  m = max(a,b);
  n = min(a,b);
  if (m % n == 0) return n;
  else return gcd(n, m%n);
};

var list = ["connor", "leia", "grace", "jude"];

var randomStudent = function(){
  len = list.length;
  index = Math.floor(Math.random() * len);
  return list[index];
};

var fibonnaci = document.getElementById("one");
fibonnaci.addEventListener("click", function(){
  console.log(fibonacci(10));
});
fibonnaci.addEventListener("click", function(){
  document.getElementById("one").innerHTML = fibonacci(10);
});

var gcd1 = document.getElementById("two");
gcd1.addEventListener("click", function(){
  console.log(gcd(382,424));
});
gcd1.addEventListener("click", function(){
  document.getElementById("two").innerHTML = gcd(382,424);
});

var gcd2 = document.getElementById("three");
gcd2.addEventListener("click", function(){
  console.log(randomStudent());
});
gcd2.addEventListener("click", function(){
  document.getElementById("three").innerHTML = randomStudent();
});
