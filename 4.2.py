from  math import sqrt
def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
def get_prime_factors(n):
    factors=[]
    while n!=1:
        for x in prime_table:
            while n%x==0:
                factors.append(x)
                n/=x
            if n==1:
                break
    return factors;

prime_table=[]
for i in range(100001):
    if isPrime(i):
        prime_table.append(i)

file=open("liczby.txt","r")
numbers=[]
for line in file:
    numbers.append(int(line))
file.close()
najwiecej_czynnikow=0
najwiecej_unikalnych_czynnikow=0
liczba=0
liczba2=0
for num in numbers:
    factors=get_prime_factors(num)
    unique_factors= len(set(factors))
    if najwiecej_czynnikow<len(factors):
        najwiecej_czynnikow=len(factors)
        liczba=num
    if unique_factors>najwiecej_unikalnych_czynnikow:
        najwiecej_unikalnych_czynnikow=unique_factors
        liczba2=num
        
print(najwiecej_czynnikow, liczba)
print(najwiecej_unikalnych_czynnikow, liczba2)