# #1
# a = None
# b = 0
# c = False
# d = ''
# e = None
# print (f"a==b:{a==b}")
# print (f"a==c:{a==c}")
# print (f"a==d:{a==d}")
# print (f"a==e:{a==e}")

# #2
# a = 32
# b = 3.141592
# c = True
# d = 'Python Programming is interesting!!'
# e = {1, 3, 2, 3, 4}
# f = (4, 'five', 6.0, {'one'})
# g = [1, '1.1', 1.2, (2,)]
# h = {0: 'zero', 1: 'one', 2: 'two'}
# print (type(a))
# print (type(b))
# print (type(c))
# print (type(d))
# print (type(e))
# print (type(f))
# print (type(g))
# print (type(h))

#3
#fname=input("first name:")
#mname=input("middle name:")
#lname=input("last name:")
#print (f"{fname},{mname},{lname}")

#4
#first = int(input("enter first number"))
#second =int(input("enter second number"))
#sum= first+ second
#difference= first -second
#print(f"{first}+{second}= {sum}")
#print (f"{first}- {second}={difference}")

# #5
# day= input("enter a day of a week:")
# match day.lower():
#     case ("saturday"|"sunday"):
#         print (f"{day} is a weekend day")
#     case ("monday"|"tuesday"|"wednesday"|"thursday"|"friday"):
#         print (f"{day} is a weekday")
#     case _:
#         print ("this is not a valid day")

#6
# import random
# options_bool=[True,False]
# small= random.choice(options_bool)
# print (small)
# green= random.choice(options_bool)
# print (f"small:{small}")
# print (f"green:{green}")
# match (small,green):
#     case (True,True):
#         print ("pea")
#     case (True,False):
#         print ("cherry")
#     case (False,True):
#         print ("watermelon")
#     case (False, True):
#         print ("pumpkin")


#7
# import random
# guess=random.randint(1,10)
# secret=random.randint(1,10)
# print (f"the random guess is:{guess}")
# if guess<secret:
#     print ("too low")
# elif guess>secret:
#     print ("too high")
# else:
#     print ("just right")
#     print (f"the random guess is:{secret}")

#8
# x=input("enter the x:")
# y=input("enter the y:")
# point =(x,y)
# match point:
#     case (x,y) if x==y:
#         print (f"the x and the y are equal ({x},{y})")
#     case (a,b) if a>b:
#         print (f"the point is: ({a},{b})")
#     case (p,q):
#         print (f"the point (x,y): ({p},{q})")

#9
# import random
# option=["rocks","scissors","paper"]
# computer=random.choice(option)
# player= random.choice(option)
# print (f"computer's choice: {computer}")
# print (F"player's choice: {player}")
# match (computer,player):
#     case ("rocks","rocks")|("paper","paper")|("scissors","scissors"):
#         print ("its a tie")
#     case ("rocks","scissors")|("scissors","paper")|("paper","rocks"):
#         print ("computer win")
#     case ("scissors","rocks")|("paper","scissors")|("rocks","paper"):
#         print ("player win")

# start=1
# end=10
# for (start <end):
# # for (int x=0;x<=10;x++):

# for (int x = 0; x <= 10; x++)--------------------------

# x=0
# y=5
# for i in range(y-x):
#     print (x)
#     x+=1
# x=1
# y=10
# for i in range(x,y):
#     print (x)
#     x+=1

# for i in range(1,5):
#     print(f"{'x':>2}{'x^2':>5}{'x^3':>7}")


#for i in range(1,4):
 #   print(f"{'x':>2}{'x^2':>5}{'x^3':>6}")
  #  
   # print(f"{'----':>2}{'----':>5}{'----':>6}")
    #print("---"*6)
    #print(f"{i:>2}{i**2:>5}{i**3:>7}")



#13
# while True:
#         a=input("enter first charactor, ").upper()
#         b=input("enter second charactor, ").upper()
#         if a <b:
#             break
# print("==="*14)
# #print(f"{"letter":>7} |{"decimal":>7} |{"octal":>7} |{"hexadecimal":>7}")
# print("---"*14)
# for code in range(ord(a),ord(b)+1):
#      letter=chr(code)
#      decimal= code
#      octal= oct(code)[2:]
#      hexa= hex(code)[2:].upper()
#      print(f"{letter:>7} |{decimal:>7} |{octal:>7} |{hexa:>7}")
#      print("---"*14)




# while True:
#     a= input("enter, ")
#     b= input("enter, ")
#     if a<b:
#         break
# print("hi")
# # for code in {ord(a),ord(b)+1}:
#     letter=chr(code)
#     decimal=code
#     octal= oct(code)
#     hexa=hex(code)
#     print (f"letter{letter},decimal{decimal}, octal{octal},hexa{hexa}")

# a= int(input("enter, "))
# for i in range(a+1,0,-1):
#    print (f"{(i-1)*' '}{(a+1-i)*'*'}")




# n=int(input("en, "))
# def fibonacci_iterative(n):
    
#     a, b = 0, 1
#     for _ in range(2, n+1):
#         a, b = b, a + b
#     return b
# y= fibonacci_iterative(n)
# print(f"{y}")

# n=int(input("en, "))
# a, b = 0, 1
# for _ in range(2, n+1):
#     a, b = b, a + b
#     print(f"0,1,g;{b}")

#def even_odd():
# a=int(input("en, "))

# b=[input(f"input({i+1})") for i in range(a)]
# print (f"b is {b}")
# for n in range(a):
#     if int(b[n])%2==0:
#         print (f"enve,{b[n]}")

# detail ={
#     "name": "hong",
#     "age": 5,
#     "city" : "toronto"
#         }
# print(detail.keys())

# sen='jignaae'
# vo="ae"
# total=0
# for i in vo:
#     count=sen.count(i)
#     total=count+total
#     print (f"vo;{vo},,{count}")


# first = input("Enter your first name: ")
# last = input("Enter your last name: ")
# def fun(first,last):
#     word= first.split()+last.split()
#     for i in word:
#         print(f"{i[0]}")
# fun(first,last)


# while True:
#     a=input("en, ")
#     b=input("en, ")
#     if a<b:
#         break
# for i in range(ord(a),ord(b)):
#     letter=chr(i)
#     decimal=i
#     octal=oct(i)
#     heximal=hex(i)
#     print (f"is,{letter},{octal},{heximal}")


# word= input("enter the word, ").lower()
# v=0
# vowels="aeiou"
# for chr in vowels:
#     b=word.count(chr)
#     v=v+b
#     print(b)
# print(f"the word has {v} vowels")


# def find_factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#         print(fact)
#     return fact
# num=int(input("enter a number: "))
# print(f"the facrorial of {num} is {find_factorial(num)}")


# def reverse_string(s: str) -> str:
#     if len(s) <= 1:
#         return s
#     return s[-1] + reverse_string(s[:-1])
# n=input("enter, ")
# # print (reverse_string(n))

# n=int(input("en, "))
# def sum_n(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum_n(n - 1)
# res=sum_n(n)
# print(f"is={res}")


n=int(input("en, "))
def sum_of_cubes_smaller_than_n(n):
    
    if n <= 1:
        return 0
    
    total_sum = 0
    for i in range(1, n):  # Iterates from 1 up to (n-1)
        total_sum += i**3
    return total_sum
c=sum_of_cubes_smaller_than_n(n)
print (c)
    

    








    

     



    

    


    




    



    




    








