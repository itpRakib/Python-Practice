#relational operator

a=20 
b=40

print(a>b) #false
print(a<b) #true
print(a>=b) #false
print(a<=b) #true
print(a==b) #false
print(a!=b) #true


#assignment operator

a=20 
b=10

a+=b
print(a) #30

a-=b 
print(a) #20

a*=b
print(a)  #200

a/=b
print(a) #20.0

a%=b
print(a) #0.0

a**=b
print(a) #0.0


#logical operator

a=20 
b=40 

print(a>10 and b>10) #true and true = true
print(a>10 or b>10) #true or true = true
print(not(a>10 and b>10))   #not true = false
print(not(a>10 or b>10))    #not true = false


# type conversion

a=10 #int
b=20.5 #float
c="30" #string

print(float(a)) #int to float
print(int(b))   #float to int
print(int(c))  #string to int
print(float(c))     #string to float
print(str(a)) #int to string
print(str(b))   #float to string
print(str(c))  #string to string

#type casting

a=10
b=20.5
c="30"

print(float(a)) #int to float
print(int(b))   #float to int
print(int(c))  #string to int
print(float(c))     #string to float
print(str(a)) #int to string
print(str(b))   #float to string
print(str(c))  #string to string
print(type(a)) #int
print(type(b)) #float
print(type(c)) #string
print(type(str(a))) #string
print(type(int(b))) #int
print(type(float(c))) #float
