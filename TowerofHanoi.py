'''In this program an algorithm which will allow the user to find a solution to the
Tower of Hanoi problem. The algorithm that is developed will make a recursive call'''
def printmove(fr, to):
    print("Move from"+str(fr)+"to"+str(to))
def Towers(n,fr,to,s):
    if n==1:
       printmove(fr, to)
    else:
        Towers(n-1,fr,s,to)
        Towers(1,fr,to,s)
        Towers(n-1,s,to,fr)
import time                #We import the time module
print("Welcome to the tower of hanoi problem")
time.sleep(0.4)            #This function halts the execution of the program for a certain time
n=int(input("How many discs are there?"))
fr=int(input("Starting from...?")) #declare from which pole you start
to=int(input("To which pole....?"))#declare your destination pole
s=int(input("Declare a spare..."))#declare a spare pole
print("Working on it........")
time.sleep(1)
Towers(n,fr,to,s)

