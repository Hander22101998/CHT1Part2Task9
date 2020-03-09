n = int(input('-->'))
factorial = 1
if n < 0:
    print('Sorry, factorial doesnt exist')
elif n == 0:
    print('The factorial of 0 is 1')
else:
    for i in range(1, n + 1):
        factorial = factorial * i 
    print(n, factorial)
