import matplotlib.pyplot as plt
lang=['python','dbms','java','c++']
popularity=[]
for i in lang:
    p=int(input(i+":"))
    popularity.append(p)
choice=int(input("\n1.Bar chart\n2.pie chart\nenter your choice:"))
if(choice==1):
    plt.bar(lang,popularity,color="blue")
    plt.title("Bar chart")
    plt.xlabel("programin languages")
    plt.ylabel("popularity")
    plt.minorticks_on()
    plt.grid(which="minor",linewidth='0.5',color='black',linestyle=":")
    plt.grid(which="major",linewidth='0.5',color='red',linestyle="-")
    plt.show()
if(choice==2):
    colors=['red','green','yellow','blue']
    explode=[0.1,0,0,0]
    plt.title("Pie chart")
    plt.pie(popularity,labels=lang,colors=colors,explode=explode,autopct='%1.1f%%',shadow=True,startangle=140)
    plt.show()