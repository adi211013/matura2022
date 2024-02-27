
file=open("liczby.txt","r")
numbers=[]
x=3;
for line in file:
    numbers.append(int(line))
file.close()
trojkicounter=0
piatkicounter=0
trojki=[]
for i in range(0,len(numbers)):
    for j in range(0,len(numbers)):
        for k in range(0,len(numbers)):
            if numbers[i]!=numbers[j] and  numbers[j]!=numbers[k] and numbers[j]%numbers[i]==0 and numbers[k]%numbers[j]==0:
                trojkicounter+=1
                temp=[numbers[i],numbers[j],numbers[k]]
                trojki.append(temp)
                    
for i in range(0,len(numbers)):
    for j in range(0,len(numbers)):
        for k in range(0,len(numbers)):
            for l in range(0,len(numbers)):
                for z in range(0,len(numbers)):
                    if numbers[i]!=numbers[j] and  numbers[j]!=numbers[k] and numbers[k]!=numbers[l] and numbers[l]!=numbers[z] and numbers[j]%numbers[i]==0 and numbers[k]%numbers[j]==0 and numbers[l]%numbers[k]==0 and numbers[z]%numbers[l]==0:
                        piatkicounter+=1
                    
print(trojkicounter)
print(trojki)
file2=open("trojki.txt","w");
for xd in trojki:
    file2.write(str(xd[0])+" "+str(xd[1])+" "+str(xd[2])+"\n")
print(piatkicounter)