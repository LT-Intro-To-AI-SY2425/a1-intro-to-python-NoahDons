# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"



"""Print the fibonacci sequence up to the number n"""
def fibonacci(n):

    curNum = 1
    lastNum = 0
    print(lastNum)
    if n >1:
        print(curNum)
        

    while curNum < n:
        
        print(curNum+lastNum)
        temp = lastNum
        lastNum = curNum
        curNum = temp+curNum
    


"Print all prime numbers less than or qual to the number n"

def prime(n):
    
    curnum = 0    
    while curnum<=n:
        isPrime = True
        for i in range(2, curnum):
            if curnum%i == 0:
                isPrime = False
        if isPrime:
            print(curnum)
        curnum+=1


""" Even-Odd Number Sum"""
def EvenOdd(n):
    sumodd = 0
    sumeven = 0

    for i in range(n+1):
        if i%2==0:
            sumeven+=i
        else:
            sumodd+=i
    
    print("Even: ", sumeven)
    print("Odd: ", sumodd)

