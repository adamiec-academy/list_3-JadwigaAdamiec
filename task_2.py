def fibonacci_sequence(n):
    return []def fibonacci_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_number(n-1) + fibonacci_number(n-2)
        

def fibonacci_sequence(n):   
    print("[", end='')
    for i in range(n-1):
        print(fibonacci_number(i), ",", end='',)
    print(fibonacci_number(n-1), ']', sep='')
        
        
fibonacci_sequence(9)
