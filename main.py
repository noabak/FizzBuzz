
print("*** FIZZBUZZ GAME ***")

numero=int(input("Please enter a number between 1 and 100:"))
if numero >=1 and numero<=100:
    print(numero)
    print("---")
    x=1
    while x<=numero:
        if x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)
        x=x+1

else:
    print("Warning: The number is smaller than 1 or bigger than 100!")




