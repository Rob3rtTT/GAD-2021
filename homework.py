import hwmodule
def your_function(*args, **kwargs):
    s=0
    for i in args:
        if type(i)==int:
            s+=i
    return s
your_function(1, 5, -3, "abc", [12, 56, "cad"])
your_function()
your_function(2, 4, "abc", param_1=2)

def integer(num):
    if type(num) == int:
        print(num)
    else:
        print(0)
integer(input())

hwmodule.sum(10)
hwmodule.even_sum(10)
hwmodule.uneven_sum(10)

def is_palindrome(word):
    reversed = ""
    i=0
    while i<len(word):
        char=word[i]
        reversed+=char
        i+=1
    return reversed == word

def doubler(numbers):
    i = 0
    while i < len(numbers):
        numbers[i] = numbers[i] * 2
        i+=1
    return numbers

def doubler2(numbers):
    doubled = []
    for i in numbers:
        doubled.append(i*2)
    return doubled
print(doubler([1,2,3,4]))
print(doubler2([1,2,3,4]))

def yell(words):
    yelled=[]
    for i in words:
        yelled.append(i.upper())
    return yelled
print(yell(["hello", "world"]))

def element_time_index(nums):
    multiplied = []
    i=0
    while i < len(nums):
        number=nums[i]
        multiplied.append(number * i)
        i+=1
    return multiplied
print(element_time_index([1,2,3,4,5,6,7]))



