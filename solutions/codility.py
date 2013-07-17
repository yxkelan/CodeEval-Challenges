########################
# 
# PrefixSet
# A non-empty zero-indexed array A consisting of N integers is given. 
# The first covering prefix of array A is the smallest integer P such that 0≤P<N 
# and such that every value that occurs in array A also occurs in sequence A[0], A[1], ..., A[P].
# For example, the first covering prefix of the following 5−element array A:
# A[0] = 2  A[1] = 2  A[2] = 1
# A[3] = 0  A[4] = 1
# is 3, because sequence [ A[0], A[1], A[2], A[3] ] equal to [2, 2, 1, 0], 
# contains all values that occur in array A.
#
# Write a function
# def solution_prefix(A)
#
# that, given a zero-indexed non-empty array A consisting of N integers, 
# returns the first covering prefix of A.
# Assume that:
# N is an integer within the range [1..1,000,000];
# each element of array A is an integer within the range [0..N−1].
# For example, given array A such that
# A[0] = 2  A[1] = 2  A[2] = 1
# A[3] = 0  A[4] = 1
# the function should return 3, as explained above.
# 
# Complexity:
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N), 
# beyond input storage (not counting the storage required for input arguments).
#
################


def solution_prefix( A ):
    
   D = {}
   sum = 0
   for v in A:
     if not v in D:
       D[v]=1
       sum += 1
   
   for i,v in enumerate(A):
    if D[v] == 1:
      D[v] = 0
      sum -= 1
    if sum == 0:
      return i

###################
#
# LinkedIn - slideshare test:  Calculating N!, and calculate the sum of digits of N!
# N - [1,,2000]
# if sum is > 1000000000, then return -1
#
###################

def solution ( N ):
    
    P = 1
    for i in range(1,N+1):
        P = P * i
        
    sum = 0
    
    while not P == 0:
        res = P % 10
        P = (P - res)/10
        sum += res
        if sum > 1000000000:
            return -1
    
    return sum