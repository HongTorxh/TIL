def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


t = int(input())
for i in range(0,t):
    n = int(input())
    left, right = n//2, n//2
    while left > 0:
        if(isPrime(left) and isPrime(right)):
            print(left, right)
            break
        else:
            left-=1
            right+=1 
        