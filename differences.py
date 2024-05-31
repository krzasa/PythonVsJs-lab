#  Get name 
# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };

def getName():
    name = input("What is your name? ")
    print('Hi ' +name)

# getName()


# Reverse it 

# const reverseIt = () => {
#   let string = "a man, a plan, a canal, frenemies!";

#   let reverse = "";

#   for (let i=0; i < string.length; i++) {
#     reverse += string[string.length - (i+1)];
#   };

#   alert(reverse);
# };

def reverseIt():
    string = "a man, a plan, a canal, frenemies!"
    reverse = ""
    for i in range(len(string)):
        reverse += string[len(string) - (i+1)]
    print(reverse)


# reverseIt()

# Swap Em
# const swapEm = () => {
#   let a = 10;
#   let b = 30;
#   let temp;

#   temp = b;
#   b = a;
#   a = temp;

#   alert("a is now " + a + ", and b is now " + b);
# };

def swapEm ():
    a = 10
    b = 30

    temp = 0
    temp = b

    b = a
    a = temp

    print("a is now " + str(a) + ", and b is now " + str(b))

# swapEm()

# Multiply Array/List

# const multiplyArray = (ary) => {
#   if (ary.length == 0) { return 1; };

#   let total = 1;
#   // let total = ary[0];

#   for (let i=0; i < ary.length; i++) {
#     total = total * ary[i];
#   };

#   return total;
# };

# arr = [1,2,3,4,5,6,7,8,9,10]

def multiplyArray(ary):
    if len(ary) == 0:
        return 1

    total = 1

    for i in range(len(ary)):
        total *= ary[i]

    print(total)

# multiplyArray(arr)

# Fizz Buzzer

# const fizzbuzzer = (x) => {
#   if( x%(3*5) == 0 ) {
#     return 'fizzbuzz'
#   } else if( x%3 == 0 ) {
#     return 'fizz'
#   } else if ( x%5 == 0 ) {
#     return 'buzz'
#   } else {
#     return 'archer'
#   }
# }

def fizzbuzzer(x):
    if x % (3*5) == 0:
        print('fizzbuzz')
    elif x % 3 == 0:
        print('fizz')
    elif x % 5 == 0:
        print('buzz')
    else:
        print('archer')
# fizzbuzzer(12)

# Nth Fibonacci
# const nthFibonacciNumber = () => {
#   let fibs = [1, 1];
#   let num = prompt("which fibonacci number do you want?");

#   while (fibs.length < parseInt(num)) {
#     let length = fibs.length;
#     let nextFib = fibs[length - 2] + fibs[length - 1];
#     fibs.push(nextFib);
#   }

#   alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
# };

def nthFibonacciNumber():
    fibs = [1, 1]
    num = int(input("Which fibonacci number do you want? "))

    while len(fibs) < num:
        length = len(fibs)
        nextFib = fibs[length - 2] + fibs[length - 1]
        fibs.append(nextFib)

    print(str(fibs[len(fibs) - 1]) + " is the fibonacci number at position " + str(num))

# nthFibonacciNumber()

# Search Array/List

# const searchArray = (array, value) => {
#   for(let i = 0; i < array.length-1; i++) {
#     if(array[i] == value) {
#       return true;
#       break;
#     }
#   }
#   return -1;
# };

def searchArray(array, value):
    state = "True"
    for i in range(len(array)-1):
        if array[i] == value:
            state = True
            break
        else:
            state = False
    print(state)       
arr = [1,2,3,4,5,6,7,8,9,10]
# searchArray(arr,12)
    
#  Palindrome
# const isPalindrome = (str) => {
#   for(let i = 0; i < str.length/2; i++){
#     if(str[i] != str[str.length-i-1]){
#       return false;
#       break;
#     }
#   }
#   return true;
# };

def isPalindrome(str):
    for i in range(len(str)//2):
        if str[i] != str[len(str)-i-1]:
            print(False)
            break
    else:
        print(True)

# isPalindrome("refer")

# hasDupes

# const hasDupes = (arr) => {
#   let obj = {};
#   for (i = 0; i < arr.length; i++) {
#     if(obj[arr[i]]) {
#       return true;
#     }
#     else {
#       obj[arr[i]] = true;
#     }
#   }
#   return false;
# };

def hasDupes(arr):
    obj = {}
    for i in range(len(arr)):
        if arr[i] in obj:
            print(True)
            break
        else:
            obj[arr[i]] = True
    else:
        print(False)

arr2 = [1,2,3,4,5,6,7,8,8,9,10]

hasDupes(arr2)