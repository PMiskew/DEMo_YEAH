import math

print("Cosine Law Calculator")
#Single Comment - anything on this line is ignored.
#Assignment Statement:
#   This is a line of code with an equal sign
#   x = 4
#   x = 2 + 3 * 3
#   x = input()
#   Evaluate the rigth hand side first then take the result and put it in the left variable
#INPUT
a = input("Side A: ") #Stops the program and waits for the user to type something and press enter.
b = input("Side B: ")
c = input("Side C: ")

print(math.cos(0))
x = math.acos(0)
print(x)
'''
Type Matters:
    When a program stores information it needs to know what type of information - this impacts how the
    information is stored and can be used. 
    
    String 
        any collection of characters - Words or sentences. 
    Numeric Types - 
        - Integers
        - Floats/Double (real numbers)
    Boolean 
        - True or false

BIG IDEA:  ALL INPUTS ARE STRINGS!!!
a = "1" not a = 1
When you add strings together "1" + "2" = "12"
When you add integers together 1 + 2 = 3

We need a way to tell the computer that the user is going to input numbers in our case lets say float (real numbers)

CASTING - Casting is the process of changing type

'''
#casts my inputs into floats
a = float(a)
b = float(b)
c = float(c)


sum = a + b + c
print(sum)

#PROCESS


#OUTPUT




'''
Block Comment: Anything within the thre single quotes is ignored. 

'''
