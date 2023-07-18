def Divisibilityby3(A):
    num=0
    for ele in A:
        num+=ele
    return 0 if num%3 else 1
if __name__ == '__main__':
    A=list(map(int,input().split()))
    print(Divisibilityby3(A))
"""
Divisibility by 3
Given a number in the form of an array A of size N. Each of the digits of the number is represented by A[i]. Check if the number is divisible by 3.
"""