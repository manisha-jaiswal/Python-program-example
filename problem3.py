#exercise print pattern
"""
input = integer n
boolean=true or false
true
*
**
***
****
false
****
***
**
*

print("How Many Row You Want To Print")
row= int(input())
print("give boolean value 0 or 1")
bo = int(input())
new =bool(bo)
if new == True:
    for i in range(1,row+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(row,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()
"""
print("Pattern Printing")
num=int(input("how many row you want to print "))
print("Enter 1 or 0 ")
bool_val=input("1 for true value and 0 for false value ")
if bool_val=="1":
    for i in range (0,num+1):
        print("*"*i)
else:
    for i in range(num,0,-1):
        print("*"*i)
