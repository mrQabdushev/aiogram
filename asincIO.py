# def multiply(a, b):
#     print(a*b)
#
# multiply(2, 2)





def generator(a, b):
    while True:
        yield a * b
        a =+ 1

generator(2, 2)


#dir(g)
#dir(multiply)


#g.__iter__

#next(g)

#next(g)
