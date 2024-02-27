file=open("liczby.txt","r")
numbers=[]
for line in file:
    numbers.append(line.rstrip())
file.close()
counter=0
first=2137
for x in numbers:
    if x[0]==x[len(x)-1]:
        if counter==0:
            first=x
        counter+=1
print(counter)
print(first)