def calc_factorial(x,processed=""):
    if x==1:
        print('processed ',processed)
        return 1
    else:
        if (processed):
            processed=processed + "*" + str(x)
        else:
            processed=str(x)
        return (x* calc_factorial(x-1,processed))

num=5
print("The factorial ",num,"! is", calc_factorial(num))
