#from tkinter import *;

grd = {
    "A+":4.0, "A":4.0,"A-":3.7, "B+":3.3, "B":3.0, "B-":2.7,
    "C+":2.3, "C":2.0, "C-":1.7, "D+":1.3, "D":1.0, "F":0,
    "a+":4.0, "a":4.0,"a-":3.7, "b+":3.3, "b":3.0, "b-":2.7,
    "c+":2.3, "c":2.0, "c-":1.7, "d+":1.3, "d":1.0, "f":0 
}
lcv = 1
totalHours = 0
gradeStr = ""
total = 0
while(True):
    lcv = float(input("Enter class hours (or 0 to finish):\t"))
    if(lcv != 0):
        totalHours += lcv
        grade = input("Enter grade (e.x. \"B+\", \"A\"):\t")
        total += grd[grade] * lcv
    else:
        break
if(totalHours != 0):
    total /= totalHours
else:
    print("No classes entered")
print(total)
print("<Press Enter Key to exit>")
input()