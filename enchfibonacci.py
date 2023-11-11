def enhanced_fibonacci(n, b, p):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return b**(enhanced_fibonacci(n-1, b, p) + enhanced_fibonacci(n-2, b, p)) % p
    
n = int(input("Write n: "))
b = int(input("Write b: "))
p = int(input("Write p: "))

nth = 0
numbers = []

while nth < n:
    number = enhanced_fibonacci(nth, b, p)
    numbers.append(number)
    nth += 1
    print(f'N: {number}')

print('The nth number is:', numbers[-1])