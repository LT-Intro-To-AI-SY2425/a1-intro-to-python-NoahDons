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
    
fibonacci(10)
