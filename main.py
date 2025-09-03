print("Hello, World!")

print("hello how are you ")

# def hello():
#     print("this is a hello fnc so i am doing hello")
# hello()

# // parameters and arguments
#   // positional args
def sum(a,b):
    print(f"the sum of the number : {a+b}")
sum(12,12)

# //default args

def hello(name,age):
    print(f"your name is {name} and your age is {age}")

hello("Gayatri" , 18 )
hello(age= 18  , name="Gayatri")

def pallindrome(st):
    rev =""
    for  i in range(len(st)-1,-1,-1):
        rev = rev + st[i]

    if rev == st:
        print("pallindrome")

    else:
        print("not an palindrome ")

pallindrome("naman")
pallindrome("cursor")

