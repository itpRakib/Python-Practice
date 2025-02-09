#practice 1

first = int(input("Enter your first : "))
second =int(input("Enter your second : ")) 

print("Sum =",  first + second )

#practice 2

side = float(input("Enter the side of the square : "))

print("Area of the square is : ", side * side)

#practice 3

a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))

print("average of the two numbers is : ", (a+b)/2)

#practice 4

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

print(a>=b)

#practice 5
name=input("Enter the string : ")
print("Length of the string is : ", len(name))

#practice 6

str = "Hey there, $how are you?"
print(str.count("$")) #1


#practice 7

num = int(input("Enter the number : "))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


#practice 8

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))
d = int(input("Enter 4th number : "))

if a>=b and a>=c:
    print("The greatest number is 1st: ", a)
elif b>=a and b>=c:
    print("The greatest number is 2nd: ", b)
elif c>=a and c>=b:
    print("The greatest number is 3rd: ", c)
else:
    print("The greatest number is 4th: ", d)

#practice 9

x = int(input("Enter the number : "))

if x% 7 == 0:
    print("The number is divisible by 7")
else:
    print("The number is not divisible by 7")


#practice 10

movies = []
movies.append(input("Enter your favorite movie1 : "))
movies.append(input("Enter your favorite movie2 : "))
movies.append(input("Enter your favorite movie3 : "))

print(movies)



#practice 11
#palindrome

list1 =[1,2,1]
list2=[1,2,3]

copy_list1 = list1.copy()   
copy_list1.reverse()

if (copy_list1 == list2):
    print("The lists are same")
else:
    print("The lists are not same")
    

#practice 12

grade=["C","D","A","A","B","B", "A"]
grade.sort()
print(grade)

 #practice 13

dictionary ={
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "a chart"]
}
print(dictionary)


