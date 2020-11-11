# These are used when we initially don't know how many arguments are needed to be passed to the function

def catch_all(*args, **kwargs):
    print("args: {}".format(args))
    print("kwargs: {}".format(kwargs))


catch_all(1, 2, 3, a=15, b=28)

catch_all(13, keyword=15)

# Args stands for arguments and it returns a tuple of the arguments passed to the function.
# kwards stands for keyword arguments and it returns a dictionary of the keyword arguments

# the name args and kwargs are not important but the asterisk/s(*/**) before them is what's really important

# The operative difference between them is that a single asterisk (*) before the variable means expand this sequence and double asterisk(**) means expand this as a dictionary
