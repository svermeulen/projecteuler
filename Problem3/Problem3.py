
def GetPrimeFactors(x):

    for i in range(2, x-1):
        if (x % i) == 0:
            return [i] + GetPrimeFactors(x // i)

    return [x]

print(max(GetPrimeFactors(600851475143)))
