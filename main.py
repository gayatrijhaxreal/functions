# print("Hello, World!")

# print("hello how are you ")

# # def hello():
# #     print("this is a hello fnc so i am doing hello")
# # hello()

# # // parameters and arguments
# #   // positional args
# def sum(a,b):
#     print(f"the sum of the number : {a+b}")
# sum(12,12)

# # //default args

# def hello(name,age):
#     print(f"your name is {name} and your age is {age}")

# hello("Gayatri" , 18 )
# hello(age= 18  , name="Gayatri")

# def pallindrome(st):
#     rev =""
#     for  i in range(len(st)-1,-1,-1):
#         rev = rev + st[i]

#     if rev == st:
#         print(f"{st} is a pallindrome")

#     else:
#         print(f"{st} is not an palindrome ")

# pallindrome("naman")
# pallindrome("cursor")

# def hello():
#     return "hello how are you "
# print(hello())

#  // DS (Data Structures)

# // lists


# a = [12,13,14,15,16,1,12,12,13,14,34.5]

# # //1st way sing index:


# for i in range(len(a)):
#     print(a[i])

# # //2nd way directly on values:

# for i in a:
#     print(i)

# print(dir(list))
# l=[1,2,3,4,5]
# l[0]=10

# l.append(6)

# l.insert(1,7)

# print(l)

# // tupple:

# a = [1,3,2,3,4,5,5,5.5,print(),"hello"]

# # a[0]= 12
# # print(a)
# # print(type(a))

# # for i in range(len(a)) :
# #     print(a[i])

# index = a.index(5)
# print(index)

# count = a.count(5)

# print(count)


# a,b,c,d,e=(1,2,3,4,5)

# print(e)

# // set

# s = {1,2,3,4,5}
# print(s)

# // set traversing

# a = {1,2,3,4,5}

# for i in a :
#     print(i)

# // set methods

# a.remove(2)
# print(a)

# // dictonary

# d ={1:"hello",2 :56}

# print(type(d))
# d[1]=100
# d[3]=59
# print(d)

# a = int(input("tell your number :-"))

# try:
#     print(10/a)
# # except ZeroDivisionError:
# except Exception as err:
#     print( f"sorry your number cannot be divided by zero {err}")
# else:
#     print("good there is no exception")

# finally:
#     print("i will run no matter what")

# print("ok i have done  the division")
  

age = int(input("tell your age:"))

try :
    if age < 10 or age >18:
       raise ValueError ("your age must be between 10 and 18")

    else:
        print("welcome to the club")

except Exception as err:
    print(f"an error occured as {err}")



print("the club will start soon")
