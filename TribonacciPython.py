def tribonacci(signature, n):
    #signature is an array of number 
    #n is a positive number 
    if n <= 0:
        return []
    else:
        if(n <=3):
            tmp = []
            for i in range(0,n):
                tmp.append(signature[i])
            return tmp
    #otherwise
    upperBoundary = n - len(signature)
    lastNumberCalulated = 0
    for i in range(0,len(signature)):
        lastNumberCalulated = lastNumberCalulated + signature[i]
    signature.append(lastNumberCalulated);
    for i in range(1,upperBoundary):
        lastNumberCalulated = lastNumberCalulated + theSumOfTheLastTwoNumberBefore(signature)
        signature.append(lastNumberCalulated)
    return signature

def theSumOfTheLastTwoNumberBefore(signature):
    numberOfElements = len(signature)
    return signature[numberOfElements-2] + signature[numberOfElements-3]


if( __name__ == "__main__"):
    print(tribonacci([1, 1, 1], 10))
    # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]