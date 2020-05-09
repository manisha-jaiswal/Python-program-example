#write a program who take input from user , when the input is >100 then print congratulation you give the number greater than 100

while(True):
    inp=int(input("Enter a number \n"))
    if inp>100:
        print("Congrats you have entered a number greater than 100 \n")
        break
    else:
        print("Try again \n")
        continue
