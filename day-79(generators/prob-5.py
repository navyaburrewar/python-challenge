## Create a generator that accepts values using send() and prints double the received value.

# def gen():
   
#     x=yield
#     print(x)

# g=gen()

# next(g)
# g.send(3)

def gen():
    x = yield
    print(x)

g = gen()

next(g)      # start generator
g.send(5)    # send value