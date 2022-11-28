#unit1
#print()function ()paraenthesis    string-collection of character inside "double quotes" or 'single quotes'   we can use 'single quotes'inside"double quotes"      or "double quotes" inside'single'
print("Hello antra !!")
print('hello!!')
print("hello 'Antra' gupta")
print('hello "Antra" gupta')
print("i'm Antra")
#escape sequences  
#\' single quotes
#\" double quotes
#\\ backslash
#\n new line
#\t tab
#\b backspace
print("hello \"antra\" gupta")
print('I\'m antra')
print("line A\nline B")
print("name \t antra")
print("this is antra\\\\")
print("antra\baa")
#normal; text
print("line a \\n line b")
#\' ~ ' (b)          \\ ~ \(a)    equal to    \\\' - \'
   


#exercise1
print("this is \\\\ double backslash")
print("these are /\/\/\/\/\ mountains")
print("he is\t awesome")
print("\\\" \\n \\t \\\' ")

print("line A  \\n  line B")

# extra thing https://unicode.org/emoji/charts/full-emoji-list.html

print("\U0001F603")
print("\U0001F601"	)
print("\U0001FAE0")

#variable.py

number1=4
print(number1)
number1= 7
print(number1)

name = 'antra'
print(name)

#rule 1 not doing
#1number = 4 not doing
#instead we start ,letter.....first letterI
_name = "Antra"
a1ntra = 18
print(a1ntra)

#snake case writing used in python
user_one_name = "Antra"
print(user_one_name)

#camel case writing but mostly it is used in java
userOneName = "Antra"













#unit2
#if condition ##if condition is true then statement will execute

age = input("enter your age:")
age = int(age)
if age >= 14:
    print("you are above 14")

#pass statement we didn't do this thing without writing code but for info only 
x = 18
if x >18:
    pass


#if-else statement



age = input("enter your age:")
age = int(age)
if age >= 14:
    print("you are above 14")
else:
    print("sorry ,you can't play ; you are below  age 14")


#exercise2
winning_number = 4
user_input = input("guess a number btw 1 and 100:")
user_input = int(user_input)
if user_input == winning_number:
    print("You Win!!!")
else:
    if user_input < winning_number:
        print("too low")
    else:
            print("too high")

#and,or operator at same time
name = 'antra'
age = 18
if name == 'antra' and age == 18:
    print("true")
else:
    print("false")

#any one condition true its shows true
    name = 'antra'
age = 18
if name == 'antra' or age == 18:
    print("true")
else:
    print("false")

#exercise3
user_name = input("enter your name : ")
user_age = input("enter your age : ")
user_age = int(user_age)
if user_age >= 10 and (user_name[0]=='a' or user_name[0] == 'A'):
   print("you can watch coco")
else:
   print("you can't watch coco")

   #if elif else

##show ticket  pricing  1 to 3 free  4 to 10 50  10 to 60 100   60 to 80  150
age = input("please enter your age :")
age = int(age)
if age==0:
    print("you cannot watch")

elif 0<age<=3:
    print("ticket pricing:free")
elif 3<age<=10:
    print("ticket pricing: 50")
elif 10<age<=60:
    print("ticket pricing: 100")
else:
  print("ticket price : 150")

 ## #in keyword

name = "antra"
if 'r' in "antra":
      print("r is present in name")
else:
     print("not present")

 ###check empty or not

     name =  input("enter your name : ")
     if name: #true if string is not empty
      print(f"your name is {name}")
     else:
        print("you didn\'t type anything")

####while loop

i = 1
while i<=10:
    print("antra")
    i = i+1
    #or
i = 1 # i = 2, i = 3
while i<=10:
    print(f"antra{i}")
    i = i+1

#sum of a number
total = 0
i = 1 #i = 2
while i <= 10:
    total = total + i 
    i = i+1
    print(total)
    #total = 0+1

#exercise4

n = input("enter a number : ")
n = int(n)
total = 0
i = 1
while i <= n:
    total += i
    i += 1
    print(total)


#exercise5

number = input("enter a number ")
#"1256"length = 4, last index = 3
#int(number[i]) 
total= 0
i = 0
while i < len(number):
  total += int(number[i])
  i += 1
  print(total)

#exercise6

name = input("enter your name:")
temp_var = ""
i = 0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
    print(f"{name[i]} : {name.count(name[i])}")
    i += 1

#for loop with range function
for i in range(1,9):
    print(f"hello antra:{i}")


#sum from 1 to 20   1+2+....20
#total = 0
###for i in range(1,21):
   # total += i
   # print(total)
n = int(input("enter your fav.number:"))
total = 0
for i in range(1,n+1):
    total += i
    print(total)

# practice for loop
total = 0
num = input("enter a number:")
for i in range(0,len(num)):
 total += int(num[i])
print(total)


#for loop same example5
name = input("enter your name:")

temp = ""
for i in range (len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
temp += name[i]

#break and continue keyword
#1 to 10 print
#for i in range (1,11):
#if i == 5:
#break
#print(i)
#print 1 to 4,but not 5

for i in range(1,11):
  if i == 5 :
    continue
print(i)

#exercise 7

winning_number = 45 
guess = 1 
number = int(input("guess a number between 1 and 100 : ")) 
game_over = False  
while not game_over:     
    if number == winning_number:      
        print(f"you win,and you guessed this number in {guess} times")      
        game_over = True 
    else:   
         if number < winning_number:    
             print("too low")    
         else :
          print("too high")

          guess += 1
        
         number = int(input("guess again : "))   
         guess += 1
            

# for i in range(0,11,2):
#print(i)
#10,9,8
for i in range(10,0,-1):
    print(i)


#for loop strings
#name = "antra"  
#for i in "soumya"
#print(i)
#1234.... 1+2+3+4
num = input("enter a number :")
total = 0
for i in num:
 total += int(i)
 print(total)

#infinite loop
i = 0
while i <= 10:
    print("hello antra")
    i += 1
    #or
    while True:
        print("hello antra")















        

#unit3


































































































































































































