print("Hello World")

def my_fuction():
    print("This is my function")
    print("A second string")

my_fuction()

def arguments(str1,str2):
    print(str1)
    print(str2)

arguments("Hola","Adios")
arguments("Otro","intento")

def print_function(name,age):
    print("My name is",name,"and my age is",age)
    print("My name is "+name+" and my age is "+str(age))

print_function("Andrea",23)

def print_default(name="Someone",age="unkown"):
    print("My name is",name,"and my age is",age)

print_default("Nick")
print_default(age=27)
print_default(age=23,name="Andrea")

def print_people(*people):
    for person in people:
        print("This person is",person)

print_people("Nick","Jack","King","Smiley")

def return_fuction(num1,num2):
    return num1+num2

math1=return_fuction(5,7)
math2=return_fuction(11,34)

print("First sum is", math1,"Second sum is",math2)


check = "Yo"

if check==False:
    print("It is false")
elif check=="Hambruger":
    print("Yummm,Hamburgers")
elif check=="Yo":
    print("Hello")
else:
    print("It is actually equal to True")


numbers=[1,2,3,4,5]

for item in numbers:
    print("Numbers",item)


run=True
current=1

while run:
    if current==100:
        run=False
    else:
        print(current)
        current+=1