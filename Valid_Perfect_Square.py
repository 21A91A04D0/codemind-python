for _ in range(int(input())):
    import math
    n=int(input())
    sq=int(math.sqrt(n))
    q=sq*sq
    if n==q:
        print("True")
    else:
        print("False")