#This is a module that contains all the special math functions
import math

#define functions at the top

'''
This function takes three lenghts and returns the first parameter corrisponding angle. 
'''
def findAngle(a,b,c):

    #This needs to apply Cosine Law
    angleA = (a * a - b * b - c * c) / (-2 * b * c)  # assignment statement
    angleA = math.acos(angleA)  # self-referencing assignment statements
    angleA = math.degrees(angleA)  # self-referencing assignment statement
    angleA = round(angleA, 5)

    # a return statement stops the function and gives something back
    return angleA



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

angleA = findAngle(a,b,c)
angleB = findAngle(b,c,a)
angleC = findAngle(c,a,b)




#When concating a string to a float you have to cast the float back to a str.
print("Angle A: "+str(angleA)+" degrees.")
print("Angle B: "+str(angleB)+" degrees.")
print("Angle B: "+str(angleC)+" degrees.")

check = angleA + angleB + angleC
print(check)







#OUTPUT