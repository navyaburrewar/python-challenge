##  Create a function using **kwargs that prints all key-value pairs passed to it.

def func(**marks):

    print("telugu:", marks["telugu"])
    print("hindhi", marks["hindhi"] )

func(telugu= 30, hindhi= 32) 