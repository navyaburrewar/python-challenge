## Create a generator that reads a sentence and yields words one by one.

def sen__1(sentence):
    for word in sentence.split():
        yield word


for word in sen__1("she is a good girl"):
    print(word)        




    