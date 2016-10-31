def sieve():
    yield 2
    
    D = {}
    q = 3
    
    while True:
        p = D.pop(q, 0)
        
        if p:
            x = q + p
            
            while x in D: 
                x += p
                
            D[x] = p
        else:
            yield q
            D[q * q] = 2 * q
            
        q += 2

N, Q = [int(temp) for temp in input().split(' ')]
A = [int(temp) for temp in input().split(' ')]
B = list()
A_temp = list()
ith_prime = sieve()

for q in range(Q):
    i = q + 1
    prime_val = next(ith_prime)
    
    while len(A) != 0:
        if A[-1] % prime_val == 0:
            B.append(A[-1])
        else:
            A_temp.append(A[-1])

        A.pop()
        
    while len(B) != 0:
        print(B[-1])
        B.pop()

    A = A_temp 
    B = list()
    A_temp = list()

while len(A) != 0:
    print(A[-1])
    A.pop()

