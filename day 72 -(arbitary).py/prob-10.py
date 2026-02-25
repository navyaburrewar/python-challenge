## Write a function that merges multiple dictionaries passed using *args.


def function(*args):
    merged ={}
    for dictionary in args :
        merged.update(dictionary)
    return merged
    
d1 ={ "a": 1 ," b" :2}
d2 ={"c":20}
d3 ={}
print(function(d1,d2,d3))                      
    