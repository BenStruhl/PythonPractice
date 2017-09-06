# print("we are the nights that say NEIH")
#
# print("we want a fen the size of", 25 + 30 / 6)
# print("Rosters", 100 - 25 * 3 % 4)
#
# print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

def sieve(n):
    x = list(range(2,n))

    for num in x:
    a    for numTwo in x:
            i = x.index(numTwo)
            if (numTwo % num) == 0 and numTwo != num:
                del x[i]

    print(x)

sieve(30)
