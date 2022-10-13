lower_bound=int(input("enter the lower bound:"))
upper_bound=int(input("enter the upper bound:"))
step_count=int(input("enter the step count:"))

series=[*range(lower_bound,upper_bound,step_count)]
sum=0
for i in series:
    sum=sum+i
print("sum of",series,"of length",len(series),"is",sum)
