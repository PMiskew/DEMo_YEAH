#This is a module that contains all the special math functions
import math
#INPUT
#Big Idea: Type matters
#Python - Python 3 takes everything as a String
a = input("What is side A: ")
a = float(a) #float is a function that takes string and returns a float value


b = float(input("What is side B: "))
c = float(input("What is side C: "))

#PROCESS

#Part Process
#
#  a^2 = b^2 + c^2 - 2bcCOS(A)
#
#  COS(A) = (a^2 - b^2 - c^2 )/ (-2bc)
#
angleA = (a*a - b*b - c*c)/(-2*b*c) #assignment statement
angleA = math.acos(angleA) #self-referencing assignment statements
angleA = math.degrees(angleA) #self-referencing assignment statement
angleA = round(angleA,5)

#Power as function
angleB = (pow(b,2) - pow(a,2) - pow(c,2))/(-2*a*c) #assignment statement
angleB = math.acos(angleB) #self-referencing assignment statements
angleB = math.degrees(angleB) #self-referencing assignment statement
angleB = round(angleB,5)

#Python Short Hand a**b is a to the power of b
angleC = (c**2 - a**2 - b**2)/(-2*a*b) #assignment statement
angleC = math.acos(angleC) #self-referencing assignment statements
angleC = math.degrees(angleC) #self-referencing assignment statement
angleC = round(angleC,5)



#When concating a string to a float you have to cast the float back to a str.
print("Angle A: "+str(angleA)+" degrees.")
print("Angle B: "+str(angleB)+" degrees.")
print("Angle B: "+str(angleC)+" degrees.")

check = angleA + angleB + angleC
print(check)







#OUTPUT