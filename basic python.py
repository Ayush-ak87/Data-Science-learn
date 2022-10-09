print("Hello World")
#variables
var1= "Bob"
print(var1)
var1="Sam"
print(var1)
#data type
a=3
print(type(a))
a=3.8
print(type(a))
a=True
print(type(a))
a="Hello"
print(type(a))
a= 4+8j
print(type(a))
#arithmetic operator
#addition
a=15
b=5
print(a+b)
#subtraction
print(a-b)
#multiplication
print(a*b)
#division
print(a/b)
#relational operator
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
#logical Operator
a= True
b= False
#and operator
print(a&b)
print(b&a)
print(a&a)
print(b&b)
#or operator
print(a|b)
print(b|a)
print(a|a)
print(b|b)
#string operator
a1= "This is my first program"
print(a1[0])
print(a1[-1])
print(a1[5:10])
print(len(a1))
print(a1.upper())
print(a1.title())
#tuple
tup1 = (1,"a",True,"b",23.0)
print(tup1[1])
print(tup1[-1])
print(tup1[1:4])
#list
l1 = [1,"a",True,2,"b",False]
print(l1[0])
print(l1[2:5])
l1[0] =100
print(l1)
l1.append("sword")
print(l1)
l1.pop()
print(l1)
#dictionary
d1={"mango":45,"apple":30,"orange":77,"guava":110}
print(d1)
print(d1.keys())
print(d1.values())
d1["mango"] = 100
print(d1)
#sets
s1={3,"a",7.8}
print(s1)
s1={3,"a",7.8,1,1,1,1,"a"}            #does not allow duplicate
print(s1)
s1.add("Hello")
print(s1)
s1.update("b",123,8+5j)
print(s1)
