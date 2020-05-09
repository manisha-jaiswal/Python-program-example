print("enter you age between 7 to 100")
age=int(input())
if age>7 and age <100:
    if(age>18):
        print("you are able to drive")
    elif(age<18):
        print("you are not able to drive")
    else:
        print("we are not decided,you first come here physically then we are decided for this")
else:
    print("Your age is too much")