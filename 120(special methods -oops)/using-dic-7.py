#  dictionary example

class configuration:
    pass

marks={
    "ds": 200,
    "ml":100,
    "krr":30
}

c1=configuration()

for attr_name,attr_value in marks.items():
    setattr(c1,attr_name,attr_value)

print(c1.krr)
print(c1.ds)    