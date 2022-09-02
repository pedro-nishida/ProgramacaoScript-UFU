
from tkinter import N


entry = int(input())

first = entry%10
second = -1

while ( first != second and entry != 0 ):

    first = entry % 10**2
    second = first % 10
    entry %= 10
    

    if (first == second):
        print("0")
        break
    else:
        continue
