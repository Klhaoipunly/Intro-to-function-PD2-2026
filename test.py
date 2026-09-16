def add(x,y):
    z=x + y
    #variables her only accessible in the function, SCOPE
    print(z)
    return x + y

z = add(5,15)