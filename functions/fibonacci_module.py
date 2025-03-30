def fibonacci_series(n):
    if n<0:
        return "please enter a positive integer"
    a,b = 0,1
    fib_sequence=[a]
    count=1
    while count<1:
        fib_sequence.append(b)
        c = a + b
        a =  b
        b = c
        count+=1
    return fib_sequence