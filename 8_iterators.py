class test:
    def __init__(self,limit): 
        self.limit=limit
    def __iter__(self):
        self.x=start
        return self
    def __next__(self):
        x=self.x
        if(x>self.limit):
            raise StopIteration
        else:
            self.x=x+1
        return x

start=int(input("start:"))
limit=int(input("limit:"))
if(limit>start):
    for i in test(limit):
        print(i)
else:
    print("limit should be gratre than start")