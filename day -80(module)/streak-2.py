##3 using send()


def generator():
    x=yield "start"
    print("recived",x)

    y=yield "middle"
    print("received:",y)

    yield "end"

g=generator()

print(next(g))
print(g.send(16))
print(g.send(24))