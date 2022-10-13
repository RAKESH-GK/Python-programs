def check_even(l):
    for i in l:
        if(i%2==0):
            print("Yes! list containe even number")
            break
    else:
        print("list Does not coantain even number")

list=[]
list=input("enter the number with whitespace: ").split()
print(list)
print("list is strting format")
print("\nconverting to integer format...")
for i in range(len(list)):
    list[i]=int(list[i])
print("after converting to integer:")
print(list)
print("\nchecking wheather list contains even number:")
check_even(list)