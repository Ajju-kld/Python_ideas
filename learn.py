numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def fit(a):
    if (a==0):
        return 0
    elif a/4 > float(fit(a)):
        return a

even_numbers = list(filter(fit, numbers))

print(even_numbers)