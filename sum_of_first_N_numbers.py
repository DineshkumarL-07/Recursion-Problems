# print the sumation of the first N number using recursion
def sumationParameterzied(n,ans):

    if n < 0:
        print(ans)
        return 
    sumationParameterzied(n-1,ans + n)

def sumationsFunctional(n):
    
    if n == 0:
        return 0
    return n + sumationsFunctional(n-1)

N = int(input("Enter the Number: "))
sumationParameterzied(N,0)
print(sumationsFunctional(N))