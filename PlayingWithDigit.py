#Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
#
#we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.
import math
def dig_pow(n, p):
    array = []
    iteration = 0
    for i in str(n):
        array.append(math.pow(int(i),p + iteration))
        iteration = iteration +1
    if(sum(array) % n == 0):
        return sum(array) / n
    return -1

