#quiz,ek list bnao ,then phle check kro wo number hai ya nh aur us list me se whi chije print kro jo 6 se bri ho
list1=[1,5,8,9,7,6,int,float,"manu"]
print(list1)
for item in list1:
    if str(item).isnumeric() and item>6:
        print(item)