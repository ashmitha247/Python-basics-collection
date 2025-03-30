import fibonacci_module

n = int(input("Enter the max value of terms: "))
result = fibonacci_module.fibonacci_series(n)

if isinstance(result,list):
    print(f"The fibonacci series upto {n}:")
    for num in result:
        print(num,end=" ")
else:
    print(result)