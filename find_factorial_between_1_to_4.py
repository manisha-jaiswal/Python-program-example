# Write a function to find factorial of given number between 1 to 5?
def fact(num):
    res=1
    while(num>=1):
        res=num*res
        num=num-1
    return(res)
for i in range (1,5):
    print("Factorial of number ",i ,"is ",fact(i))


