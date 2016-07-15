#This is a program to make a simple alarm
#We are going to open a youtube page to act as an alarm




import time             #Import time module
import webbrowser   #import webbrowesr module

d=input("Whether time will bw entered in Hours, Minutes or Seconds") #Prompt the user 

if d=="Hours":
    temp=int(input("Enter the no of hours")) 
    t=temp*3600                                      #convert hours to seconds for the time module
    time.sleep(t)                                        #sleep function to halt the program
elif d=="Minutes":
    temp=int(input("Enter no of minutes"))
    t=temp*60                                           #convert to seconds
    time.sleep(t)
elif d=="Seconds":
    temp=int(input("Enter the no of seconds"))
    t=temp
    time.sleep(t)
url="https://www.youtube.com/watch?v=9SKFwtgUJHs"  #Enter the url as a variable
webbrowser.open(url,new=2)               #the open function to open the default browser
                                                       # the 'new=2' will open the video in a new tab 
