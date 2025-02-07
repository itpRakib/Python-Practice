#strings
str1 = "Hey"
len1 = len(str1)
print(len1)

str2 = "There"
len2 = len(str2)
print(len2)

final_str = str1 + " " + str2
print(final_str)
print(len(final_str))

#indexing

str3 = "Hello"
ch = str3[0]
print(ch)

#slicing

str = "welcome"
print(str[1:4]) #elc
print(str[0:len(str)]) #welcome
print(str[:]) #welcome 
print(str[2:]) #lcome
print(str[:4]) #welc

#negative indexing
print(str[-1]) #e
print(str[-2]) #m
print(str[-3:-1]) #lm

#string methods

str = "hey dude how are you"
print(str.endswith("you")) #true
print(str.capitalize()) #Hey dude how are you
print(str.replace("dude", "buddy")) #hey buddy how are you
print(str.find("dude")) #4
print(str.count("e")) #3


#conditional statements

age = 15
if age >= 18:
    print("You are eligible to vote")
    print("You can vote")
elif age == 17:
    print("You are 17 years old")
else:
    print("You are not eligible to vote")
    print("You cannot vote")


#nesting of if else

age = 18 

if(age>=18):
    if(age>=80):
        print("You cannot drive")
    else:
        print("You can drive")
else:
    print("You cannot drive")